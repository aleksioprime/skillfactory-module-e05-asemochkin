from django.shortcuts import render
from django.views.generic import ListView
from auto.models import Car
from django.db.models import Q, F

class CarView(ListView):
    model = Car
    context_object_name = "cars"
    template_name = "car_list.html"
    def get_queryset(self):
        query = Q()
        if 'manufacturer' in self.request.GET:
            query.add(Q(manufacturer__contains=self.request.GET['manufacturer']), Q.AND)
        if 'model' in self.request.GET:
            query.add(Q(model__contains=self.request.GET['model']), Q.AND)
        if 'year' in self.request.GET:
            if self.request.GET['year']:
                query.add(Q(year=self.request.GET['year']), Q.AND)
        if 'transmission' in self.request.GET:
            query.add(Q(transmission=self.request.GET['transmission']), Q.AND)
        if 'color' in self.request.GET:
            query.add(Q(color__contains=self.request.GET['color']), Q.AND)
        queryset = Car.objects.filter(query)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transmissions'] = Car.TRANS
        return context