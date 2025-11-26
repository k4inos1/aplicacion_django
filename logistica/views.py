from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vehiculo, Carga
from .forms import VehiculoForm, CargaForm

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'logistica/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiculos_count'] = Vehiculo.objects.count()
        context['cargas_count'] = Carga.objects.count()
        context['ultimas_cargas'] = Carga.objects.order_by('-created_at')[:5]
        return context

# --- Vehiculo CRUD ---
class VehiculoListView(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = 'logistica/vehiculo_list.html'
    context_object_name = 'vehiculos'
    paginate_by = 10

class VehiculoDetailView(LoginRequiredMixin, DetailView):
    model = Vehiculo
    template_name = 'logistica/vehiculo_detail.html'

class VehiculoCreateView(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'logistica/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'logistica/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    template_name = 'logistica/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo_list')

# --- Carga CRUD ---
class CargaListView(LoginRequiredMixin, ListView):
    model = Carga
    template_name = 'logistica/carga_list.html'
    context_object_name = 'cargas'
    paginate_by = 10

class CargaDetailView(LoginRequiredMixin, DetailView):
    model = Carga
    template_name = 'logistica/carga_detail.html'

class CargaCreateView(LoginRequiredMixin, CreateView):
    model = Carga
    form_class = CargaForm
    template_name = 'logistica/carga_form.html'
    success_url = reverse_lazy('carga_list')

class CargaUpdateView(LoginRequiredMixin, UpdateView):
    model = Carga
    form_class = CargaForm
    template_name = 'logistica/carga_form.html'
    success_url = reverse_lazy('carga_list')

class CargaDeleteView(LoginRequiredMixin, DeleteView):
    model = Carga
    template_name = 'logistica/carga_confirm_delete.html'
    success_url = reverse_lazy('carga_list')
