from django.forms import ModelForm, Textarea, TextInput, RadioSelect,ClearableFileInput
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review        
        fields = [
            'title', 'content', 'movie_name', 'grade', 'image1', 'image2', 'image3',
        ]
        widgets = { 
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 100%; border-style:solid;',
                
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'style': 'max-width: 100%; border-style:solid;',
                
            }),
            'movie_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 100%; border-style:solid;',
            }),
           'grade' : RadioSelect,
        }
