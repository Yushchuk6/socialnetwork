from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='likes', blank=True)

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.post_date)
