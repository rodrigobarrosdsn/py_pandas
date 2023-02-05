from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
import pandas as pd
import os
from django.conf import settings
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def list_rules(request):
    """
    List rules of gamefication
    """

    page_size = request.GET['page_size']
    paginator = PageNumberPagination()
    paginator.page_size = page_size
    paginator.page_query_param = 'page'

    static_root = settings.STATIC_ROOT
    file_path = os.path.join(static_root, 'gamefication.xlsx')
    xlsx = pd.read_excel(file_path)

    import ipdb
    ipdb.set_trace()

    rules = Rule.objects.all().order_by("-created_at")

    rules_serializer = RuleSerializer(paginator.paginate_queryset(rules, request), many=True).data

    return paginator.get_paginated_response(rules_serializer)
