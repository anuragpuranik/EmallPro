from django.forms import *;
from . import models;


utypes=[('buyer','Buyer'),('seller','Seller')]

class UserMasterForm(ModelForm):
    password=CharField(widget=PasswordInput())
    usertype=CharField(widget=Select(choices=utypes))
    class Meta:
        model=models.UserMaster
        fields="__all__";
        
class UserProfileForm(ModelForm):
    class Meta:
        model=models.UserProfile
        exclude=['userid',]
        

        
class ProductCategoryForm(ModelForm):
    class Meta:
        model=models.ProductCategory
        fields="__all__";
        
class ProductForm(ModelForm):
    class Meta:
        model=models.Product
        fields="__all__";
        
class OrderMasterForm(ModelForm):
    class Meta:
        model=models.OrderMaster
        fields="__all__";
        
class OrderDetailForm(ModelForm):
    class Meta:
        model=models.OrderDetails
        fields="__all__";
        
class ComplaintForm(ModelForm):
    compdesc=CharField(widget=Textarea({"rows":5, "cols":30}))
    class Meta:
        model=models.Complaints
        fields="__all__";