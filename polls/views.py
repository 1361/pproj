from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from mysite import settings
import stripe

from .models import Question, Choice, Car

stripe.api_key = "sk_test_wDLDyofvO4HaufPVzroEI5p8"


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def payment_form(request):
    context = {"stripe_key": settings.STRIPE_PUBLIC_KEY}
    return render(request, "polls/payment-form.html", context)


# Using Flask


# def checkout(request):
#     token = request.POST.get('stripeToken')
#     stripe.Charge.create(
#         amount=999,
#         currency='usd',
#         description='Example charge',
#         source=token,
#     )


def checkout(request):
    new_car = Car(
        name="Honda Civic",
        year=2017
    )

    token = request.POST.get("stripeToken")

    try:
        charge = stripe.Charge.create(
            amount=2000,
            currency="usd",
            source=token,
            description="The product charged to the user"
        )

        new_car.charge_id = charge.id

    except stripe.error.CardError as ce:
        return False, ce

    else:
        new_car.save()
        return HttpResponseRedirect('/polls/thankyou')

def thankyou(request):
    return render(request, "polls/thankyou.html")


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


@permission_required('polls.add_question')
def question(request):
    question_txt = request.POST.get('question_txt')
    ch1 = request.POST.get('ch1')
    ch2 = request.POST.get('ch2')
    new_question = Question(question_text=question_txt, pub_date=timezone.now())
    new_question.save()
    p = new_question
    p.choice_set.create(choice_text=ch1, votes=0)
    p.choice_set.create(choice_text=ch2, votes=0)

    return HttpResponseRedirect('/polls/')
