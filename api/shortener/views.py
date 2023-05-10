from typing import Any

from django.views.generic import RedirectView
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models, serializers
from .serializers import URLSerializer


class CreateShortURLApiView(generics.CreateAPIView):
    """
    create:
    Creates a short URL from the provided original URL.

    Expects JSON data in the format:
    {
        "url": "http://protected-brushlands-01714.herokuapp.com/abcd/"
    }

    Where "url" is the original URL that is to be shortened.

    The response contains the original URL and the shortened URL:
    {
        "url": "http://example.com",
        "short_url": "http://your-domain.com/abcd"
    }
    """

    queryset = models.URL.objects.all()
    serializer_class = serializers.OriginalURLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()

        short_url = URLSerializer(instance=url, context={"request": request})

        return Response(data=short_url.data, status=status.HTTP_201_CREATED)


class ShortUrlRedirectView(RedirectView):
    """
    get:
    Redirects the user to the original URL from the provided short URL.

    Expects the short URL to be part of the path, like:
    http://protected-brushlands-01714.herokuapp.com/abcd/

    Where "abcd" is the short URL.

    The response is a HTTP 302 redirect to the original URL.
    """

    def get_redirect_url(self, *args: Any, short_url: str, **kwargs: Any) -> str | None:
        url = get_object_or_404(models.URL, short_url=short_url)

        return url.url
