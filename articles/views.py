from django.shortcuts import render

from articles.models import Article, Likes


# Create your views here.


def article_views(request):
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles': articles})


def article_detail_views(request):
    id = 1
    article = Article.objects.get(id=id)
    likes = Likes.objects.filter(article_id=id)
    return render(request, 'article_detail.html', {'article': article, 'likes': likes})


