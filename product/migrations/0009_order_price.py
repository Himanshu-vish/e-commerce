# Generated by Django 4.2.1 on 2023-08-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_order_address_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]