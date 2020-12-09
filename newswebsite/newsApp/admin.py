from django.contrib import admin
from .models import catagory_of_news, News_Comment, add_news_new, like
# Register your models here.


class add_news_display(admin.ModelAdmin):
    list_display = ['name_news', 'catagory']


admin.site.register(catagory_of_news)
admin.site.register(News_Comment)
admin.site.register(add_news_new, add_news_display)
admin.site.register(like)
