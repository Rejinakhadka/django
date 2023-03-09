from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('addproduct/',post_product),
    path('addcategory/',post_category),
]