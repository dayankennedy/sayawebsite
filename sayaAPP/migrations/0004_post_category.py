# Generated by Django 4.1.7 on 2023-08-06 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayaAPP', '0003_remove_post_category_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sayaAPP.category'),
        ),
    ]
