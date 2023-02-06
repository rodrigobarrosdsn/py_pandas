from django.urls import include, path
from .views import list_rules, populate_excel, list_evaluate

urlpatterns = [
    path('list-rules/', list_rules),
    path('populate-excel/', populate_excel),
    path('list-evaluate/', list_evaluate)
]
