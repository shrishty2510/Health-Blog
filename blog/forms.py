from attr import field
from matplotlib import widgets
from . models import Post
from django import forms


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category','title','image','content','summary']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','cols': 10, 'rows': 6}),
            'category':forms.Select(attrs={'class':'form-control',}),
            'summary':forms.Textarea(attrs={'class':'form-control','cols': 10, 'rows': 3}),
        }