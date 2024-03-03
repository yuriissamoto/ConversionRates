from converter.models import Exchange
from rest_framework import serializers


# class ExchangeRateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExchangeRate
#         fields = '__all__'
        
# class CurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Currency
#         fields = '__all__'
        
class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'
        
        # def to_internal_value(self, data):
        #     # Validar e converter initialValue para float
        #     if 'initialValue' in data:
        #         initial_value = data['initialValue']
        #         try:
        #             data['initialValue'] = float(initial_value)
        #         except ValueError:
        #             raise serializers.ValidationError({'initialValue': ['Um número válido é necessário.']})
            
        #     # Validar e converter finalValue para float
        #     if 'finalValue' in data:
        #         final_value = data['finalValue']
        #         try:
        #             data['finalValue'] = float(final_value)
        #         except ValueError:
        #             raise serializers.ValidationError({'finalValue': ['Um número válido é necessário.']})

        #     return super().to_internal_value(data)