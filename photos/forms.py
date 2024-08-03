from django import forms
from .models import Photo, Category

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
