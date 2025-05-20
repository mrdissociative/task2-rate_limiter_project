from django.http import JsonResponse # type: ignore

def test_view(request):
    return JsonResponse({"message": "OK"})
