from rest_framework import generics, status
from rest_framework.response import Response

from . import models, serializers
from .serializers import URLSerializer


class CreateShortURLAPIView(generics.CreateAPIView):
    queryset = models.URL.objects.all()
    serializer_class = serializers.OriginalURLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        short_url = URLSerializer(instance=instance, context={"request": request})

        return Response(data=short_url.data, status=status.HTTP_201_CREATED)
