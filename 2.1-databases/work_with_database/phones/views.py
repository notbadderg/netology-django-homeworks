from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    selected_sorting = request.GET.get('sort')
    if selected_sorting == 'name':
        order_by = 'name'
    elif selected_sorting == 'min_price':
        order_by = 'price'
    elif selected_sorting == 'max_price':
        order_by = '-price'
    else:
        order_by = 'id'

    phones = Phone.objects.all().order_by(order_by)

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
