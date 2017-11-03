# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APITestCase
import json

# Create your tests here.

class MetricsTests(APITestCase):
    def test_create_metric(self):
        url = '/metrics'
        data = {'timestamp': 12345,
                'name': 'response_time',
                'value': 300}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        r_data = json.loads(response.content)
        assert(r_data['timestamp'] == 12345)

    def test_metric_aggregate(self):
        url = '/metrics'
        data = {'timestamp': 12345,
                'name': 'response_time',
                'value': 300}
        response = self.client.post(url, data, format='json')
        data = {'timestamp': 12346,
                'name': 'response_time',
                'value': 255}
        response = self.client.post(url, data, format='json')
        data = {'timestamp': 12347,
                'name': 'response_time',
                'value': 230}
        response = self.client.post(url, data, format='json')
        data = {'timestamp': 12348,
                'name': 'response_time',
                'value': 275}
        response = self.client.post(url, data, format='json')

        url = '/metrics/aggregate/12345/12348/response_time'
        response = self.client.get(url)
        r_data = json.loads(response.content)
        self.assertEqual(r_data['name'],'response_time')

    def test_timestamp_metric(self):
        url = '/metrics'
        data = {'timestamp': 12345,
                'name': 'response_time',
                'value': 300}
        response = self.client.post(url, data, format='json')
        data = {'timestamp': 12345,
                'name': 'response_time',
                'value': 255}
        response = self.client.post(url, data, format='json')
        data = {'timestamp': 12346,
                'name': 'response_time',
                'value': 255}
        response = self.client.post(url, data, format='json')

        url = '/metrics/timestamp-metric/12345/response_time'
        response = self.client.get(url)
        r_data = json.loads(response.content)
        self.assertEqual(len(r_data), 2)
