# Generated by Django 5.0.3 on 2024-07-20 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_payment_customer_remove_payment_tour'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
