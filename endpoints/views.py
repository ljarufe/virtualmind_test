from email.policy import default
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Result


def _fibonacci(num):
    if num < 2:
      return 0
    return _fibonacci(num - 1) + _fibonacci(num - 2)


@api_view()
def fibonacci(request, num):
  result, _ = Result.objects.get_or_create(
    argument=num, defaults={'result':_fibonacci(num)})

  return Response({'message': result.result})

