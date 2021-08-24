from django.db import models
from apps.users.models import User
from apps.posts.models import Post

class Saved(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name='saves', on_delete=models.SET_NULL)
    posts = models.ManyToManyField(Post, blank=True, related_name='saves')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.id}"

    
