from .models import Product
import django.forms as forms
# from django.forms import Form
from django.forms import ModelForm



# class ProdForm(Form):
#     name = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#     about = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#     )
#     price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
#     weight = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
#     picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input', 'type': 'file'}),
#                                required=False)

class ProdForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name','about','price','weight','picture')
        widgets = {
            'about': forms.TextInput(attrs={'class': 'about'})
        }


class ProdFormAddNew(ModelForm):
    class Meta:
        model = Product
        fields = ('name','about','price','weight','picture')
        widgets = {
            'about': forms.TextInput(attrs={'class': 'about'}),
            'id': forms.IntegerField()
        }

    def save(self):
        product = Product.objects.create(
            name=self.cleaned_data['name'],
            about=self.cleaned_data['about'],
            price=self.cleaned_data['price'],
            weight=self.cleaned_data['weight'],
            picture=self.cleaned_data['picture']
        )
        product.save()
        return product
    #
    # def clean_id(self):
    #     self.id = Product.objects.last().id+1
