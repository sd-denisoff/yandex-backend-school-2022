from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.base import LOGGER
from api.base.models import Item
from api.base.serializers import ItemModelSerializer
from api.utils.responses import responses


@api_view(['POST'])
def imports(request):
    items, update_date = request.data['items'], request.data['updateDate']

    LOGGER.info('Start imports...')

    for i, item_data in enumerate(items):
        serializer = ItemModelSerializer()
        validated_data = serializer.validate({**item_data, 'date': update_date})
        item, is_new = serializer.update_or_create(validated_data)
        serializer.update_dates(item)
        LOGGER.info(f'({i + 1}/{len(items)}) done')

    LOGGER.info('Imported!')

    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
def _delete(request, id):
    if type(id) is not str:
        return Response(responses[400], status=status.HTTP_400_BAD_REQUEST)

    item = Item.objects.filter(id=id).first()
    if item is None:
        return Response(responses[404], status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def nodes(request, id):
    if type(id) is not str:
        return Response(responses[400], status=status.HTTP_400_BAD_REQUEST)

    item = Item.objects.filter(id=id).first()
    if item is None:
        return Response(responses[404], status=status.HTTP_404_NOT_FOUND)

    serializer = ItemModelSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)
