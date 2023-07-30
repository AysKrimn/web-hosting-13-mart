from django.db import models

# Create your models here.
class Servisler(models.Model):
    product_image = models.FileField(("Banner"), upload_to="Uploads", max_length=100)
    product_title = models.CharField(("Ürün Başlığı"), max_length=50)
    product_descriptipn = models.TextField(("Ürün Açıklaması"), max_length=150)

    
    def __str__(self) -> str:
        return self.product_title
    


class Kategoriler(models.Model):

    category = models.CharField(("Kategori"), max_length=50)

    def __str__(self) -> str:
        return self.category




class Ozellikler(models.Model):

    price = models.IntegerField(default=50)
    type = models.ForeignKey(Kategoriler, verbose_name=("Tür"), on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.type
