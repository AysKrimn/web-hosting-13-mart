# Generated by Django 4.2 on 2023-07-31 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0004_serverbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('description', models.TextField(max_length=150, verbose_name='Açıklama')),
                ('file', models.FileField(upload_to='Uplaods', verbose_name='İçerik Görsel')),
            ],
        ),
    ]
