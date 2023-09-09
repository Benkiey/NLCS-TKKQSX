from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')
def base(request):
    return render(request, 'app/base.html')

def thongke(request):
    return render(request, 'app/thongke.html')

def quaythu(request):
    return render(request, 'app/quaythu.html')
