# Generated by Django 4.0.5 on 2022-06-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0008_concert'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
