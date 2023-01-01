from django.shortcuts import render


# Create your views here.
def index(request):
    context={}
    return render(request, "interact/index.html", context);

def detail(request, pk):
    context={}
    return render(request, "interact/details.html", context);
