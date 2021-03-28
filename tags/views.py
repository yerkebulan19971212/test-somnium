from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Tags
from .serializers import TagsCelerySerializer, TagsSerializer
from .tasks import get_html_tags


class TagsCreateView(CreateAPIView):
    serializer_class = TagsSerializer


class CeleryTagsCreateView(CreateAPIView):
    serializer_class = TagsCelerySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tag = Tags.objects.create(tag_counter=None)
        task = get_html_tags.delay(tag.pk, request.data.get('url'))
        return Response(
            {"pk": tag.pk, 'task_id': task.id, 'task_status': task.status},
            status=status.HTTP_201_CREATED
        )


class TagsRetrieveView(RetrieveAPIView):
    queryset = Tags.objects.all()

    def get(self, request, *args, **kwargs):
        tags = self.get_object().tag_counter

        return Response(tags)


class Json(TagsRetrieveView):
    def get(self, request, *args, **kwargs):
        tags = self.get_object().tag_counter

        tags_list = []
        for key, value in tags.items():
            tag = {
                "name": key,
                "count": value
            }
            tags_list.append(tag)

        return Response(tags_list)
