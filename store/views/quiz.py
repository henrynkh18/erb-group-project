from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib import messages

from store.models.category import Category
from store.models.supercategory import SuperCategory
from store.models.producttype import ProductType
from store.models.product import Product

class StyleQuiz(View):
    
    def get(self, request):
        
        return render(request, 'style_quiz.html')


    def post(self, request):
        
        return render(request, 'style_quiz.html')