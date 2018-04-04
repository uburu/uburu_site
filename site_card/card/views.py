from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader


DATA = [
dict(id=1, full_name="Никита Рубинов", 
	short_description_bold="Лидер команды ụbụrụ.", 
	short_description="Студент МГТУ им. Н.Э. Баумана. Кафедра ИУ-7. Увлекаюсь Deep Learning и web.",
	projects=["Cайт для подготовки к ЕГЭ и ГИА", "Детектор пауз хезитации", "Умный поиск"]),
dict(
	id=2, full_name="Иван Морозов",
	short_description_bold="Программист. Руководитель проектов по компьютерному зрению. ",
	short_description="Студент МГТУ им. Н.Э. Баумана. Кафедра ИУ-7. Увлекаюсь Компьютерным зрением и web.",
	projects=["Парсер Instagram без API", "Распознавание минималистичных фотографий", "Умный поиск"]),
]

# Create your views here.
def index(request):
	data = DATA
	template = loader.get_template('card/index.html')
	context = {
	"teammates" : data,
	}
	return HttpResponse(template.render(context, request))