import random
import datetime
from django.shortcuts import render, HttpResponse

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

