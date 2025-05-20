from django.urls import path # type: ignore
from .views import test_view

urlpatterns = [
    path("test/", test_view),
]
