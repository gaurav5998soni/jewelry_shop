from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer, Item
from .forms import CustomerForm, ItemForm
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView
from django.db.models import Q

# Create your views here.
def home(request):
    query = request.GET.get('search')
    members = None
    if query:
        members = Customer.objects.filter(Q(name__icontains=query) |
                                         Q(aadhaar__icontains=query))
    return render(request, 'jewelry/index.html',{'members':members})


def add(request):
    return render(request, 'jewelry/add.html')


def customers(request):
    # form = OurTeamForm()
    members = Customer.objects.all().order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(members, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    query = request.GET.get('search')

    if query:
        users = Customer.objects.filter(Q(name__icontains=query) |
                                         Q(aadhaar__icontains=query))

    context = {
        # 'members': members,
        'page_obj': users,
    }

    return render(request, 'jewelry/customers.html', context)

def add_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            messages.success(request, 'Hey {name}, is created successfully!')
            form.save()
            return redirect('customers')
        else:
            messages.error(request, 'Fill all fields accurately!')
    return render(request, 'jewelry/add.html')

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'

class CustomerDeleteView(DeleteView):
	model = Customer
	success_url = '/'


def add_item(request, pk):
    form = ItemForm()
    customer = Customer.objects.all().get(pk=pk)
    if request.method == "POST":

        form = ItemForm(request.POST)
        if form.is_valid():
            nf = form.save(commit=False)
            nf.customer = customer
            name = form.cleaned_data.get('name')
            messages.success(request, 'Hey {name}, is created successfully!')
            nf.save()
            return redirect('items',pk)
        else:
            messages.error(request, 'Fill all fields accurately!')
    return render(request, 'jewelry/item_add.html', {'customer':customer})


def items(request,pk):
    # form = OurTeamForm()
    members = Item.objects.all().filter(customer=pk).order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(members, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    context = {
        # 'members': members,
        'page_obj': members,
        'pk':pk
    }

    return render(request, 'jewelry/items.html', context)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'item_id', 'weight', 'lending_amount', 'remarks','intrest']



class ItemDeleteView(DeleteView):
    model = Item
    success_url = '/'