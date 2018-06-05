from django.views import View
from django.http import JsonResponse

from . import testing


class ProfChoiceView(View):

    def get(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        result = ''
        for choice in request.POST.keys():
            result = result + testing.test(choice) if testing.test(choice) else ''
        result = testing.get_test_results(result)
        return JsonResponse({'result': result})


class GetEgePoints(View):

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
