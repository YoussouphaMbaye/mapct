# Generated by Django 3.2.10 on 2022-05-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220503_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='repcommentaire',
            name='reponse',
            field=models.TextField(blank=True, max_length=355, null=True),
        ),
    ]
