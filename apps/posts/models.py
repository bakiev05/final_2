from django.db import models
from apps.users.models import User
from apps.categories.models import Category


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    category = models.ForeignKey(
        Category,
        related_name='post_category',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.title}"


class PostImage(models.Model):
    image = models.ImageField(
        upload_to='post_image',
        verbose_name='Картинки',
        blank=True, null=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_image'
    )

    def __str__(self):
        return f"{self.post.title} -- {self.post.id}"
    



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')

    def __str__(self):
        return f"{self.user.username} -- {self.post.title}"

