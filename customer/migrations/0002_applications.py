# Generated by Django 5.0.3 on 2024-04-04 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_rename_agency_addtours_agency'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('mobile', models.TextField(max_length=20, null=True)),
                ('address', models.TextField(max_length=400, null=True)),
                ('pincode', models.BigIntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.addtours')),
            ],
        ),
    ]
