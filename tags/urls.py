from django.urls import path

from .views import Json, TagsCreateView, TagsRetrieveView

urlpatterns = [
    path('', TagsCreateView.as_view()),
    path('<int:pk>/', TagsRetrieveView.as_view()),
    path('json/<int:pk>/', Json.as_view())
]
