from django.urls import path
from news.views import scrape, news_list, news
urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news, name="home"),
  path('history/', news_list, name="history"),
]