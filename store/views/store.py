from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.db.models import Q
from django.contrib import messages

from store.models.producttype import ProductType
from store.models.product import Product
from store.models.category import Category
from store.models.supercategory import SuperCategory
from store.models.color import Color
from store.models.sport import Sport

# Create your views here.

# products page
def store(request): 
    return redirect("store_undercat", cat_pk=0)

# products page under category
def store_undercat(request, cat_pk):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {} 
    
    data = {}
    
    if cat_pk != 0:
        cat_pk = Category.objects.get(id=cat_pk)
        data['cat_pk'] = cat_pk.id
    
    products = ProductType.get_all_products_by_categoryid(cat_pk)
    super_categories = SuperCategory.objects.all()   
    categories = Category.get_all_categories()
    colors = Color.get_all_colors() 
    sports = Sport.get_all_sports()
    # colorID = request.GET.get('color')
    # sportID = request.GET.get('sport')

    data['products'] = products
    data['super_categories'] = super_categories
    data['categories'] = categories
    data['colors'] = colors
    data['sports'] = sports
    
    sportFlag = []
    for sport in sports:
        if request.POST.get(f'sport_{sport.id}'):
            sportFlag.append(True)
        else:
            sportFlag.append(False)           
    data['sportFlag'] = sportFlag
    
    colorFlag = []
    for color in colors:
        if request.POST.get(f'color_{color.id}'):
            colorFlag.append(True)
        else:
            colorFlag.append(False)           
    data['colorFlag'] = colorFlag
    
    data['minPrice'] = 0
    data['maxPrice'] = 1500
       
    
    if request.method == 'POST':
        
        # filter by sport
        spo = {} 
        spo_products = ProductType.objects.none()
        sportFlag = []
        for sport in sports:
            sportPOST = request.POST.get(f'sport_{sport.id}')
            #print(sportPOST)
            if sportPOST:
                spo[sport.id] = ProductType.get_all_products_by_sportid(int(sportPOST))
                spo_products |= spo[sport.id]
                sportFlag.append(True)
            else:
                sportFlag.append(False)
            #print("spo:", spo_products)
        data['sportFlag'] = sportFlag
        
        # filter by color
        col = {}
        col_products = ProductType.objects.none()
        colorFlag = []
        for color in colors:
            colorPOST = request.POST.get(f'color_{color.id}')
            #print(colorPOST)
            if colorPOST:
                col[color.id] = ProductType.get_all_products_by_colorid(int(colorPOST))
                col_products |= col[color.id]
                colorFlag.append(True)
            else:
                colorFlag.append(False)
        data['colorFlag'] = colorFlag
            #print("col:", col_products)
        
        if any(sportFlag) and any(colorFlag):
            tmp = col_products.intersection(spo_products)
            products = products.intersection(tmp)
            
        elif any(sportFlag) and not any(colorFlag):
            products = products.intersection(spo_products)
            
        elif any(colorFlag) and not any(sportFlag):
            products = products.intersection(col_products)
            
        else:
            products = ProductType.get_all_products_by_categoryid(cat_pk)
        
        # filter by price range    
        minPrice = request.POST.get('min')
        maxPrice = request.POST.get('max')
        data['minPrice'] = minPrice
        data['maxPrice'] = maxPrice

        pri = ProductType.objects.filter(price__range=(minPrice, maxPrice))    
        products = pri.intersection(products)
        data['products'] = products
    
    elif request.method == 'GET':
        
        # keyword search
        keyword = request.GET.get('search')   
        if keyword:
            search_products = ProductType.objects.filter(
                Q(name__icontains=keyword) 
                # | Q(description__icontains=keyword)
                )
            data['keyword'] = keyword
            data['products'] = search_products
    
            messages.info(request, f'The search result of "{keyword}":', extra_tags='search')

    print('You are: ', request.session.get('email'))    
    return render(request, 'products.html', data)
