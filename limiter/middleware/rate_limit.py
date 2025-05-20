import time
from django.utils.deprecation import MiddlewareMixin # type: ignore
from django.core.cache import cache # type: ignore
from django.http import JsonResponse # type: ignore

class RateLimitMiddleware(MiddlewareMixin):
    RATE_LIMIT = 100
    WINDOW_SECONDS = 300  # 5 minutes

    def process_request(self, request):
        ip = self.get_client_ip(request)
        cache_key = f"rl:{ip}"
        now = time.time()

        request_times = cache.get(cache_key, [])
        request_times = [ts for ts in request_times if now - ts < self.WINDOW_SECONDS]

        if len(request_times) >= self.RATE_LIMIT:
            return JsonResponse(
                {"detail": "Too Many Requests"},
                status=429
            )

        request_times.append(now)
        cache.set(cache_key, request_times, timeout=self.WINDOW_SECONDS)
        request.remaining = self.RATE_LIMIT - len(request_times)

    def process_response(self, request, response):
        remaining = getattr(request, 'remaining', None)
        if remaining is not None:
            response['X-RateLimit-Remaining'] = str(remaining)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')
