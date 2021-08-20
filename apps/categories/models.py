from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



class Category(MPTTModel):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True, blank=True
    )
  


    def __str__(self):
        return f"{self.title}"
