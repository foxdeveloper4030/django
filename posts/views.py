from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data={'year':1394}
    return render(request,'posts/index.html')