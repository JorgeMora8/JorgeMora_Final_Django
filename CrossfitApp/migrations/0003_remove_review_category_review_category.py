# Generated by Django 4.1.7 on 2023-03-01 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CrossfitApp', '0002_review_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='Category',
        ),
        migrations.AddField(
            model_name='review',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CrossfitApp.blog'),
        ),
    ]