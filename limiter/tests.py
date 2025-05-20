from django.test import TestCase, Client # type: ignore
from django.core.cache import cache # type: ignore

class RateLimitTests(TestCase):
    def setUp(self):
        self.client = Client()
        cache.clear()

    def test_100_requests_allowed(self):
        for _ in range(100):
            response = self.client.get("/test/")
            self.assertEqual(response.status_code, 200)

    def test_101st_blocked(self):
        for _ in range(100):
            self.client.get("/test/")
        response = self.client.get("/test/")
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.json().get('detail'), 'Too Many Requests')
