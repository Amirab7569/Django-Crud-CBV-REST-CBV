from django import forms
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','is_published',]
    
    
class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'