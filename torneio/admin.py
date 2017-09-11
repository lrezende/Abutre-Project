from django.contrib import admin

# Register your models here.

from .models import Players
from .models import Torneios
from .models import Etapa
from .models import Ranking

#admin.site.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    fields = ['player', 'telefone', 'nick', 'email', 'redesocial']
    list_display = ('player', 'telefone')

admin.site.register(Players, PlayersAdmin)

#admin.site.register(Torneios)
class TorneiosAdmin(admin.ModelAdmin):
    fields = ['torneio', 'vlr_buyinn', 'vlr_jackpot', 'qtd_etapas']
    list_display = ('torneio', 'vlr_buyinn', 'vlr_jackpot', 'qtd_etapas')

admin.site.register(Torneios, TorneiosAdmin)


#admin.site.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    fields = ['id_torneio', 'etapa', 'data', 'local', 'status']
    list_display = ('etapa', 'data', 'status')

admin.site.register(Etapa, EtapaAdmin)

#admin.site.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    fields = ['id_torneio', 'id_etapa', 'id_player', 'buyinn', 'qtd_rebuy', 'posicao', 'pontuacao', 'premio']
    list_display = ('id_etapa', 'id_player', 'buyinn', 'qtd_rebuy')

admin.site.register(Ranking, RankingAdmin)