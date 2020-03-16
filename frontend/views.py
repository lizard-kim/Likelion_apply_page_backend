from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def apply(request):
    return render(request, 'apply.html') 