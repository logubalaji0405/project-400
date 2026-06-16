from django import forms
from .models import Contact, Editor

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={
                'class':'form-control',
                'rows':5
            }),
        }