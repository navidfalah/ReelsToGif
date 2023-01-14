from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UrlSerializer
from moviepy.editor import *
from .models import UrlVideo


class VideoToImageApi(generics.GenericAPIView):
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data["url"]
        clip = VideoFileClip(url)
        clip = clip.subclip(0, 2)
        video_url = UrlVideo.objects.create(url=url)
        clip.write_gif('media/'+str(video_url.pk)+".gif")
        return Response({
                "message": "ok, everything is fine",
                "url":'media/'+str(video_url.pk)+".gif"
        }, status=status.HTTP_200_OK)

