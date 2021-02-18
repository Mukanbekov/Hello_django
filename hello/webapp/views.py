from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def reg_view(request):
    return render(request, 'reg.html')

def sot_view(request):
    return render(request, 'sot.html')
# Create your views here.
