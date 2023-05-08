from typing import Any

from django.views.generic import RedirectView
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models, serializers
from .serializers import URLSerializer


class CreateShortURLApiView(generics.CreateAPIView):
    queryset = models.URL.objects.all()
    serializer_class = serializers.OriginalURLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, contex={"request": request})
        serializer.is_valid(raise_exception=True)
        url = serializer.save()

        short_url = URLSerializer(instance=url)

        return Response(data=short_url.data, status=status.HTTP_201_CREATED)


class ShortUrlRedirectView(RedirectView):
    def get_redirect_url(self, *args: Any, short_url: Any, **kwargs: Any) -> str | None:
        url = get_object_or_404(models.URL, short_url=short_url)

        return url.url
