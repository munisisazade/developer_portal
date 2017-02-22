from django.contrib import admin
from news.models import Slider,How_it_works,Author,ArticleCategory,ArticleTags,RelationTagArticle,RelationCategoryArticle,ArticleImages,Article,Mesagges,Contact_us,PrivacyPolicy
# Register your models here.



class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ('show_image',)
    list_display = ('show_image','title','text','status','read_more')
    icon = '<i class="material-icons admin-modelicon-build">picture_in_picture</i>'

class AuthorAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">recent_actors</i>'

class ArticleAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">note_add</i>'

class ArticleImagesAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">perm_media</i>'

class Contact_usAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">contacts</i>'

class ArticleTagsAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">loyalty</i>'

class ArticleCategoryAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">library_books</i>'

class MesaggesAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">message</i>'

class How_it_worksAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons admin-modelicon-build">work</i>'




admin.site.register(Slider,SliderAdmin)
admin.site.register(How_it_works,How_it_worksAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(ArticleCategory,ArticleCategoryAdmin)
admin.site.register(ArticleTags,ArticleTagsAdmin)
admin.site.register(RelationTagArticle,ArticleTagsAdmin)
admin.site.register(RelationCategoryArticle,ArticleCategoryAdmin)
admin.site.register(ArticleImages,ArticleImagesAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Mesagges,MesaggesAdmin)
admin.site.register(Contact_us,Contact_usAdmin)
admin.site.register(PrivacyPolicy)


