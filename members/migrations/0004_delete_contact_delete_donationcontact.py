# Generated by Django 4.1.7 on 2023-07-05 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_phone_number_contact_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='DonationContact',
        ),
    ]
