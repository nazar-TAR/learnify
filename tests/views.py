
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from .models import Test
from django.core.paginator import Paginator


class TestDetailView(TemplateView):
    template_name = 'tests/test_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson_id = self.kwargs['lesson_id']
        test = get_object_or_404(Test, lesson_id=lesson_id)
        questions = test.questions.all()
        paginator = Paginator(questions, 6)
        page_num = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        questions_with_options = []
        for question in test.questions.all():
            options = question.get_shuffled_options()
            questions_with_options.append({
                'question': question,
                'shuffled_options': options
            })

        context['test'] = test
        context['page_obj'] = page_obj
        context['questions_with_options'] = questions_with_options
        return context

    def post(self, request, *args, **kwargs):
        lesson_id = kwargs['lesson_id']
        test = get_object_or_404(Test, lesson_id=lesson_id)
        score = 0

        for question in test.questions.all():
            user_answer = request.POST.get(f'question{question.id}')
            if user_answer == question.correctAnswer:
                score += 1

        return render(request, 'tests/test_result.html', {
            'test': test,
            'score': score,
            'total_questions': test.questions.count()
        })


