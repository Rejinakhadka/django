from django.forms import ModelForm
from . models import *

class ProductForm(ModelForm):
    class Meta:
        model = Prouduct
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
