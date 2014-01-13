from django.forms import ModelForm, Textarea

from blog.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment        
        widgets = {            
            'body' : Textarea(attrs={'cols': 80, 'rows' : 2}),
        }
        exclude = ["post"]