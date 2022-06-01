from django import forms
from .models import Post, Category

choice = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choice:
    choice_list.append(item)

class   PostForm(forms.ModelForm):
    class Meta:
        model = Post    
        fields = ('title', 'author','category',  'body' , 'snippet', 'created_at')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            # there is java script for this
            'author' : forms.TextInput(attrs={'class' : 'form-control','value':'', 'id':'admin', 'type':'hidden'}),
            'category' : forms.Select(choices = choice_list , attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class' : 'form-control'}),
            'created_at' : forms.TextInput(attrs={'class' : 'form-control'}),
        }