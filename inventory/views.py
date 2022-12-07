from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import custom_forms as cf
from inventory.models import Location, Consumable, Inventory, DateTable
from django.views.decorators.cache import never_cache


CHURCH_NAME = "Grace Baptist Church"

items = Consumable.objects.all()


@never_cache
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    locations = Location.objects.all()
    return render(request, "inventory/index.html", {
        "church_name": CHURCH_NAME,
        "title": "inventory",
        "locations": locations,
        "items": items
    })


@never_cache
def new_item(request):
    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse("login", current_app="users"))
        return HttpResponseRedirect(reverse("users:login"))
    if request.method == "POST":
        form = cf.NewItemForm(request.POST)
        if form.is_valid():
            try:
                new_form_item = form.cleaned_data["item_name"]
                location_name = form.cleaned_data["location"]

                new_form_item = Consumable(name=new_form_item, item_location=location_name)
                new_form_item.save()

                return HttpResponseRedirect(reverse("inventory:index"))

            except:
                print("error")
    else:
        return render(request, "inventory/new_item.html", {
            "church_name": CHURCH_NAME,
            "title": "inventory: Add Item",
            "items": items,
            "form": cf.NewItemForm()
        })


@never_cache
def new_location(request):
    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse("login", current_app="users"))
        return HttpResponseRedirect(reverse("users:login"))
    if request.method == "POST":
        form = cf.NewLocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data["location"]
            # Add SQL Data
            location = Location(location_name=location)
            location.save()
            return HttpResponseRedirect(reverse("inventory:index"))
            # return HttpResponseRedirect(reverse("inventory:new_location"))
    else:
        locations = Location.objects.all()
        return render(request, "inventory/new_location.html", {
            "church_name": CHURCH_NAME,
            "title": "inventory: New Room",
            "locations": locations,
            "form": cf.NewLocationForm()
        })


# @never_cache
def count(request):
    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse("login", current_app="users"))
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "inventory/count.html", {
        
    })
    
#     if request.method == "POST":
#         form = cf.NewLocationForm(request.POST)
    #     if form.is_valid():
    #         location = form.cleaned_data["location"]
    #         # Add SQL Data
    #         location = Location(location_name=location)
    #         location.save()
    #         return HttpResponseRedirect(reverse("inventory:index"))
    #         # return HttpResponseRedirect(reverse("inventory:new_location"))
    # else:
    #     # Needs location object
    #     return render(request, "inventory/count.html", {
    #         "church_name": CHURCH_NAME,
    #         "title": "inventory: New Room",
    #         # "form": cf.NewItemForm
    #     })


@never_cache
def stock(request):
    # cache.clear()
    # cache.set('my_cache_key', None)
    if request.method == "POST":
        pass
    #     form = NewStockForm(request.POST)
    #     if form.is_valid():
    #         stocked_item = form.cleaned_data["stocked_item"]
    #         stock_quantity = form.cleaned_data["stock_quantity"]

    else:
        return render(request, "inventory/stock.html", {
            "church_name": CHURCH_NAME,
            "title": "inventory: Re-Stocking",
            "form": cf.NewStockForm()
        })
