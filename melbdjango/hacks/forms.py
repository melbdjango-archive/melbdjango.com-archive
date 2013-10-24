
from django import forms

from . import models

class IdeaForm(forms.ModelForm):

    class Meta:
        model = models.Idea
        fields = (
            'title',
            'description',
        )

class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = (
            'comment',
        )
