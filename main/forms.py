from .models import Entry,Comment,Gallery,UserProfile
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput,Textarea,FileInput


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar','description']
        widgets = {
            'avatar': FileInput(attrs={'class':'form-control-file'}),
            'description':Textarea(attrs={'class':'form-control'}),
        }


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['keyword','content']
        widgets = {
            'keyword': TextInput(attrs={'class':'form-control','placeholder':'Keyword (optional)'}),
            'content': Textarea(attrs={'class':'form-control','placeholder':''}),
        }
        labels = {
            'keyword': '',
            'content':'',
        }
       

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        widgets = {
            'content':Textarea(attrs={'class':'form-control'}),
        }
        labels = {'content':''}
           

class FeedbackForm(forms.Form):
    CATGEORY_CHOICES = [ ('Feature Suggestion','Feature suggestion'),
                         ('Bug Report','Bug Report'),
                         ('Moderation Feedback','Moderation Feedback'),
                       ]
    category = forms.ChoiceField(choices=CATGEORY_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['photo']
        widgets = {
            'photo':FileInput(attrs={'class':'form-control-file'})
        }
        labels = {'photo':''}