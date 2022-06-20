from datetime import timedelta

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.base import LOGGER
from api.base.models import Item
from api.base.serializers import ItemStatisticSerializer
from api.utils.validation import validate_datetime


@api_view(['GET'])
def sales(request):
    now = validate_datetime(request.query_params.get('date'))
    last_24 = now - timedelta(hours=24)

    objects = Item.objects.filter(type='OFFER')
    updated = [obj for obj in objects
               if last_24 <= validate_datetime(obj.price_last_update) <= now]
    items = ItemStatisticSerializer(updated, many=True)

    LOGGER.info(f'Retrieved {len(items.data)} last 24 hours updated items')
    return Response({'items': items.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def node_statistic(request, id):
    # skipped
    return Response(status=status.HTTP_200_OK)
