from collections import Counter

import requests
from bs4 import BeautifulSoup
from celery import shared_task

from .models import Tags


@shared_task
def get_html_tags(pk: int, url: str,):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tags = [tag.name for tag in soup.find_all()]
    counter = Counter(tags)
    Tags.objects.filter(pk=pk).update(tag_counter=dict(counter))
