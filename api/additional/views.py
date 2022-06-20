from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.base import LOGGER


@api_view(['GET'])
def sales(request):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)


@api_view(['GET'])
def node_statistic(request, id):
    # skipped
    return Response(status=status.HTTP_200_OK)
