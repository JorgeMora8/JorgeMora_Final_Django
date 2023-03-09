# Generated by Django 4.1.5 on 2023-03-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrossfitApp', '0006_alter_competitors_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitors',
            name='image',
        ),
        migrations.AddField(
            model_name='competitors',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
