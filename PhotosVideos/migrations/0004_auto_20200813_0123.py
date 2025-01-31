# Generated by Django 3.1 on 2020-08-13 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotosVideos', '0003_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='img_src',
            field=models.ImageField(upload_to='static/photos/'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='static/videos'),
        ),
    ]
