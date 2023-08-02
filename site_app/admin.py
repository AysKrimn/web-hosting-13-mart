from django.contrib import admin

# servis modelini çagır
from .models import *


# admin syf kayit et
admin.site.register(Servisler)
admin.site.register(Ozellikler)
admin.site.register(Kategoriler)
admin.site.register(UrunOzellikleri)
admin.site.register(ServerBanner)
admin.site.register(AboutUs)
admin.site.register(HeaderParts)
admin.site.register(Banner)
