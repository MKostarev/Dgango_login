from django.conf import settings
from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #tag =
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    article = models.TextField()
    cower_image = models.ImageField(upload_to='cower_image/', blank=True, null=True)


class Galery(models.Model):
    image = models.ImageField(upload_to='galery/', blank=True, null=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')


class Likes(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('article_id', 'user_id')

