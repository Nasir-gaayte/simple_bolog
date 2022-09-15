
from tkinter import Widget
from django import forms 
from .models import Post,Category



class PostForm (forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ( 'title', 'header_image' ,'title_tag','author','category','body')
    
        widgets= {
            'author':forms.TextInput({'class':'form-control', 'value':'','id':'user', 'type':'hidden'})
        }
    
    
    
class CategoryForm (forms.ModelForm):
    
     class Meta:
        model = Category
        fields = ('name',)   