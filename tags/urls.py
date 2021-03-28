from django.urls import path

from .views import CeleryTagsCreateView, Json, TagsCreateView, TagsRetrieveView

urlpatterns = [
    path('', TagsCreateView.as_view(), name="tags_create"),  # API без использования celery
    path('with-celery/', CeleryTagsCreateView.as_view()),  # API c Celery
    path('<int:pk>/', TagsRetrieveView.as_view(), name="tags_detail"),  # API получение детали как в документацие
    path('json/<int:pk>/', Json.as_view())  # API получение детали по моему (подумал так получить лучше :) )
]
