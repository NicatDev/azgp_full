# Generated by Django 4.2.5 on 2023-11-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_full_name_message_name_remove_message_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='about',
            name='mainimage',
        ),
        migrations.AddField(
            model_name='about',
            name='description_az',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='description_en',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='about',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='about',
            name='image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='about',
            name='mission',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='projects',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_az',
            field=models.CharField(max_length=440, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_en',
            field=models.CharField(max_length=440, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='vision',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description2_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description2_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='minititle_az',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='minititle_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='title_az',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='title_en',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='field',
            name='name_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='field',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='description_az',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='description_en',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_az',
            field=models.CharField(max_length=440, null=True),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_en',
            field=models.CharField(max_length=440, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='description2_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='description2_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='minititle_az',
            field=models.CharField(max_length=330, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='minititle_en',
            field=models.CharField(max_length=330, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='strong_description_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='strong_description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='title_az',
            field=models.CharField(max_length=340, null=True),
        ),
        migrations.AddField(
            model_name='portfolia',
            name='title_en',
            field=models.CharField(max_length=340, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description2_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description2_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='minititle_az',
            field=models.CharField(max_length=330, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='minititle_en',
            field=models.CharField(max_length=330, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='title_az',
            field=models.CharField(max_length=340, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='title_en',
            field=models.CharField(max_length=340, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=440),
        ),
    ]
