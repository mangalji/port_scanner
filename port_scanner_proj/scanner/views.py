from django.shortcuts import render

# Create your views here.
def home(request):
    print()
    return render(request, "index.html")