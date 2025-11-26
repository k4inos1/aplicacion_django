from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

    # Vehiculos
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo_list'),
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculos/<int:pk>/', views.VehiculoDetailView.as_view(), name='vehiculo_detail'),
    path('vehiculos/<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculos/<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='vehiculo_delete'),

    # Cargas
    path('cargas/', views.CargaListView.as_view(), name='carga_list'),
    path('cargas/nueva/', views.CargaCreateView.as_view(), name='carga_create'),
    path('cargas/<int:pk>/', views.CargaDetailView.as_view(), name='carga_detail'),
    path('cargas/<int:pk>/editar/', views.CargaUpdateView.as_view(), name='carga_update'),
    path('cargas/<int:pk>/eliminar/', views.CargaDeleteView.as_view(), name='carga_delete'),
]
