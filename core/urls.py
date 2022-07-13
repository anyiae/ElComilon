from nturl2path import url2pathname
from django.urls import path
from .views import *

urlpatterns = [
    path ('', root),
    path('home',home, name="home"),
    path('productos',productos, name="productos"),
    path('locales',locales, name="locales"),
    path('delivery',delivery, name="delivery"),
    path('pago',pago, name="pago")
]