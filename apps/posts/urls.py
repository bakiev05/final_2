from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.posts import views

urlpatterns = [
    path('', views.data, name='data'),
    path('blog/', views.blog_post, name='blog_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)