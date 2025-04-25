from django.shortcuts import render

def history(request):
    return render(request, 'history.html')

def frameworks(request):
    return render(request, 'frameworks.html')

def libraries(request):
    return render(request, 'libraries.html')

def documentation(request):
    return render(request, 'documentation.html')
def home(request):
    return render(request, 'home.html')
