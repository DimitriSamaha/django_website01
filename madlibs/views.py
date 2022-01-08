from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":

        adj = request.POST["adjective"]
        verb1 = request.POST["verb1"]
        verb2 = request.POST["verb2"]
        famous_person = request.POST["famous_person"]

        result = f"Computer programming is so {adj}! It makes me so excited all the time because" \
                 f"I love to {verb1}. Stay positive and {verb2} like you are {famous_person}"
        
        return render(request, 'madlibs/index.html', {
            "message": result
        })
    else:
        return render(request, 'madlibs/index.html')
