from django.contrib import admin
from basket.models import Basket, BasketItems, PaymentMethod, Order

admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(PaymentMethod)
admin.site.register(Order)
