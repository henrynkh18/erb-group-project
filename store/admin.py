from django.contrib import admin

from .models.customer import Customer
from .models.gender import Gender
from .models.orders import Order
from .models.supercategory import SuperCategory
from .models.category import Category
from .models.producttype import ProductType
from .models.product import Product

from .models.color import Color
from .models.sport import Sport
from .models.size import Size

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'phone']
    list_display_links = ['id', 'email']
    ordering = ['id']

class AdminProductType(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'sport', 'color']
    list_display_links = ['id', 'name']
    ordering = ['id']
    
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'size', 'stock_on_hand']
    list_display_links = ['id', 'name']
    ordering = ['name', 'size']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'super_category']
    list_display_links = ['id', 'name']
    
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_display_links = ['id', 'name']
    ordering = ['-id']   
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity', 'status']
    list_display_links = ['id', 'customer', 'product']
    ordering = ['-id']

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Gender)
admin.site.register(Order, OrderAdmin)
admin.site.register(SuperCategory)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, AdminProductType)
admin.site.register(Product, AdminProduct)
admin.site.register(Sport)
admin.site.register(Color)
admin.site.register(Size, SizeAdmin)