from django.contrib import admin
from .models import (Customer,Product,Orderplaced,Cart)
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=["user","name","locality","city","zipcode","state"]
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=["title","selling_price","discounted_price","description","brand","catagory","Product_image"]
  
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=["user","product","quantity"]

@admin.register(Orderplaced)
class OrderplacedModelAdmin(admin.ModelAdmin):
    list_display=["user","customer","product","quantity","ordered_date","status"]