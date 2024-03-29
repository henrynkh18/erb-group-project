from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.db.models import F

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            quantity=cart.get(str(product.id))           
            
            Product.objects.filter(pk=product.id).update(stock_on_hand = F('stock_on_hand') - quantity)
            
            order = Order(customer=Customer(id=customer),
                        product=product,
                        price=product.name.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)))
            order.save()
            
        request.session['cart'] = {}

        return redirect('cart')
