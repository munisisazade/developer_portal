from django.db import models
from datetime import datetime
from slugify import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

def image_path(instance,filename):
    return "slider/%s_%s" % (datetime.today().strftime("%d_%m_%Y_%H_%M") ,filename.replace(" ","_"))

def news_path(instance,filename):
    return "news/%s_%s" % (datetime.today().strftime("%d_%m_%Y_%H_%M") ,filename.replace(" ","_"))




icon = (
    (1,'Bina'),
    (2,'Adam'),
    (3,'Gunes'),
)



class Author(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.username

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



class ArticleTags(ArticleCategory):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'



class RelationTagArticle(models.Model):
    article_obj = models.ForeignKey('Article')
    tag_obj = models.ForeignKey('ArticleTags')

    def __str__(self):
        return "%s %s" % (self.article_obj.title,self.tag_obj.title)


class RelationCategoryArticle(models.Model):
    article_obj = models.ForeignKey('Article')
    category_obj = models.ForeignKey('ArticleCategory')

    def __str__(self):
        return "%s %s" % (self.article_obj.title, self.category_obj.title)



class ArticleImages(models.Model):
    article_obj = models.ForeignKey('Article')
    image = models.ImageField(upload_to=news_path)

    def __str__(self):
        return str(self.image.name)


class Article(models.Model):
    title = models.CharField(max_length=255,verbose_name="Basligi")
    content = RichTextField(config_name='awesome_ckeditor',verbose_name="Kontenti")
    author = models.ForeignKey('Author')
    status = models.BooleanField(default=True,verbose_name="Xeberin statusu")
    home_page_status = models.BooleanField(default=True,verbose_name="Ana səhifədə görünsün?")
    date = models.DateTimeField(default=timezone.now)

    def get_images(self):
        try:
            item = ArticleImages.objects.filter(article_obj_id=self.id)
            return item
        except:
            return False


    def __str__(self):
        return str(self.title)


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



class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return str(self.title)



class Haqqimizda(models.Model):
    html = models.TextField()

    def __str__(self):
        return self.html[:10]
