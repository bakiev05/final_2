from django.db import models
from apps.posts.models import Post


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name="recipes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    process = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class RecipeImage(models.Model):
    image_recipe = models.ImageField(
        upload_to='image_recipe',
        verbose_name='pictures',
        blank=True, null=True
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='recipe_image'
    )

    def __str__(self):
        return f"{self.recipe.title} -- {self.recipe.id}"
