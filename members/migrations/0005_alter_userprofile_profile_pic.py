# Generated by Django 4.1.7 on 2023-07-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_delete_contact_delete_donationcontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='/profile_pics/default_profile.PNG', upload_to='profile_pics'),
        ),
    ]