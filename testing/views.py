from django.views import View
from django.http import JsonResponse

from . import testing
from core import models


class ProfChoiceView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        result = ''
        for choice in request.POST.keys():
            result = result + testing.test(choice) if testing.test(choice) else ''
        result = testing.get_test_results(result)
        psychotype = models.Psychotype.objects.filter(title=result)[0]
        return JsonResponse({
            'title': psychotype.title,
            'description': psychotype.description,
        })


class GetEgePoints(View):

    def post(self, request, *args, **kwargs):
        subjects = {
            'info': 'Информатика',
            'history': 'История',
            'geography': 'География',
            'sculpture': 'Скульптура',
            'paint': 'Рисование',
            'chemistry': 'Химия',
            'biology': 'Биология',
            'physyc': 'Физика',
            'literutare': 'Литература',
            'language': 'Английский язык',
            'society': 'Обществознание',
            'math': 'Математика',
            'russian': 'Русский язык',
        }
        psychotype = request.POST.get('psychotype')
        speciality_by_psychotype = models.Psychotype.objects.filter(title=psychotype)[0].speciality.all()
        response = [speciality.title for speciality in speciality_by_psychotype]
        return JsonResponse({'response': ' '.join(response)})
