"""challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from metrics import views as metric_views

urlpatterns = [
    # api
    url(r'^metrics$', metric_views.metric_collection),
    url(r'^metrics/range/(?P<t1>\d+)/(?P<t2>\d+)/(?P<name>\w+)$',
        metric_views.metric_range),
    url(r'^metrics/timestamp-metric/(?P<timestamp>\d+)/(?P<name>\w+)$',
        metric_views.timestamp_metric),
]
