from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib import messages

from store.models.category import Category
from store.models.supercategory import SuperCategory
from store.models.producttype import ProductType
from store.models.product import Product

class ProductDetail(View):
    
    def get(self, request, pk):       
        super_categories = SuperCategory.objects.all()
        categories = Category.get_all_categories()        
        producttype = ProductType.objects.get(id=pk)  
        products = Product.objects.filter(name__pk=producttype.id)

        #product = request.POST.get('product')
        
        data = {}  
        data['producttype'] = producttype
        data['products'] = products
        data['super_categories'] = super_categories
        data['categories'] = categories
        
        return render(request, 'product_detail.html', data)


    def post(self, request, pk):   
        product = request.POST.get('product')
        cart = request.session.get('cart')
        #remove = request.POST.get('remove')
        
        if product:
            if cart:
                quantity = cart.get(product)                
                if quantity:                    
                    cart[product]  = quantity + 1                      
                    # if remove:
                    #     if quantity<=1:
                    #         cart.pop(product)
                    #     else:
                    #         cart[product]  = quantity - 1
                    # else:
                    #     cart[product]  = quantity + 1
                    
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1
                
            messages.success(request, 'Added to cart.', extra_tags='add_to_cart')
            

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        
        return HttpResponseRedirect(f"/product_detail/{pk}")
        

# def product_detail(request, pk):
#     cart = request.session.get('cart')
#     if not cart:
#         request.session['cart'] = {}

#     super_categories = SuperCategory.objects.all()
 
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')        
    
#     product = Products.objects.get(id=pk)  
    
#     data = {}  
#     data['product'] = product
#     data['super_categories'] = super_categories
#     data['categories'] = categories
    
#     return render(request, 'product_detail.html', data)
