from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader


# Информация о разаработчиах
# TODO в будущем перенести в json 
DATA = [
dict(id=1, full_name="Никита Рубинов", 
	short_description="Лидер команды ụbụrụ.", 
	full_description="Студент МГТУ им. Н.Э. Баумана. Кафедра ИУ-7. Студент образовательной программы Технопарк Mail.Ru Group. Увлекаюсь Deep Learning и web.",
	projects=["Cайт для подготовки к ЕГЭ и ГИА", "Детектор пауз хезитации", "Умный поиск", "Проверка смысловой близости двух текстов"],
	photo_name= "nikitarub.jpeg"
	),

dict(
	id= 2,
	full_name= 'Максим Ермаков',
	short_description= 'Backend разработчик',
	full_description= 'Студент МГТУ им Н. Э. Баумана. Кафедра ИУ-7. Образовательная программа Технопарк Mail.Ru Group',
	projects= ['Telegram бот - доставщик еды', 'Telegram бот - связка ключей, с возможностью генерации новых безопасных паролей', 
							'Умный поиск', 'Проверка смысловой близости двух текстов',],
	photo_name= "max.jpeg"
),
dict(
	id=3, full_name="Иван Морозов",
	short_description="Программист. Разработчик в направлении компьютерное зрение. ",
	full_description="Студент МГТУ им. Н.Э. Баумана. Кафедра ИУ-7. Увлекаюсь Компьютерным зрением и web.",
	projects=["Парсер Instagram без API", "Распознавание минималистичных фотографий", "Умный поиск"],
	photo_name= "ivan.jpeg"
),
dict(
	id=4, full_name="Никита Колобаев", 
	short_description="Разработчик. Тестировщик.", 
	full_description="Студент МГТУ им. Н.Э. Баумана. Кафедра ИУ-7. Увлекаюсь аналитикой, проектированием и web",
	projects=["Умный поиск"],
	photo_name= "nikitakol.jpeg"
)
]


# редерениг основной страницы
def index(request):
	data = DATA
	template = loader.get_template('card/index.html')
	context = {
	"teammates" : data,
	}
	return HttpResponse(template.render(context, request))