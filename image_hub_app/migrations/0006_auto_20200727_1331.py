# Generated by Django 3.0.8 on 2020-07-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_hub_app', '0005_auto_20200727_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagehub',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
