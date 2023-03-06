from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
from .forms import AddItem, UpdateItem
from .models import Order, Item, OrderItem
from .context_processors import new_order_id
from .utils import delete_order_item
import re


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def search_items(request):
    item_name = request.POST.get('item-name')
    suggestions = []
    try:
        index_number = int(item_name)
        item = Item.objects.get(pk=index_number)
        suggestions.append(
            (item, str(item))
        )
    except ValueError:
        query = re.compile(item_name, re.IGNORECASE)

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
        context
    )


@csrf_exempt
def add_item(request, item_id):
    #  adds item to the order
    order_id = new_order_id(request).get('new_order_id')
    print(f"{order_id=} {item_id=}")
    item = Item.objects.get(pk=item_id)
    print(f"{item=}")
    order = Order.objects.get_or_create(pk=order_id)[0]
    order_item = OrderItem.objects.create(
        order=order,
        item=item)
    order_item.save()
    context = {"order": order}
    return render(
        request,
        'partials/show-added-items.html',
        context
    )


@csrf_exempt
def update_item_quantity(request, item_id, order_id):
    # updates the quantity of the item in the order
    quantity = request.POST.get('item-quantity')
    order = Order.objects.get(pk=order_id)
    print(f'Got order: {order}')
    order_item = order.orderitem_set.get(item__pk=item_id)
    print(f'Got relative order_item: {str(order_item.item)}')
    order_item.quantity = quantity
    print(f'Updated quantity: {order_item.quantity}')
    order_item.save()
    context = {"order": order}
    return render(request, 'partials/show-added-items.html', context)


@csrf_exempt
def delete_item(request, order_id, item_id):
    order = delete_order_item(order_id, item_id)
    context = {
        'order': order
    }
    return render(request,
                  'partials/show-added-items.html', context)


@csrf_exempt
def create_order(request, order_id):
    print(f'Create Order: {order_id}')
    order = Order.objects.get(pk=order_id)
    order.save()
    new_order = Order.objects.create(pk=order_id+1)
    context = {
        'prev_order': order,
        'order': new_order,
    }
    return render(request, 'index.html', context)


@csrf_exempt
def update_table_number(request, order_id):
    order = Order.objects.get(pk=order_id)
    table_number = request.POST.get('table-number')
    order.table_number = table_number
    order.save()
    context = {
        'order': order,
    }
    return render(request, 'index.html', context)


def pizzeria_login(request):
    form = AuthenticationForm
    if request.method == "POST":
        print('Inside login post method')
        form = AuthenticationForm(request, data=request.POST)
        print('Got login form')
        if form.is_valid():
            print('Form is valid')
            user = form.get_user()
            print('Got User')
            if user is not None:
                print('User exists')
                login(request, user)
                return redirect('billing:pizzeria_admin')
            else:
                print('User does not exist')
                return render(request,
                              'pizzeria-login.html',
                              {'error_message': 'Invalid Login!'})
        else:
            print('Form is invalid')
            form = AuthenticationForm
            return render(request,
                          'pizzeria-login.html',
                          {'login_form': form,
                           'error_message': 'Form is Invalid'})
    else:
        print('Inside request get method')
        context = {
            'login_form': form
        }

        print('Rendering login page')
        return render(request, 'pizzeria-login.html', context)


@login_required
def pizzeria_admin(request):
    return render(request,
                  'pizzeria-admin.html')
