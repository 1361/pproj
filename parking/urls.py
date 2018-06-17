from django.conf.urls import url




from . import views

urlpatterns = [
    url(r'^$', views.parking_index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^add/$', views.add, name='add'),
    url(r'^view/$', views.view, name='view'),

]
