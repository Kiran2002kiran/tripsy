# Generated by Django 5.0.3 on 2024-03-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencyname', models.TextField(max_length=100, null=True)),
                ('branches', models.TextField(max_length=100, null=True)),
                ('ownername', models.TextField(max_length=100, null=True)),
                ('userid', models.TextField(max_length=100, null=True)),
                ('license', models.TextField(max_length=100, null=True)),
                ('password', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
