from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.base import LOGGER
from api.base.serializers import ItemModelSerializer


@api_view(['POST'])
def imports(request):
    items, update_date = request.data['items'], request.data['updateDate']

    for it in items:
        serializer = ItemModelSerializer()
        validated_data = serializer.validate({**it, 'date': update_date})
        serializer.update_or_create(validated_data)

    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
def _delete(request, id):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)


@api_view(['GET'])
def nodes(request, id):
    LOGGER.info('Hello, world!')
    return Response('Hello, world!', status=status.HTTP_200_OK)
