from cgitb import html
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.template import loader
import paralleldots

paralleldots.set_api_key("API_KEY")

# Create your views here.
def index(request):
    return render(request, "random/index.html")
def start(request):
    return render(request, "random/start.html")
def breath(request):
    print(request.GET)
    print(type(request.GET["mind"]))
    emo = paralleldots.emotion(str(request.GET["mind"]))
    emo = emo["emotion"]
    stats = emo

    list1 = []
    for x in stats.keys():
        if stats[x] == max(stats.values()):
            list1.append(x)

    max_keys = list1
    if len(max_keys) > 1:
        if "Angry" in max_keys:
            emo = "Angry"
        elif "Fear" in max_keys:
            emo = "Fear"
        else:
            emo = "Happy"
    else:
        emo = max_keys[0]
   
    context = {
        

        'min': emo,
        'artis':request.GET["artist"],
        'youtube':request.GET['youtuber'],
        'sho':request.GET['show'],
        'tea':request.GET['team'],
    }
    return render(request, "random/breath.html", context)
    
def final(request):
    context = {
        

        'min': request.GET["mind"],
        'artis':request.GET["artist"],
        'youtube':request.GET['youtuber'],
        'sho':request.GET['show'],
        'tea':request.GET['team'],
    }
    print("hasdf", request.GET["mind"], request.GET["artist"], request.GET['youtuber'], request.GET["show"], request.GET["team"])

    return render(request, "random/final.html", context)
