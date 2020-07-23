from django.http import HttpResponse

def index(request):
    return HttpResponse("_Привет мир!_")

def test    (request):
    return HttpResponse("_ТЕСТОВАЯ СТРАНИЦА_")
