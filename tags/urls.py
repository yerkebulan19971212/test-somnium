from django.urls import path
from .views import TagsCreateView, TagsRetrieveView

urlpatterns = [
    path('', TagsCreateView.as_view()),
    path('<pk>/', TagsRetrieveView.as_view())
]
