from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def advertisement_list(request, *args, **kvargs):
    return render(request, 'advertisement/advertisement_list.html', {})
