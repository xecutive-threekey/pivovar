from django.contrib import admin
from .models import Brend, BeerStyle, Volume, PackageType, Country, Category, Discount, Item

admin.site.register(Brend)
admin.site.register(BeerStyle)
admin.site.register(Volume)
admin.site.register(PackageType)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Item)
