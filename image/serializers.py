from venv import create
from rest_framework import serializers


class UrlSerializer(serializers.Serializer):
    url = serializers.URLField()
