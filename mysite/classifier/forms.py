from django import forms

class ImageForm(forms.Form):
    Submit_image = forms.ImageField(required=False)