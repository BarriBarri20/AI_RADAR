from django.contrib import admin
from .models import NewsItem, ScrapeHistory


@admin.register(NewsItem)
class NewsItemAdminView(admin.ModelAdmin):
    list_display = ('source', 'link', 'title','published_date')



@admin.register(ScrapeHistory)
class ScrapeHistoryAdminView(admin.ModelAdmin):
    list_display = ('timestamp','finished_time', 'finished')