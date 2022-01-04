from django.urls import path
from acr.views import product, productview

urlpatterns = [
    path('v/',product),
    path('productview/<int:abc>/',productview,name='productview')
]