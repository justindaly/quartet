# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Metric(models.Model):
    timestamp = models.BigIntegerField()
    name = models.CharField(max_length=200)
    value = models.IntegerField()

    def __str__(self):
        return "timestamp %s, name %s, value %s" % (self.timestamp, self.name, self.value)
