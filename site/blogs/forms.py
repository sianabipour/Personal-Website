from django import forms
from .models import Blog

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['header', 'title','author','date','text','instagram','twitter','slug']
