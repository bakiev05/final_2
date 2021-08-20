from django.contrib import admin
from apps.posts.models import Post, PostImage, Like
from apps.categories.models import Category
from apps.comments.models import Reply, LikeReply
from apps.recipes.models import Recipe, RecipeImage
from apps.users.models import User

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(RecipeImage)
admin.site.register(Reply)
admin.site.register(LikeReply)
admin.site.register(Like)

