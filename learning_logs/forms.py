from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        help_texts = {'text': 'Please enter text above'}

        # text area will be 80 columns wide
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
