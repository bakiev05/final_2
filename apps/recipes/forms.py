from apps.recipes.models import Recipe, RecipeImage
from django import forms 


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image_recipe']
        widgets = {
            'image_recipe': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }