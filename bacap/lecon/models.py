from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class lecon(models.Model):
	les_class = (
		('1er', '1er annee bac'),
		('2eme', '2eme annee bac'),
	)
	les_matiers = (
		('ar', 'la langue arabe'),
		('fr', 'la langue francais'),
		('i', "l'education islamic"),
		('geo', 'la geographie'),
		('m', 'le math'),
		('pc', 'le phisique & chimique'),
		('svt', 'le svt'),
		('ph', 'la philosophie'),
		('an', "l'anglais"),
	)
	les_types = (
		('lecon', 'un lecon'),
		('examine', 'un examine')
	)
	titre = models.TextField(max_length=200)
	le_auteur = models.ForeignKey(User)
	le_niveau_scolaire = models.CharField(max_length=4, choices=les_class)
	la_matier = models.CharField(max_length=3, choices=les_matiers)
	le_type = models.CharField(max_length=6, choices=les_types)
	la_date = models.DateTimeField(auto_now_add=True)
	le_contenu = models.TextField()
	le_tag = TaggableManager()

	def __unicode__(self):
		return self.title