from django.shortcuts import render
from django.http import HttpResponse
from numpy import negative, positive
from .forms import userinput
from .sentiment import primary
import matplotlib.pyplot as plt
# Create your views here.

def index(request):
    user_input = userinput()
    return render(request, 'index.html', {'input_jumlah':user_input})

def analyze(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
         input_jumlah = user_input.cleaned_data['jmlTwt']
         print (input_jumlah)
         data = primary(input_jumlah)
         return render(request, 'result.html', {'data': data})
    return render(request, 'index.html', {'input_jumlah': user_input})
