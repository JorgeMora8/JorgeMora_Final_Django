# Generated by Django 4.1.5 on 2023-03-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrossfitApp', '0007_remove_competitors_image_competitors_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitors',
            name='user_linked',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
