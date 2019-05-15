from django import forms
from apps.academico.models import Inscrito, Ugel, Curso

class InscritoForm(forms.ModelForm):
	class Meta:
		model = Inscrito
		fields = [
			'id',
			'nombres',
			'apellidos',
			'dni',
			'telefono',
			'direccion',
			'curso',
			'ugel',
			'beneficiario',
			'modulos_entregados',
			'asesora',
			'fecha_matricula',
			'fecha_diploma',
			'promocion',
			'descuento_actual',
			'descuento_pendiente',
			'observaciones',
			
		]

		labels = {
			'id':'Codigo',
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'dni' : 'DNI',
			'telefono' : 'Telefono',
			'direccion':'Direccion',
			'curso':'Curso',
			'ugel': 'Ugel',
			'beneficiario': 'Beneficiario',
			'modulos_entregados': 'Modulos Entregados',
			'asesora': 'Asesora',
			'fecha_matricula':'Fecha de Matricula',
			'fecha_diploma':'Fecha de Entrega de Diploma',
			'promocion':'Promoción',
			'descuento_actual':'Descuento Actual',
			'descuento_pendiente':'Decuento Pendiente',
			'observaciones':'Observaciones,'
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'dni':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'curso':forms.Select(attrs={'class':'form-control'}),
			'ugel':forms.Select(attrs={'class':'form-control'}),
			'beneficiario':forms.TextInput(attrs={'class':'form-control'}),
			'modulos_entregados':forms.Textarea(attrs={'class':'form-control'}),
			'asesora':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_matricula':forms.DateInput(attrs={'class':'form-control'}),
			'fecha_diploma':forms.DateInput(attrs={'class':'form-control'}),
			'promocion':forms.TextInput(attrs={'class':'form-control'}),
			'descuento_actual':forms.TextInput(attrs={'class':'form-control'}),
			'descuento_pendiente':forms.TextInput(attrs={'class':'form-control'}),
			'observaciones':forms.Textarea(attrs={'class':'form-control'}),
		}

class UgelForm(forms.ModelForm):
	class Meta:
		model = Ugel
		fields = [
			'id',
			'nombre',
			'director',
		]

		labels = {
			'id':'Codigo',
			'nombre': 'Ugel',
			'director':'Director',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'director':forms.TextInput(attrs={'class':'form-control'}),
		}

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = [
			'id',
			'nombre',
			'costo',
			'cant_modulos',
			'observaciones',
		]

		labels = {
			'id':'Codigo',
			'nombre': 'Curso',
			'director':'Director',
			'cant_modulos': 'Cantidad de Modulos',
			'observaciones':'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'director':forms.TextInput(attrs={'class':'form-control'}),
			'cant_modulos': forms.TextInput(attrs={'class':'form-control'}),
			'observaciones': forms.Textarea(attrs={'class':'form-control'}),
		}

