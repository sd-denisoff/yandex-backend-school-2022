from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.base import LOGGER


@api_view(['GET'])
@permission_classes([AllowAny])
def sales(request):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def node_statistic(request, id):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)
