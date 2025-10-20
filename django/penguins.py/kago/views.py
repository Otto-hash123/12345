from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, Kago")

def home(request):
    return  HttpResponse("this is home page ---------------")