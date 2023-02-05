from django.urls import include, path
from .views import list_rules

urlpatterns = [
    path('list-rules/', list_rules),
]
