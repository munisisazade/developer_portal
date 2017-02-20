from django.db import models
from datetime import datetime

# Create your models here.

def image_path(instance,filename):
    return "slider/%s_%s" % (datetime.today().strftime("%d_%m_%Y_%H_%M") ,filename.replace(" ","_"))

icon = (
    (1,'Bina'),
    (2,'Adam'),
    (3,'Gunes'),
)


"""
    This is for slider
"""
class Slider(models.Model):
    image = models.ImageField(upload_to=image_path)
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=255,null=True,blank=True)
    text = models.CharField(max_length=255,null=True,blank=True)
    read_more = models.BooleanField(default=False)

    def __str__(self):
        return self.image.name

    def show_image(self):
        return "<image src='%s' alt='%s' style='width: 190px;height: auto;'>" % ('/media/'+self.image.name,self.image.name)

    show_image.short_description = "Hal-hazırdakı slayder şəkli"
    show_image.allow_tags = True



class How_it_works(models.Model):
    icons = models.IntegerField(choices=icon)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255,null=True,blank=True)
    text = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
