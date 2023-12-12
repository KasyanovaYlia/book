from django.shortcuts import render,redirect
from products.models import Product
from .forms import ProductForm
# Create your views here.
def index(request):
    context = {'title': 'Книжный сайт',}
    return render(request,'products/index.html',context)


def products(request):
    context={
        'title': 'Новинки',
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html',context)

def add(request):

    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error='Данные не верные'


    form = ProductForm()

    data = {
        'form': form,
        'error': error
    }
    context = {'title': 'Книжный сайт',}
    return render(request,'products/add.html',data)