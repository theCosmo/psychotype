from django.views.generic.base import TemplateView

from testing import testing


class MainPageView(TemplateView):

    template_name = 'core/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = [question for question in testing.QUESTIONS.keys()]

        context['questions'] = questions
        return context
