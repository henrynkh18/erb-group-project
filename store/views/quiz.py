from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q

from store.forms import *
from store.modules import *
from store.models.customer import Customer
from store.models.supercategory import SuperCategory
from store.models.category import Category
from store.models.producttype import ProductType
from store.models.product import Product
from store.models.sport import Sport

def stylequiz(request):      
    return render(request, 'style_quiz.html')


def stylequiz_question(request, pk):
    customer_id = request.session.get('customer')  #id
    if not customer_id:
        return redirect("login")
    customer = get_object_or_404(Customer, pk=customer_id)
    
    data = {'pk': pk}
    
    
    if request.method == "GET":
        
        if pk == 1:
            form1 = GenderForm(instance=customer)     
            if form1.is_valid():
                gender = form1.cleaned_data['gender']

            data['form1'] = form1
                
        elif pk == 2:
            form2 = HeightWeightForm(instance=customer)
            if form2.is_valid():
                height = form2.cleaned_data['height']
                weight = form2.cleaned_data['weight']
                
            data['form2'] = form2
        
        elif pk == 3:           
            form3 = ColorForm(instance=customer)
            if form3.is_valid():
                color = form3.cleaned_data['color']
                
            data['form3'] = form3
        
        elif pk == 4:
            sports = Sport.get_all_sports()
            data['sports'] = sports
        
        elif pk == 5:
            sport = request.session['sport']  
            #print(sport)
                     
            if customer.gender.id == 1: # male
                categorys = Category.objects.filter(Q(super_category__id=2) | Q(super_category__id=3))
            elif customer.gender.id == 2: # female
                categorys = Category.objects.filter(super_category__id=1)
            data['categorys'] = categorys
        
        elif pk == 6:
            catoption = request.session['catoption']
        

    
    elif request.method == "POST":
        
        if pk == 1:
            form1 = GenderForm(request.POST, instance=customer)
            if form1.is_valid():
                gender = form1.cleaned_data['gender']
                
                customer = form1.save(commit=False)
                customer.gender = gender
                customer.save()
                return redirect('stylequiz_question', pk=pk+1)
            
        elif pk == 2:
            form2 = HeightWeightForm(request.POST, instance=customer)
            if form2.is_valid():
                height = form2.cleaned_data['height']
                weight = form2.cleaned_data['weight']               
                bmi = bmi_cal(height, weight)                           

                customer = form2.save(commit=False)
                customer.height = height
                customer.weight = weight               
                customer.bmi = bmi
                customer.save()
                
                return redirect('stylequiz_question', pk=pk+1)
        
        elif pk == 3:
            form3 = ColorForm(request.POST, instance=customer)
            if form3.is_valid():
                color = form3.cleaned_data['color']                 

                customer = form3.save(commit=False)
                customer.color = color
                customer.save()
                
                return redirect('stylequiz_question', pk=pk+1)
            
        elif pk == 4:
            
            sport_id = request.POST.get('sportoption')
            request.session['sport'] = sport_id
            # if sport_id:
            #     sport = Sport.objects.filter(pk=sport_id)
            # else:
            #     sport = Sport.get_all_sports()

            return redirect('stylequiz_question', pk=pk+1)      
        
        elif pk == 5:
            
            cat_id = request.POST.get('catoption')
            request.session['catoption'] = cat_id
            
            return redirect('stylequiz_question', pk=pk+1)    

    return render(request, 'style_quiz.html', data)