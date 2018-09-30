from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control', 'placeholder':'Your email...'}))
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'size':'40','class': 'form-control', 'placeholder':'Subject...'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Message...'}))
