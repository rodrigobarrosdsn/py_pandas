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
import base64
from io import BytesIO
from .rules_engine import evaluate_rules
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def list_rules(request):
    """
    List rules of gamefication
    """

    paginator = PageNumberPagination()
    paginator.page_size = request.GET['page_size']
    paginator.page_query_param = 'page'

    rules = Rule.objects.all().order_by("-created_at")

    rules_serializer = RuleSerializer(paginator.paginate_queryset(rules, request), many=True).data

    return paginator.get_paginated_response(rules_serializer)

@api_view(['POST'])
@permission_classes([AllowAny])
def populate_excel(request):
    """
    Populate rules of gamefication
    """
    # static_root = settings.STATIC_ROOT
    # file_path = os.path.join(static_root, 'gamefication.xlsx')
    # xlsx = pd.read_excel(file_path)

    xls_base64_string = request.data['excel']
    xls_binary = base64.b64decode(xls_base64_string)
    xls_file = BytesIO(xls_binary)

    df = pd.read_excel(xls_file)


    for index, row in df.iterrows():
        rule = Regra()
        rule.rule_name = row['rule_name']
        rule.rule_description = row['rule_description']
        rule.rule_criteria = row['rule_criteria']
        rule.rule_outcome = float(row['rule_outcome'])
        rule.rule_field = row['rule_field']
        rule.save()

    return Response({'message': 'success'})

@api_view(['GET'])
@permission_classes([AllowAny])
def list_evaluate(request):
    """
    Populate rules of gamefication
    """
    user_obj = User.objects.get(id=1)
    rules_obj = Regra.objects.all()

    for rule in rules_obj:
        evaluate_rules(user_obj, rule)


    return Response({'message': 'success'})