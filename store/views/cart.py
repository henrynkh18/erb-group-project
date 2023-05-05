from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())       
        products = Product.get_products_by_id(ids)
        print(products)
        
        data = {
            'products':products,         
        } 
        
        return render(request, 'cart.html', data)

    
    def post(self, request):
        
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity - 1
                else:
                    cart[product]  = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        
        return HttpResponseRedirect("cart")