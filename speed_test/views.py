from django.http import HttpResponse
from django.shortcuts import render

import sys
sys.path.append('..')
from game_01 import speed_hands
# imports speed_hands

# Create your views here.
def index(request):
    return render(request, 'speed_test/index.html')


def type_test(request):
    if request.method == "POST":
        
        return render(request, 'speed_test/start_type_test.html')
    else:
        return render(request, 'speed_test/type_test.html')


def equ_solve(request):
    return HttpResponse("Equation solving")
