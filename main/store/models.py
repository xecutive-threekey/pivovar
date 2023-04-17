from django.db import models


class Brend(models.Model):
    name = models.CharField(verbose_name='название бренда', max_length=150)
    discription = models.TextField(verbose_name='описание бренда')

    def __str__(self):
        return self.name


class BeerStyle(models.Model):
    name = models.CharField(verbose_name='стиль напитка', max_length=30)

    def __str__(self):
        return self.name


class Volume(models.Model):
    value = models.DecimalField(verbose_name='объем', max_digits=7, decimal_places=3)

    def __str__(self):
        return str(self.value)+'л'


class PackageType(models.Model):
    package_type = models.CharField(verbose_name='тип упаковки', max_length=30)

    def __str__(self):
        return self.package_type


class Country(models.Model):
    name = models.CharField(verbose_name='страна', max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name='категория', max_length=50)

    def __str__(self):
        return self.name


class Discount(models.Model):
    value = models.IntegerField(verbose_name='скидка')

    def __str__(self):
        return str(self.value)+"%"


class Item(models.Model):
    brend = models.ForeignKey(Brend, verbose_name='бренд', on_delete=models.SET_NULL, blank=True, null=True)
    beer_style = models.ForeignKey(BeerStyle, verbose_name='стиль', on_delete=models.SET_NULL, blank=True, null=True)
    volume = models.ForeignKey(Volume, verbose_name='объем', on_delete=models.SET_NULL, blank=True, null=True)
    package = models.ForeignKey(PackageType, verbose_name='тип упаковки', on_delete=models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name='страна', on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.SET_NULL, blank=True, null=True)
    discount = models.ForeignKey(Discount, verbose_name='скидка', on_delete=models.SET_NULL, blank=True, null=True)
    stock = models.IntegerField(verbose_name='колличество на складе')
    name = models.CharField(verbose_name='наименование', max_length=100)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    price = models.DecimalField(verbose_name='цена', max_digits=7, decimal_places=2)
    img = models.ImageField(upload_to='images', verbose_name='изображение', blank=True, null=True)

    def __str__(self):
        return self.name
