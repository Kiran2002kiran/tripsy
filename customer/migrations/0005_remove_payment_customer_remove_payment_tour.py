# Generated by Django 5.0.3 on 2024-04-12 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='tour',
        ),
    ]