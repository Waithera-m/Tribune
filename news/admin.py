from django.contrib import admin

from .models import Article,tags, MoringaMerch

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Article)
admin.site.register(tags)
admin.site.register(MoringaMerch)
# Register your models here.
