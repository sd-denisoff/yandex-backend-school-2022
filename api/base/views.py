from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.base import LOGGER


@api_view(['POST'])
@permission_classes([AllowAny])
def imports(request):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def _delete(request, id):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def nodes(request, id):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)
