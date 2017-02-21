from django.db import models
from datetime import datetime
from slugify import slugify
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


class ArticleCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(ArticleCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title.lower().replace('ə', 'e').replace(' ', '-'))
        super(ArticleCategory, self).save(*args, **kwargs)



class Mesagges(models.Model):
    full_name = models.CharField(max_length=100,verbose_name="Adi",null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    message = models.TextField(verbose_name="Mesaj",null=True,blank=True)

    def __str__(self):
        return str(self.full_name if self.full_name else "adsiz")




class Contact_us(models.Model):
    facebook = models.CharField(max_length=255,null=True,blank=True)
    twitter = models.CharField(max_length=255,null=True,blank=True)
    googleplus = models.CharField(max_length=255,null=True,blank=True)
    place = models.CharField(max_length=255,null=True,blank=True)
    phone_1 = models.CharField(max_length=20,null=True,blank=True)
    phone_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.email if self.email else "adsiz")