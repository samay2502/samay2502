from django.shortcuts import render,get_object_or_404
from acr.models import raw
# Create your views here.

def product(request):
    a = raw.objects.all()
    return render(request,'product.html',{ 'asap' : a })

def productview(request,abc):
    obj=get_object_or_404(raw,pk=abc)
    return render(request,'product_view.html',{'obj':obj})