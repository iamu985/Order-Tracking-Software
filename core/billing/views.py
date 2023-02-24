from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
from .forms import AddItem, UpdateItem
from .models import Order, Item
import re

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # form = AddItem()
    # new_order = Order.objects.create()
    # context = {"form": form,
    #            "new_order": new_order}
    # return render(request, 'billing/index.html', context)


@csrf_exempt
def search_items(request):
    item_name = request.POST.get('item-name')
    query = re.compile(item_name, re.IGNORECASE)
    suggestions = []
    for item in Item.objects.all():
        if re.search(query, item.name):
            suggestions.append(
                #  item[0] is the item object
                #  item[1] is the string to represent the item
                (item, str(item)))
    context = {"suggestions": suggestions}
    return render(
        request,
        'partials/search-results.html',
        context)


def add_item(request):
    pass
