# Generated by Django 4.1.7 on 2023-08-02 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayaAPP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationcontact',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
