from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.category import Category
from store.models.supercategory import SuperCategory

def home(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    
    super_categories = SuperCategory.objects.all()
 
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')          
    
    data = {}  
    data['super_categories'] = super_categories
    data['categories'] = categories
    
    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)
