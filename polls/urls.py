from django.contrib import admin

from django.conf.urls import url




from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^list-products/$', views.ListView.as_view(), name='list-products'),
    url(r'^view-products/$', views.ViewProductsView.as_view(), name='view-products'),
    url(r'^order-form/$', views.order_form, name='order-form'),
    url(r'^order-confirm/$', views.order_confirm, name='order-confirm'),

    url(r'^(?P<listing_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^add/$', views.new_listing, name='index2'),

    url(r'^producer-signup/$', views.producer_signup, name='producer_signup'),
    url(r'^consumer-signup/$', views.consumer_signup, name='consumer_signup'),
    url(r'^payment-form/$', views.payment_form, name='payment_form'),
    url(r'^checkout/$', views.checkout, name='checkout_page'),
    url(r'^thankyou/$', views.thankyou, name='thankyou_page'),
]