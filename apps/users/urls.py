from django.urls import path
from apps.users import views

urlpatterns = [
    # path('sign_in/', views.UserCreateView.as_view(), name='user_create'),
    path('register/', views.register, name='register'),
]
