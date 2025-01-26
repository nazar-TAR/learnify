from django import forms

from discussions.models import Comment


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Your feedback about this course'}
        widgets = {'text':
                       forms.Textarea(attrs=
                                      {'placeholder': 'Write your experience about this course...',
                                       'cols': '55'})}