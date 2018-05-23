from django.contrib import admin

from django.conf.urls import url




from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^add/$', views.question, name='index2'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^payment-form/$', views.payment_form, name='payment_form'),
    url(r'^checkout/$', views.checkout, name='checkout_page'),
    url(r'^thankyou/$', views.thankyou, name='thankyou_page'),
]