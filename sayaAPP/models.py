from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class CommentPost(models.Model):
    author = models.ForeignKey(models.ForeignKey)
    comment_text = models.TextField(max_length=255, blank=True)
    date_crated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment_text
    

class LikePost(models.Model):
    pass
