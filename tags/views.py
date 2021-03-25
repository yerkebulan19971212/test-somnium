from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TagsSerializer, TagsRetrieveSerializer
from .models import Tags


class TagsCreateView(CreateAPIView):
    serializer_class = TagsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TagsRetrieveView(RetrieveAPIView):
    serializer_class = TagsRetrieveSerializer
    queryset = Tags.objects.all()

