from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo']
        labels = {
            'title': '제목',
            'content': '내용',
            'photo': '사진',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'content': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }
