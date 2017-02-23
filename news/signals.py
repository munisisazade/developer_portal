from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from news.models import Slider,ArticleCategory
import os


@receiver(post_delete, sender=Slider, dispatch_uid="delete_slider")
def delete_slider(sender,**kwargs):
    slider = kwargs.get('instance')
    file = os.path.join(settings.BASE_DIR,settings.MEDIA_ROOT,slider.image.name)
    if os.path.isfile(file):
        os.remove(file)
        obj = ArticleCategory(title='Obyekt silindi')
        obj.save()
    else:
        obj = ArticleCategory(title='Obyekt silinmedi')
        obj.save()


