from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=280)
    date_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return f'{self.autor.username}: {self.content[:30]}'

    def total_likes(self):
        return self.likes.count()
    