from django.shortcuts import render, redirect

# veritabanı modelini çağır
from .models import *

from django.contrib import messages

import requests

# def apiReq():

#         url = "https://fake-valid-cc-data-generator.p.rapidapi.com/request/"

#         querystring = {"visa_type":"visa"}

#         headers = {
#             "X-RapidAPI-Key": "7fe38db4a7msh066836ccb5bdefap1ea3c5jsn08a4eb57d9f1",
#             "X-RapidAPI-Host": "fake-valid-cc-data-generator.p.rapidapi.com"
#         }

#         response = requests.get(url, headers=headers, params=querystring)

#         print("apiden gelen data:", response.json())


# apiReq()

def anasayfa(request):
    context = {}
    # veritabanındaki tüm servisleri getir
    products = Servisler.objects.all()
    pricing = Ozellikler.objects.all()
    serverData = ServerBanner.objects.all()
    aboutData = AboutUs.objects.all()
    # bannerdeki tüm verileri çek
    bannerData = Banner.objects.all()

    context['urunler'] = products
    context['ucretlendirme'] = pricing
    context['serverData'] = serverData
    context['aboutData'] = aboutData
    context['bannerData'] = bannerData
   
    return render(request, "index.html", context)




def hakkimizda(request):
    print("şuan oldugun yer", request.path)
    return render(request, 'about.html')



def hizmetlerimiz(request):
    context = {}
    services = Servisler.objects.all()
    context['services'] = services

    return render(request, 'service.html', context)



def ucretlendirme(request):
    context = {}
    navLinks = HeaderParts.objects.all()
    context['navLinks'] = navLinks

    return render(request, 'price.html', context)



def bizeUlas(request):

    return render(request, 'contact.html')







def satinAlim(request, servisId):
    
    # apidan gelen örnek veri
    data = [{

         "firstname": "Michael",
         "lastname": "Gallegos",
         "cc": "4487489441398491",
         "valid_date": "10/31",
         "cvc": "248",
         "cash": 50
    }]

    if request.method == 'POST':
        
        ad = request.POST.get('adi')
        soyad = request.POST.get('soyadi')
        cardNo = request.POST.get('cardNo')
        ay = request.POST.get('ay')
        gun = request.POST.get('gun')
        formatAy = ay + "/" + gun
        cvc = request.POST.get('cvc')


        if ad.strip() and soyad.strip() and cardNo.strip() and ay and gun and cvc:
            
            # satın alınmak istenen servisi veritabanından çek
            product = Ozellikler.objects.filter(id=servisId).first()

            for cardOwner in data:
                
              if cardOwner['firstname'] == ad and cardOwner['lastname'] == soyad:
                  
                  if cardOwner['cc'] == cardNo: 
                      
                      if cardOwner['valid_date'] == formatAy:
                          
                          if cardOwner['cvc'] == cvc:

                            if cardOwner['cash'] >= product.price:
                                #   başarılı
                               print("ürün satın alındı")
                               messages.success(request, 'Başarılı bir şekilde satın alındı')
                               return redirect('anasayfa')
                            
                            else:
                               messages.error(request, 'Yeterli Bakiyeniz Yok')
                      else:
                        # geçerlilik süresi uyusmuyor
                        messages.error(request, 'Geçerlilik süresi uyuşmuyor')
                  else:
                    # card numarası hatalı
                    messages.error(request, 'Kart numaranız hatalı')
              else:
                #   ad veya soyad uyusmuyor
                messages.error(request, 'Kart üzerindeki ad veya soyad hatalı')
            

               # potensiyel bir hatada
              return redirect('anasayfa')
        else:
           
           messages.error(request, 'Lütfen tüm alanları doldurunuz..')
           return redirect('anasayfa')

    else:
        return redirect('anasayfa')