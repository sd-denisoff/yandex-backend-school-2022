from datetime import datetime

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from api.base.models import Item
from api.utils.responses import responses


def validate_datetime(dt_str):
    try:
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except:
        raise ValidationError(responses[400])


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def get_model_fields(self):
        return [field.name for field in Item._meta.fields]

    def validate(self, data):
        validated_data = {}

        # parent processing
        parent = Item.objects.filter(id=data.pop('parentId', None)).first()
        if parent is not None and parent.type == 'O':
            raise ValidationError(responses[400])
        data['parent'] = parent

        # check data fields
        model_fields = self.get_model_fields()
        required_fields = ['id', 'name', 'type']
        for field in model_fields:
            if field not in data and field in required_fields:
                raise ValidationError(responses[400])
            elif field in data:
                validated_data[field] = data[field]

        # check non-empty name
        if validated_data['name'] is None:
            raise ValidationError(responses[400])

        # check prices
        price = validated_data.get('price')
        if validated_data['type'] == 'CATEGORY' and price is not None:
            raise ValidationError(responses[400])
        if validated_data['type'] == 'OFFER' and (price is None or price < 0):
            raise ValidationError(responses[400])

        # check dt format
        validated_data['date'] = validate_datetime(validated_data['date'])

        return validated_data

    def update_or_create(self, validated_data):
        id = validated_data.pop('id')
        return self.Meta.model.objects.update_or_create(id=id, defaults=validated_data)
