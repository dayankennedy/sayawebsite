# Generated by Django 4.1.7 on 2023-05-13 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_contact_donationcontact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
