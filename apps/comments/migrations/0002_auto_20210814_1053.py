# Generated by Django 3.2.6 on 2021-08-14 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(verbose_name='reply_text'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_user', to=settings.AUTH_USER_MODEL),
        ),
    ]