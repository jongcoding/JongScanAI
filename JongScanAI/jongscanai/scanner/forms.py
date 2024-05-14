from django import forms

class ScanForm(forms.Form):
    url = forms.URLField(label='Website URL', max_length=200, widget=forms.URLInput(attrs={'placeholder': 'Enter the URL to scan'}))
