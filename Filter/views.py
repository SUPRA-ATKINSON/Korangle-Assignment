from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'html/index.htm')

def namesort(request):
    return render(request, 'html/namesort.htm')

def datesort(request):
    return render(request, 'html/datesort.htm')

def famesort(request):
    return render(request, 'html/famesort.htm')

    
