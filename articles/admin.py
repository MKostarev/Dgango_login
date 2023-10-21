from django.contrib import admin
from articles.models import Article, Category, Likes, Galery
from django_summernote.admin import SummernoteModelAdmin

class ArticleTextEditAdmin(SummernoteModelAdmin):
    pass

# Register your models here.
class GaleryInline(admin.TabularInline):
    fk_name = 'article_id'
    model = Galery

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    inlines = [GaleryInline]
    list_display = ['user', 'category', 'title']
    search_fields = ['title', 'article']
    list_filter = ['user', 'category']
    summernote_fields = '__all__'

admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Galery)