from django.db import models

# class Currency(models.Model):
#     code = models.CharField(max_length=3, unique=True)
#     name = models.CharField(max_length=100)
    
    

# class ExchangeRate(models.Model):
#     from_currency = models.ForeignKey(Currency, related_name='from_currency', on_delete=models.CASCADE)
#     to_currency = models.ForeignKey(Currency, related_name='to_currency', on_delete=models.CASCADE)
#     rate = models.DecimalField(max_digits=20, decimal_places=10)
    
class Exchange(models.Model):
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=20, decimal_places=10)