# Generated by Django 4.1.5 on 2023-03-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrossfitApp', '0004_competitors_competition_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitors',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='competitorImages'),
        ),
    ]
