# Generated by Django 4.2 on 2023-07-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0005_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('to', models.CharField(max_length=50, verbose_name='Gideceği link')),
            ],
        ),
    ]
