# Generated by Django 3.2.10 on 2022-04-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lieu',
            name='latitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lieu',
            name='longitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
