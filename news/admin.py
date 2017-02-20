from django.contrib import admin
from news.models import Slider,How_it_works
# Register your models here.



class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ('show_image',)
    list_display = ('show_image','title','text','status','read_more')



admin.site.register(Slider,SliderAdmin)
admin.site.register(How_it_works)
