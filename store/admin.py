from django.contrib import admin

from .models.customer import Customer
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
    ordering = ['id']

class AdminProductType(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'sport', 'color']
    ordering = ['id']
    
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'size', 'stock_on_hand']
    ordering = ['name', 'size']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'super_category']
    
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity', 'status']
    ordering = ['-id']

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(SuperCategory)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, AdminProductType)
admin.site.register(Product, AdminProduct)
admin.site.register(Sport)
admin.site.register(Color)
admin.site.register(Size, SizeAdmin)


# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
