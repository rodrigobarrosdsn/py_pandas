from django.urls import include, path
from .views import list_rules, populate_excel

urlpatterns = [
    path('list-rules/', list_rules),
    path('populate-excel/', populate_excel),
]
