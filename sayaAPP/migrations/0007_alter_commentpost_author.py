# Generated by Django 4.1.7 on 2023-07-19 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sayaAPP', '0006_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='author',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
