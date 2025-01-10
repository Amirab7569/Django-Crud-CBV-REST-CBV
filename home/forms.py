from django import forms
from .models import Post

class CreatePost(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    author = forms.CharField()
    is_published = forms.BooleanField()
    created = forms.DateTimeField()
    
class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'