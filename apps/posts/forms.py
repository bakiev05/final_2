from apps.posts.models import Post,PostImage
from apps.categories.models import Category
from django import forms



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'





class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }