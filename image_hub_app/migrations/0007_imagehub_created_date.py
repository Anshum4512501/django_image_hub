# Generated by Django 3.0.8 on 2020-07-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_hub_app', '0006_auto_20200727_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagehub',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
