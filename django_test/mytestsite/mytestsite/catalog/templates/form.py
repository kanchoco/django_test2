# https://stackoverflow.com/questions/40108197/upload-html-in-django
from django import forms


class ReadFileForm(forms.Form):
    file = forms.FileField()
