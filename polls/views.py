from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from polls.forms import ProducerProfileForm, ConsumerProfileForm
from django.contrib.auth import login, authenticate
from mysite import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
import stripe
from decimal import Decimal

from .models import Question, Choice, Listing, Cart

stripe.api_key = "sk_test_wDLDyofvO4HaufPVzroEI5p8"


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class ListView(generic.ListView):
    template_name = 'polls/list-products.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Listing.objects.order_by('-pub_date')[:5]


class ViewProductsView(generic.ListView):
    model = Listing
    template_name = 'polls/view-products.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Listing.objects.order_by('-pub_date')[:5]


# class OrderFormView(generic.ListView):
#     model = Listing
#     template_name = 'polls/order-form.html'
#     context_object_name = 'latest_question_list'


class DetailView(generic.DetailView):
    model = Listing
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Listing
    template_name = 'polls/results.html'


# class OrderConfirmView(generic.DetailView):
#     model = Listing
#     template_name = 'polls/order-confirm.html'


def producer_signup(request):
    if request.method == 'POST':
        form = ProducerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='Beef Producers')
            group.user_set.add(user)
            login(request, user)
            return redirect('polls:index')
    else:
        form = ProducerProfileForm()
    return render(request, 'registration/producer-signup.html', {'form': form})


def consumer_signup(request):
    if request.method == 'POST':
        form = ConsumerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='Consumers')
            group.user_set.add(user)
            login(request, user)
            return redirect('polls:index')
    else:
        form = ConsumerProfileForm()
    return render(request, 'registration/consumer-signup.html', {'form': form})


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
    # new_order = Listing(
    #     name="Honda Civic",
    #     year=2017
    # )
    type = request.POST.get('type')
    cost = request.POST.get('cost')
    co = float(cost)
    quantity = request.POST.get('quantity')
    qu = float(quantity)
    charge_amount = qu * co *100
    ch1 = int(charge_amount)
    token = request.POST.get("stripeToken")

    try:
        charge = stripe.Charge.create(
            amount=ch1,
            currency="usd",
            source=token,
            description="The product charged to the user"
        )

        # new_car.charge_id = charge.id

    except stripe.error.CardError as ce:
        return False, ce

    else:
        # new_car.save()
        return HttpResponseRedirect('/polls/thankyou')


def thankyou(request):
    return render(request, "polls/thankyou.html")


def vote(request, listing_id):
    p = get_object_or_404(Listing, pk=listing_id)
    try:
        selected_choice = p.products_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'listing': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.amount_available -= 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def order_form(request):
    pid = Listing.objects.get(pk=request.POST['listing_id'])

    products = pid.products_set.all()
    return render(request, 'polls/order-form.html', {'pid': pid, 'products': products})


def shopping_cart(request):
    type = request.POST.get('type')
    quantity = request.POST.get('quantity')
    listing_id = request.POST.get('id')
    listing = Listing.objects.get(pk=listing_id)
    p = listing.products_set.get(type=type)
    cost = float(p.list_price)
    qu = float(quantity)
    total = cost*qu
    order = p.cart_set.create(quantity=quantity)
    order.save()
    return render(request, 'polls/order-confirm.html', {'listing': listing, 'p': p, 'order': order, 'total': total})


@permission_required('polls.add_question')
def new_listing(request):
    listing_name = request.POST.get('listing_name')
    new_listing = Listing(listing_name=listing_name, pub_date=timezone.now())
    new_listing.save()
    p = new_listing
    return render(request, 'polls/edit-listing.html', {'p': p})

    # type2 = request.POST.get('type2')
    # amount_available2 = request.POST.get('amount_available2')
    # list_price2 = request.POST.get('list_price2')
    #
    # type3 = request.POST.get('type3')
    # amount_available3 = request.POST.get('amount_available3')
    # list_price3 = request.POST.get('list_price3')
    # p.products_set.create(type=type, amount_available=amount_available, list_price=list_price)
    # p.products_set.create(type=type2, amount_available=amount_available2, list_price=list_price2)
    # p.products_set.create(type=type3, amount_available=amount_available3, list_price=list_price3)
    # p.products_set.create(choice_text=ch2, votes=0)

@permission_required('polls.add_question')
def edit_listing(request):
    type1 = request.POST.get('type')
    amount_available = request.POST.get('amount_available')
    unit = request.POST.get('unit')
    list_price = request.POST.get('list_price')
    id = request.POST.get('id')
    p = Listing.objects.get(pk=id)
    p.products_set.create(type=type1, amount_available=amount_available, unit=unit, list_price=list_price)
    p.save()
    return render(request, 'polls/edit-listing.html', {'p': p})
