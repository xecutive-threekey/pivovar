from django.db import models
from account.models import MyUser
from store.models import Item


class Basket(models.Model):
    user = models.ForeignKey(MyUser, verbose_name='пользователь', on_delete=models.SET_NULL, blank=True, null=True)
    sold = models.BooleanField(verbose_name='продано', default=False)

    def __str__(self):
        return f'№{self.pk} пользователя {self.user} продано={self.sold}'


class BasketItems(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.SET_NULL, null=True, verbose_name='корзина')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, verbose_name='товар')
    count = models.IntegerField(verbose_name='колличество товара')

    def __str__(self):
        return f'в корзине={self.basket}, товар={self.item}, колличество={self.count}'

class PaymentMethod(models.Model):
    CARD = "CARD"
    CASH = "CASH"
    PAYMENT_METHOD_CHOICES = [
        (CARD, 'card'),
        (CASH, 'cash'),
    ]
    type_of_payment = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default=CARD,
    )

    def __str__(self):
        return self.type_of_payment


class Order(models.Model):
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE, verbose_name='корзина')
    description = models.TextField(verbose_name='описание заказа', blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, verbose_name='способ оплаты')
    price = models.DecimalField(verbose_name='стоимость заказа', max_digits=10, decimal_places=3)

    def __str__(self):
        return f'заказ номер {self.pk} стоимостью {self.price}'