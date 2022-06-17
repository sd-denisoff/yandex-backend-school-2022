import json
from pathlib import Path

import yaml
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render


def yaml_to_html(request):
    if hasattr(settings, 'SWAGGER_YAML_FILE'):
        file = open(settings.SWAGGER_YAML_FILE)
        spec = yaml.safe_load(file.read())
        return render(request,
                      template_name=Path(__file__).resolve().parent / 'ui.html',
                      context={'schema': json.dumps(spec)})
    else:
        raise ImproperlyConfigured('Define SWAGGER_YAML_FILE in settings')
