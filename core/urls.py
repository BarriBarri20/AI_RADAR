from django.urls import path
from core import views

urlpatterns = [
	path('', views.NewsItemsListView.as_view(), name='home'),
 
	path('scrape-history/', views.ScrapeRecordListView.as_view(), name='scrape-history')
]