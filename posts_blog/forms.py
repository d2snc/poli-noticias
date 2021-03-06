from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'conteudo')
        
class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('autor', 'texto')
    