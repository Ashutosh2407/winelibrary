from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Query
from wines.services.search import search
import os 
from django.conf import settings
# Create your views here.

def index(request):
    return render(request,"wines/index.html")

def results(request, query):
    query = request.POST['query']
    result = search(query)
    return render(request,"wines/results.html", {"result":result})
    