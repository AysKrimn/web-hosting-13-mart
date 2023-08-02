# Generated by Django 4.2 on 2023-07-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_kategoriler_ozellikler'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrunOzellikleri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ozellik', models.CharField(max_length=50, verbose_name='Ürün Özelliği')),
            ],
        ),
        migrations.AddField(
            model_name='ozellikler',
            name='options',
            field=models.ManyToManyField(to='site_app.urunozellikleri', verbose_name='Özellikler'),
        ),
    ]