import random
import datetime
from django.shortcuts import render, HttpResponse
from laptop.models import Product

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! It's my project")


def fun_view(request):
    fun_list = ["Я напомню вам состав БТС, первый - кончимин, второй - инсулин, "
                "третий - панкихой, четвертый - отченаш и пятый - чокопай",
                "идут как то два безруких, никого не трогают"]
    if request.method == 'GET':
        return HttpResponse(random.choice(fun_list))


def main_view(request):
    date = datetime.datetime.now()
    if request.method == 'GET':
        return render(request, 'main.html', context={'date': date})


def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'laptop/product_list.html', context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse('Product not found', status=404)
        context = {'product': product}
        return render(request, 'laptop/product_detail.html', context)

