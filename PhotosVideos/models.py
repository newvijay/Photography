from django.db import models

# Create your models here.
class Photos(models.Model):
    img_name = models.CharField(max_length=300)
    img_src = models.ImageField(upload_to='photos/')

    # def __str__(self):
    #     return self.img_name + ": " + str(self.img_src)

class Videos(models.Model):
    video_name = models.CharField(max_length=300)
    video_url = models.FileField(upload_to='videos/',blank=True,null=True)
