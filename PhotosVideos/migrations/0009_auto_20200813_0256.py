# Generated by Django 3.1 on 2020-08-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotosVideos', '0008_auto_20200813_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='img_src',
            field=models.ImageField(upload_to='media/photos/'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video_url',
            field=models.FileField(blank=True, null=True, upload_to='media/videos/'),
        ),
    ]
