# Generated by Django 3.1 on 2021-06-07 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
    ]
