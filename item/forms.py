from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'itemname', 'description', 'manufacturer', 'price', 'image')

        widgets = {
            'category':forms.Select(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }

        widgets = {
            'itemname':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }

        widgets = {
            'description':forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }
        widgets = {
            'manufacturer':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }   
        widgets = {
            'price':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }   
        widgets = {
            'image':forms.FileInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }   

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('itemname', 'description', 'manufacturer', 'price', 'image', 'is_sold')

        widgets = {
            'itemname':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }

        widgets = {
            'description':forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }
        widgets = {
            'manufacturer':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }   
        widgets = {
            'price':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }   
        widgets = {
            'image':forms.FileInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }                   