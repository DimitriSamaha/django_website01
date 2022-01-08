from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse

import sys
sys.path.append('C:/dimi_coding/web/game_01')
import rock_paper_scissors as rps


# Create your views here.
def index(request):
    if request.method == "POST":
        choice = request.POST['options']
        i = rps.convert_to_i(choice)
        x = rps.choose_comp()
        comp_choice = rps.display_title(x)
        res = rps.check_win(i, x)
        respo = f"You chose {choice} and the computer chose {comp_choice}: {res}"
        return render(request, 'RockPaperScissors/index.html', {
            "message": respo,
            "result": res
        })
    else:
        return render(request, 'RockPaperScissors/index.html')
