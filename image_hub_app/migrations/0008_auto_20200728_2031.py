# Generated by Django 3.0.8 on 2020-07-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_hub_app', '0007_imagehub_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagehub',
            name='number_of_views',
            field=models.IntegerField(default=0, verbose_name='view'),
        ),
    ]