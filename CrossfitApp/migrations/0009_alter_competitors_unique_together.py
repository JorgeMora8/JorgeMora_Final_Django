# Generated by Django 4.1.7 on 2023-03-09 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrossfitApp', '0008_competitors_user_linked'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='competitors',
            unique_together={('competition_in', 'user_linked')},
        ),
    ]