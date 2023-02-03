from django.shortcuts import render, HttpResponse
from .models import register


# Create your views here.
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = register()
        user.Username = name
        user.Password = password
        user.save()
        return HttpResponse("Welcome")
    return render(request, 'hello.html')