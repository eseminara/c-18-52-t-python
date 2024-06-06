from django import forms
from .models import Forum, Message

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'description']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
