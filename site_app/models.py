from django.db import models

# Create your models here.


# site banner
class Banner(models.Model):
    
    product_image = models.FileField(("Banner"), upload_to="Uploads", max_length=100)
    product_title = models.CharField(("Ürün Başlığı"), max_length=50)
    product_description = models.TextField(("Ürün Açıklaması"), max_length=150)

    def __str__(self) -> str:
        return self.product_title
    

# services kısmı
class Servisler(models.Model):
    product_image = models.FileField(("Banner"), upload_to="Uploads", max_length=100)
    product_title = models.CharField(("Ürün Başlığı"), max_length=50)
    product_descriptipn = models.TextField(("Ürün Açıklaması"), max_length=150)

    
    def __str__(self) -> str:
        return self.product_title
    


# services category kısmı
class Kategoriler(models.Model):

    category = models.CharField(("Kategori"), max_length=50)

    def __str__(self) -> str:
        return self.category


# server image kısmı
class ServerBanner(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    description = models.TextField(("Açıklama"), max_length=150)
    file = models.FileField(("İçerik Görsel"), upload_to="Uplaods", max_length=100)

    def __str__(self) -> str:
        return self.title


class UrunOzellikleri(models.Model):
    ozellik = models.CharField(("Ürün Özelliği"), max_length=50)

    def __str__(self) -> str:
        return self.ozellik

# price kısmı
class Ozellikler(models.Model):

    price = models.IntegerField(default=50)
    type = models.ForeignKey(Kategoriler, verbose_name=("Tür"), on_delete=models.CASCADE)
    options = models.ManyToManyField(UrunOzellikleri, verbose_name=("Özellikler"))


    def __str__(self) -> str:
        return self.type.category



class AboutUs(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    description = models.TextField(("Açıklama"), max_length=150)
    file = models.FileField(("İçerik Görsel"), upload_to="Uplaods", max_length=100)


# navdaki linkler
class HeaderParts(models.Model):

    name = models.CharField(("İsim"), max_length=50)
    to = models.CharField(("Gideceği link"), max_length=50)

    def __str__(self) -> str:
        return self.name