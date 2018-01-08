from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    
    file = models.FileField()
    caption = models.TextField()
    location = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def count_likes(self):
        return self.like_set.all().count()

    def count_comments(self):
        return self.comment_set.all().count()

    def __str__(self):
        return f'{self.caption} - {self.location}'

    class Meta:
        ordering = ("-created_at",)


class Comment(models.Model):

    message = models.TextField()
    directed_to = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.message} - {self.directed_to.location}'

    class Meta:
        ordering = ("-id",)


class Like(models.Model):

    directed_to = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.created_by}'

    class Meta:
        ordering = ("-id",)
