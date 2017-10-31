# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from metrics.models import Metric
from metrics.serializers import MetricSerializer

# Create your views here.

@csrf_exempt
#@api_view(['GET, POST'])
def metric_collection(request):
    if request.method == 'GET':
        metrics = Metric.objects.all().reverse()
        serializer = MetricSerializer(metrics, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MetricSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonRespons(serializer.errors, status=400)

