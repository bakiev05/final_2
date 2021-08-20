from django.db import models
from apps.users.models import User
from apps.posts.models import Post


class Reply(models.Model):
    text = models.TextField(
        verbose_name='reply_text'
    )
    user = models.ForeignKey(
        User,
        related_name='reply_user',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='reply_post',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.post.id} -- {self.user.id}"


class LikeReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='likes_comment')

    def __str__(self):
        return f"{self.user.username} -- {self.reply.id}"
