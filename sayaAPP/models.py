from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()

# category models


class Category(models.Model):
    name = models.CharField(max_length=255, default='News')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(default="", null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.title

    class Meta:
        # changing the name of model in the admin interface
        verbose_name_plural = 'News & Events'

# comment


class CommentPost(models.Model):
    author = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'  # changing name to 'Comments'

    def __str__(self):
        return self.author

# like post model


class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"

# contac model


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# donation model
class DonationContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=4000)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
