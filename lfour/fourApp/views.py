from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello World','number':100}
    return render(request,'fourApp/index.html', context=context_dict)

def other(request):
    return render(request,'fourApp/other.html')

def base(request):
    return render(request,'fourApp/base.html')

def relative(request):
    return render(request,'fourApp/relative.html')
