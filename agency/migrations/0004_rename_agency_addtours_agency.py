# Generated by Django 5.0.3 on 2024-03-28 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_alter_addtours_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtours',
            old_name='agency',
            new_name='Agency',
        ),
    ]