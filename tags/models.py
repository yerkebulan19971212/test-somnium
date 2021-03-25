from django.db import models
from jsonfield import JSONField


class Tags(models.Model):
    tag_counter = JSONField(null=True)
