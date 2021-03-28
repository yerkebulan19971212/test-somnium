from django.urls import path

from .views import CeleryTagsCreateView, Json, TagsCreateView, TagsRetrieveView

urlpatterns = [
    path('', TagsCreateView.as_view(), name="tags_create"),
    path('with-celery/', CeleryTagsCreateView.as_view()),
    path('<int:pk>/', TagsRetrieveView.as_view(), name="tags_detail"),
    path('json/<int:pk>/', Json.as_view())
]
