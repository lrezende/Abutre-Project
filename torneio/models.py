from django.db import models

# Create your models here.
class Players(models.Model):
    player = models.CharField(max_length=30)
    nick = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=30)
    redesocial = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    def __str__(self):
        return self.player
    class Meta:
        ordering = ('player',)

class Torneios(models.Model):
	torneio = models.CharField(max_length=20)
	qtd_etapas = models.IntegerField()
	qtd_players = models.IntegerField()
	qtd_rebuy = models.IntegerField()
	vlr_buyinn = models.FloatField()
	vlr_rebuy = models.FloatField()
	vlr_jackpot = models.FloatField()
	def __str__(self):
		return self.torneio
	class Meta:
		ordering = ('torneio',)

class Etapa(models.Model):
	etapa = models.CharField(max_length=20)
	id_torneio = models.ForeignKey(Torneios)
	local = models.CharField(max_length=20)
	status = models.BooleanField()
	data = models.DateField()
	def __str__(self):
		return self.etapa
	class Meta:
		ordering = ('data',)

class Ranking(models.Model):
	id_torneio = models.ForeignKey(Torneios)
	id_etapa = models.ForeignKey(Etapa)
	id_player = models.ForeignKey(Players)
	buyinn = models.IntegerField()
	qtd_rebuy = models.IntegerField()
	pontuacao = models.IntegerField()
	posicao = models.IntegerField()
	premio = models.FloatField()

#class ClassName(object):
#	"""docstring for ClassName"""
#	def __init__(self, arg):
#		super(ClassName, self).__init__()
#		self.arg = arg
		