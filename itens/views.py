from django.shortcuts import render
from .models import Itens
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

# Create your views here.

class ItensList(ListView):
    model = Itens

class ItensCreate(CreateView):
    model = Itens
    fields = ('name', 'price', 'description')
    success_url = reverse_lazy('itens_namespace:itens_list')

class ItensDelete(DeleteView):
    model = Itens
    success_url = reverse_lazy('itens_namespace:itens_list')

class ItensUpdate(UpdateView):
    model = Itens
    fields = ('name', 'price', 'description')
    success_url = reverse_lazy('itens_namespace:itens_list')
