from django.forms import ModelForm, Textarea
from . import models


class PostForm(ModelForm):
    class Meta:
        model = models.Posts
        fields = ('title', 'content',)
        widgets = {
            'content': Textarea(attrs={'cols': 100, 'rows': 2})
        }
