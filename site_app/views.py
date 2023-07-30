from django.shortcuts import render

# veritabanı modelini çağır
from .models import *


# Create your views here.
def anasayfa(request):
    context = {}

    # veritabanındaki tüm servisleri getir
    products = Servisler.objects.all()

    context['urunler'] = products

    return render(request, "index.html", context)




def hakkimizda(request):
    print("şuan oldugun yer", request.path)
    return render(request, 'about.html')



def hizmetlerimiz(request):

    return render(request, 'service.html')



def ucretlendirme(request):

    return render(request, 'price.html')



def bizeUlas(request):

    return render(request, 'contact.html')