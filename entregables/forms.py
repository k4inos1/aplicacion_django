from django import forms
from .models import Vehiculo, Operario, Faena, Mantencion, RegistroIncidente

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'tipo', 'marca', 'modelo', 'año', 'estado', 'horas_uso', 'capacidad_carga', 'fecha_adquisicion', 'observaciones']
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABCD-12'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'horas_uso': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacidad_carga': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_patente(self):
        patente = self.cleaned_data['patente'].upper()
        return patente

class OperarioForm(forms.ModelForm):
    class Meta:
        model = Operario
        fields = ['rut', 'nombre', 'rol', 'licencia', 'telefono', 'fecha_ingreso', 'activo']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345678-9'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
            'licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        if not Operario.validar_rut(rut):
            raise forms.ValidationError("El RUT ingresado no es válido.")
        return rut
