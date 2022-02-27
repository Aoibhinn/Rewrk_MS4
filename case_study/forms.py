"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form to enable an authenticated
    user to input a comment into commentform
    """
    class Meta:
        """
        A class to enable user to input comment
        """
        model = Comment
        fields = ('body',)
