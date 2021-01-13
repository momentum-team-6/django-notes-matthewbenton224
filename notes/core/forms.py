from django import forms
from core.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, label="Search")
    
