from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
from .forms import PollForm

class IndexView(generic.TemplateView):
    template_name = "polls/index.html"

class LastPollsView(generic.ListView):
    template_name = 'polls/lastPolls.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class MostVotedView(generic.ListView):
    template_name = 'polls/mostVoted.html'
    context_object_name = 'most_voted_polls'

    def get_queryset(self):
        """Return the top 5 voted polls."""
        return Choice.most_voted_polls()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class CreateView(FormView):
    template_name = 'polls/pollForm.html'
    form_class = PollForm
    
def pollFormError(request):
    return render(request, 'polls/pollFormError.html')

def createPoll(request):
    
    count = request.POST.get('count')
    form = PollForm(request.POST, count=count)
    
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        question = form.cleaned_data['question']
        q = Question(question_text=question, pub_date=timezone.now())
        q.save()
        print(count)
        for i in range(int(count)):
            choice = form.cleaned_data['choice_' + str(i+1)]
            q.choice_set.create(choice_text=choice, votes=0)
            print(choice)
            
        q.save()
        
        return render(request, 'polls/pollCreated.html', {'question': q})
    else:
        return render(request, 'polls/pollFormError.html')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
