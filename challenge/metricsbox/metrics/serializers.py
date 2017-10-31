from rest_framework import serializers
from metrics.models import Metric

class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metric
        fields = ('timestamp', 'name', 'value')
