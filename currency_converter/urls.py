from django.urls import path, include
from converter.views import ExchangeRateViewSet
from rest_framework import routers, views
from converter import views as hv
from django.views.generic import TemplateView
from django.views.static import serve

router = routers.DefaultRouter()

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('convert/', TemplateView.as_view(template_name='templates/moeda/index.html'), name='index'),
    # path('convert/', serve, {'document_root': 'templates/moeda/index.html'}),
    path('convert/', ExchangeRateViewSet.as_view()),
    path('convert/convert_currency/', ExchangeRateViewSet.as_view())
    
]