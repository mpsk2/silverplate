from django.db import models

# Create your models here.
class Dados_Ingrediente(models.Model):
	Ingrediente = models.CharField(max_length=1000)
	Receita = models.CharField(max_length=500)
	Grupo = models.CharField(max_length=500, default='Ingredientes')

	def __str__(self):
		return self.descricao

class Dados_Modo_Fazer(models.Model):
	Descricao = models.CharField(max_length=500)
	Receita = models.CharField(max_length=500)
	Grupo = models.CharField(max_length=500, default='Modo de Fazer')
	
	def __str__(self):
		return self.descricao

class Ingrediente_Spec(models.Model):
	Palavra = models.CharField(max_length=500)
	Count = models.IntegerField()
	Tipo = models.CharField(max_length=1)

