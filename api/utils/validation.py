from datetime import datetime

from rest_framework.serializers import ValidationError

from api.utils.responses import responses


def validate_datetime(dt_str):
    """ISO 8601 format check"""
    try:
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except ValueError:
        raise ValidationError(responses[400])
