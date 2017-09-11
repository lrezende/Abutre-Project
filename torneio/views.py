from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from .models import Players
from .models import Ranking

class PlayersListView(ListView):
    model = Players

class RankingListView(ListView):
    model = Ranking


def rankingAll(request,):
	return render_to_response("torneio/ranking_list.html", 
		{
		"object_list": Ranking.objects.values("id_player", "pontuacao").annotate(dcount=Count("pontuacao"))
		}
		)