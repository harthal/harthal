from django.shortcuts import render
from django.http import HttpResponse
from hart.models import Hartal
from django.views.generic import ListView,DetailView
# Create your views here.
class HartalList(ListView):
    model=Hartal

    def get_queryset(self):
        return Hartal.objects.order_by('-published_date')


class HartalDetail(DetailView):
    model=Hartal
