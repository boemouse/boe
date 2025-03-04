from django.contrib import admin
from . models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('price','name','stock')

class OrderAdmin(admin.ModelAdmin):
    list_display =('customer_name', 'quantity')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


# Register your models here.
