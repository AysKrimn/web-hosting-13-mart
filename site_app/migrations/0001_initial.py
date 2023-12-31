# Generated by Django 4.2 on 2023-07-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servisler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.FileField(upload_to='Uploads', verbose_name='Banner')),
                ('product_title', models.CharField(max_length=50, verbose_name='Ürün Başlığı')),
                ('product_descriptipn', models.TextField(max_length=150, verbose_name='Ürün Açıklaması')),
            ],
        ),
    ]
