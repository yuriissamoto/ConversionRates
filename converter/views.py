from converter.models import Exchange
from converter.serializer import ExchangeSerializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
from django.template import loader


# class IndexView(TemplateView):
#     template_name = "moeda/index.html"
    
ALLOWED_CURRENCIES = {'USD', 'BRL', 'EUR', 'BTC', 'ETH'}

class ExchangeRateViewSet(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def get(self, request, pk=None, format=None):
        # Verifica se a conversão de moeda foi solicitada
        from_currency = request.GET.get('from')
        to_currency = request.GET.get('to')
        amount = float(request.GET.get('amount', '0'))

        if from_currency and to_currency and amount > 0:
            return self.convert_currency(request)
        

        # Se não houver solicitação de conversão de moeda, apenas renderiza a página index
        listservice = Exchange.objects.all()
        showlistservice = ExchangeSerializer(listservice, many=True).data
        return render(request, 'moeda/index.html', {'exchanges': showlistservice})

    def convert_currency(self, request):
        from_currency = request.GET.get('from')
        to_currency = request.GET.get('to')
        amount = float(request.GET.get('amount', '0'))

        if not from_currency or not to_currency:
            return JsonResponse({'error': 'Por favor, especifique a moeda de origem e a moeda de destino'}, status=400)

        if from_currency not in ALLOWED_CURRENCIES or to_currency not in ALLOWED_CURRENCIES:
            return JsonResponse({'error': 'Moeda não suportada'}, status=400)

        if amount <= 0:
            return JsonResponse({'error': 'O valor a ser convertido deve ser maior que zero'}, status=400)

        api_key = '2be61f05b6-cc44adf6fa-s9lfew'
        base_url = 'https://api.fastforex.io/fetch-all'
        params = {'base': from_currency, 'symbols': to_currency, 'api_key': api_key}

        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            if 'error' in data:
                return JsonResponse({'error': data['error']}, status=400)

            if to_currency not in data['results']:
                return JsonResponse({'error': f'A moeda "{to_currency}" não foi encontrada'}, status=400)
            
            

            exchange_rate = data['results'][to_currency]
            converted_amount = amount * exchange_rate

            template = loader.get_template('moeda/conversion_result.html')
            context = {
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'converted_amount': converted_amount
            }
            return HttpResponse(template.render(context, request))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
            

            
    def post(self, request):

        serviceregister_serializer = ExchangeSerializer(data=request.data)
        if serviceregister_serializer.is_valid(raise_exception=True):
            new_user = serviceregister_serializer.save()
            if new_user:
                return Response({'msg': 'Service Registration Successful'}, status=status.HTTP_201_CREATED)
            return Response(serviceregister_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, pk=None, format=None):
    #     listservice = Exchange.objects.all()
    #     showlistservice = ExchangeSerializer(listservice, many=True).data
    #     return Response(showlistservice)