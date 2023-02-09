from django import forms 

from apps.order.models import Order 



class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ["address", "mobile"]

        widgets = {
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "mobile": forms.TextInput(attrs={"class":"form-control"}),
        }