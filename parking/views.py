# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

import numpy as np
from matplotlib import pyplot as plt
import datetime

from .models import Citation


# Create your views here.


def parking_index(request):
    return render(request, "parking/index.html")


# class ResultsView(generic.DetailView):
#     model = Citation
#     template_name = 'parking/view.html'
#     context_object_name = "citation_list"


def view(request):
    hour = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    m_count = list()
    t_count = []
    w_count = []
    tr_count = []
    f_count = []
    x = 7
    while x < 19:
        monday = Citation.objects.filter(date__week_day=2, date__hour=x).values("date")
        mvls = monday.values_list('date', flat=True)
        mcnt = len(mvls)
        m_count.append(mcnt)

        tuesday = Citation.objects.filter(date__week_day=3, date__hour=x).values("date")
        tvls = tuesday.values_list('date', flat=True)
        tcnt = len(tvls)
        t_count.append(tcnt)

        wednesday = Citation.objects.filter(date__week_day=4, date__hour=x).values("date")
        wvls = wednesday.values_list('date', flat=True)
        wcnt = len(wvls)
        w_count.append(wcnt)

        thursday = Citation.objects.filter(date__week_day=5, date__hour=x).values("date")
        trvls = thursday.values_list('date', flat=True)
        trcnt = len(trvls)
        tr_count.append(trcnt)

        friday = Citation.objects.filter(date__week_day=6, date__hour=x).values("date")
        fvls = friday.values_list('date', flat=True)
        fcnt = len(fvls)
        f_count.append(fcnt)

        x = x + 1

    return render(request, 'parking/view.html',
                  {'hour': hour, 'm_count': m_count, 't_count': t_count, 'w_count': w_count, 'tr_count': tr_count, 'f_count': f_count})


def upload(request):
    return render(request, "parking/upload.html")


def add(request):
    street = request.POST.get('street')
    date = request.POST.get('date')
    officer = request.POST.get('officer')
    citation = Citation.objects.create(street=street, date=date, officer=officer)
    citation.save()

    return redirect('parking:view')
