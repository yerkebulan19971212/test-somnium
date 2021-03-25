from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Tags
from .serializers import TagsSerializer


class TagsCreateView(CreateAPIView):
    serializer_class = TagsSerializer


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
