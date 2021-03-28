from collections import Counter

import requests
from bs4 import BeautifulSoup
from rest_framework import serializers

from tags.models import Tags


class TagsSerializer(serializers.ModelSerializer):
    url = serializers.URLField(write_only=True)

    class Meta:
        model = Tags
        fields = ('pk', 'url', )

    def create(self, validated_data):
        url = validated_data.pop('url')
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        tags = [tag.name for tag in soup.find_all()]
        counter = Counter(tags)
        instance = self.Meta.model.objects.create(tag_counter=dict(counter))

        return instance


class TagsCelerySerializer(serializers.ModelSerializer):
    url = serializers.URLField(write_only=True)

    class Meta:
        model = Tags
        fields = ('pk', 'url', )
