from django.contrib import admin
from django.urls import path
from .middlewares.auth import auth_middleware

from .views.index import home
from .views.store import store, store_undercat
from .views.product import ProductDetail
from .views.quiz import stylequiz, stylequiz_question
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView


urlpatterns = [
    path('', home, name='home'),    
    path('index/', home, name='home'),
    path('products/', store, name='store'),
    path('products/<int:cat_pk>/', store_undercat, name='store_undercat'),
    path('product_detail/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('stylequiz/', auth_middleware(stylequiz), name='stylequiz'),
    path('stylequiz/<int:pk>/', stylequiz_question, name='stylequiz_question'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
