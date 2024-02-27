from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

def browse(request):
    query = request.GET.get('query','')
    items = Item.objects.filter(is_sold=False)
    if query:
        items=items.filter(itemname__icontains=query)

    return render(request, 'item/browse.html',{                          
    'items':items,
    'query':query,
    })

def details(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, "item/detail.html",{
        "item":item
    })

def category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(request, "item/category.html",{
        "category":category,
        "items":category.items.all()
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid:
            item=form.save(commit=False)
            item.created_by = request.user
            item.save()
        
            return redirect('item:details', pk=item.id)    
    else:
        form = NewItemForm()

    return render(request, "item/form.html",{
        'form':form
    } )

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid:
            item.save()
        
            return redirect('item:details', pk=item.id)    
    else:
        form = EditItemForm(instance=item)

    return render(request, "item/form.html",{
        'form':form
    } )
                             