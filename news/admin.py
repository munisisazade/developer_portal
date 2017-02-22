from django.contrib import admin
from news.models import Slider,How_it_works,Author,ArticleCategory,ArticleTags,RelationTagArticle,RelationCategoryArticle,ArticleImages,Article,Mesagges,Contact_us,PrivacyPolicy
# Register your models here.



class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ('show_image',)
    list_display = ('show_image','title','text','status','read_more')
    icon = '<i class="material-icons admin-modelicon-build">input</i>'



admin.site.register(Slider,SliderAdmin)
admin.site.register(How_it_works)
admin.site.register(Author)
admin.site.register(ArticleCategory)
admin.site.register(ArticleTags)
admin.site.register(RelationTagArticle)
admin.site.register(RelationCategoryArticle)
admin.site.register(ArticleImages)
admin.site.register(Article)
admin.site.register(Mesagges)
admin.site.register(Contact_us)
admin.site.register(PrivacyPolicy)


