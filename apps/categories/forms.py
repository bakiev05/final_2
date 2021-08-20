from apps.categories.models import Category
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'parent': forms.Select(attrs={'class': "form-control"}),
        }


