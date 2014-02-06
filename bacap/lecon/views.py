from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import lecon

def acueill(request):
	les_lecons = lecon.Objects.all()
	template = render_to_response('lecon/acueill.html', {'les_lecons' : les_lecons'})
	return HttpResponse(template)