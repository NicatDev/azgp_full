# Generated by Django 4.2.6 on 2023-11-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_portfolia_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolia',
            name='client_country',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='strong_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='value',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
