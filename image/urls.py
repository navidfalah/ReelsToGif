from .api import VideoToImageApi
from django.urls import path, include

urlpatterns = [
    path('video/', VideoToImageApi.as_view(), name="video_image"),
]
