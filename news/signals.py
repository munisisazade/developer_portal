from django.conf import settings
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from news.models import Slider,Author
import os


@receiver(post_delete, sender=Slider, dispatch_uid="delete_slider")
def delete_slider(sender,**kwargs):
    slider = kwargs.get('instance')
    file = os.path.join(settings.BASE_DIR,settings.MEDIA_ROOT,slider.image.name)
    if os.path.isfile(file):
        os.remove(file)
    else:
        print('There is no file in this directory')



@receiver(post_save, sender=User, dispatch_uid="create_author")
def create_author(sender,**kwargs):
    user = kwargs.get('instance')
    try:
        Author.objects.get(user=user)
    except:
        obj = Author(user=user)
        obj.save()