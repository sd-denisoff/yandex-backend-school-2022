"""Products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.urls import include, path, reverse

from api.additional.views import node_statistic, sales
from api.base.views import _delete, imports, nodes
from api.utils.swagger_generator.views import yaml_to_html


def index(request):
    doc_url = reverse('doc')
    return HttpResponse(
        f'Greetings from server! '
        f'SwaggerUI is available <a href={doc_url}>here</a>\n'
    )


api_urlpatterns = [
    # base
    path('imports/', imports, name='imports'),
    path('delete/<str:id>/', _delete, name='_delete'),
    path('nodes/<str:id>/', nodes, name='nodes'),

    # additional
    path('sales/', sales, name='sales'),
    path('node/<str:id>/statistic/', node_statistic, name='node_statistic'),
]

urlpatterns = [
    path('', index, name='index'),
    path('', include(api_urlpatterns), name='API'),
    path('doc/', yaml_to_html, name='doc'),
    path('admin/', admin.site.urls, name='admin'),
]

urlpatterns += staticfiles_urlpatterns()
