from django.shortcuts import render


# Create your views here.

def file_home(request):
    return render(request, "file_crud/file_home.html")
