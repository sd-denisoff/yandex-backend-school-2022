from math import floor
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from api.base.models import Item
from api.utils.responses import responses
from api.utils.validation import validate_datetime


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value)
        data = serializer.data
        if data['children'] in ([], None):
            data['children'] = None if value.type == 'OFFER' else []
        return data


class ItemModelSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'type', 'parent', 'price', 'date', 'children']

    def validate(self, data):
        validated_data = {}

        # parent processing
        parent = Item.objects.filter(id=data.pop('parentId', None)).first()
        if parent is not None and parent.type == 'OFFER':
            raise ValidationError(responses[400])
        data['parent'] = parent

        # check data fields
        required_fields = ['id', 'name', 'type']
        for field in self.Meta.fields:
            if field not in data and field in required_fields:
                raise ValidationError(responses[400])
            elif field in data:
                validated_data[field] = data[field]

        # check non-empty name
        if validated_data['name'] is None:
            raise ValidationError(responses[400])

        # check dt format
        validate_datetime(validated_data['date'])

        # check prices
        price = validated_data.get('price')
        if validated_data['type'] == 'CATEGORY' and price is not None:
            raise ValidationError(responses[400])
        if validated_data['type'] == 'OFFER' and (price is None or price < 0):
            raise ValidationError(responses[400])
        if validated_data['type'] == 'OFFER' and validated_data.get('price') is not None:
            validated_data['price_last_update'] = validated_data['date']

        return validated_data

    def update_or_create(self, validated_data):
        id = validated_data.pop('id')
        return self.Meta.model.objects.update_or_create(id=id, defaults=validated_data)

    def update_dates(self, item):
        update_date = item.date
        if item.parent is not None:
            item.parent.date = update_date
            item.parent.save()
            self.update_dates(item.parent)

    def calc_sub_prices(self, prices, item):
        if item['children'] is not None:
            for child in item['children']:
                if child['type'] == 'OFFER':
                    prices.append(child['price'])
                else:
                    sub_prices = self.calc_sub_prices([], child)
                    prices.extend(sub_prices)
        return prices

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['parentId'] = representation.pop('parent')
        if representation['price'] is None:
            prices = self.calc_sub_prices([], representation)
            representation['price'] = floor(sum(prices) / len(prices)) if prices else None
        return representation


class ItemStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'type', 'parent', 'price', 'date']
