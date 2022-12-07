from django import forms
from inventory.models import Location, Consumable, Inventory, DateTable


class NewStockForm(forms.Form):
    stocked_item = forms.ModelChoiceField(queryset=Consumable.objects.all().order_by('name'))
    stock_quantity = forms.IntegerField(label="Adding ", min_value=1)


class NewLocationForm(forms.Form):
    location = forms.CharField(label="New Location")


class NewItemForm(forms.Form):
    item_name = forms.CharField(label="Item Name")
    location = forms.ModelChoiceField(queryset=Location.objects.all().order_by('location_name'))
