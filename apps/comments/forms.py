from apps.comments.models import Reply
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'






