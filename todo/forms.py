from django import forms
from . models import ToDoItems
class ToDoItemForm(forms.ModelForm):
    class Meta:
        model=ToDoItems
        fields=['title','completed']