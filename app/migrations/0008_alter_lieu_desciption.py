# Generated by Django 3.2.10 on 2022-05-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_lieu_desciption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lieu',
            name='desciption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
