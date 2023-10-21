from django.urls import path
from articles.views import article_views, article_detail_views

#main page / article

urlpatterns = [
    path('', article_views, name='article'),
    path('article_detail/', article_detail_views, name='article_detail')
]