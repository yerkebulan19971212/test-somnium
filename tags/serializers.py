from rest_framework import serializers

from tags.models import Tags
import requests
from collections import Counter
from bs4 import BeautifulSoup


class TagsSerializer(serializers.ModelSerializer):
    url = serializers.URLField(write_only=True)

    class Meta:
        model = Tags
        fields = ('pk', 'url', )

    def create(self, validated_data):
        model_class = self.Meta.model
        url = validated_data.pop('url')
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        tags = [tag.name for tag in soup.find_all()]
        counter = Counter(tags)
        try:
            instance = self.Meta.model.objects.create(tags_counter=dict(counter))
        except TypeError:
            msg = (
                'Got a `TypeError` when calling `%s.%s.create()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.%s.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception was:\n %s' %
                (
                    model_class.__name__,
                    model_class._default_manager.name,
                    model_class.__name__,
                    model_class._default_manager.name,
                    self.__class__.__name__,
                )
            )
            raise TypeError(msg)
        return instance


class TagsRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('tags_counter',)
