from urllib import request


import requests

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Result


class FibonacciTest(TestCase):
  def test_fibonacci(self):
    factory = APIRequestFactory()
    request = factory.get('api/fibonacci/5/')
    result = Result.objects.get(argument=5)
    self.assertEquals(result.result, 5)
