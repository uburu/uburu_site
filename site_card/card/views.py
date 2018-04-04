from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('card/index.html')
	context = {
	"hi" : "hi",
	}
	return HttpResponse(template.render(context, request))