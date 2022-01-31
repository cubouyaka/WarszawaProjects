from django.shortcuts import render

def index(request):
    return render(request, "warszawa1/index.html")

def pdf_path(request):
    return render(request,"")