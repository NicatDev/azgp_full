# Generated by Django 4.2.6 on 2023-11-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_portfolia_client_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
