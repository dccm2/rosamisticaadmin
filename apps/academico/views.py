from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.academico.forms import InscritoForm, UgelForm, CursoForm
from apps.academico.models import Inscrito, Ugel, Curso

from django.views.generic import ListView
# Create your views here.
def academico(request):
	return render(request, 'academico/index.html')


def inscrito_view(request):
	if request.method == 'POST':
		form = InscritoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('inscrito')
	else:
		form = InscritoForm()

	return render (request, 'academico/inscrito_form.html',{'form':form})


def inscrito_list(request):
	inscrito = Inscrito.objects.all().order_by('id')
	contexto = {'inscritos': inscrito}
	return render (request, 'academico/inscrito.html',contexto)


def inscrito_edit(request, id_inscrito):
	inscrito = Inscrito.objects.get(id = id_inscrito)
	if request.method == 'GET':
		form = InscritoForm(instance=inscrito)
	else:
		form = InscritoForm(request.POST, instance=inscrito)
		if form.is_valid():
			form.save()
		return redirect('inscrito')
	return render(request, 'academico/inscrito_form.html',{'form':form})

def inscrito_delete(request,id_inscrito):
	inscrito = Inscrito.objects.get(id=id_inscrito)
	if request.method=='POST':
		inscrito.delete()
		return redirect('inscrito')
	return render(request, 'academico/inscrito_del.html',{'inscrito': inscrito})


def ugel_view(request):
	if request.method == 'POST':
		form = UgelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('academico')
	else:
		form = UgelForm()

	return render (request, 'academico/ugel_form.html',{'form':form})


def ugel_list(request):
	ugel = Ugel.objects.all().order_by('id')
	contexto = {'ugels': ugel}
	return render (request, 'academico/ugel.html',contexto)


def ugel_edit(request, id_ugel):
	ugel = Ugel.objects.get(id = id_ugel)
	if request.method == 'GET':
		form = UgelForm(instance=ugel)
	else:
		form = UgelForm(request.POST, instance=ugel)
		if form.is_valid():
			form.save()
		return redirect('ugel')
	return render(request, 'academico/ugel_form.html',{'form':form})

def ugel_delete(request,id_ugel):
	ugel = Ugel.objects.get(id=id_inscrito)
	if request.method=='POST':
		ugel.delete()
		return redirect('ugel')
	return render(request, 'academico/ugel_del.html',{'ugel': ugel})

def curso_view(request):
	if request.method == 'POST':
		form = CursoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('academico')
	else:
		form = CursoForm()

	return render (request, 'academico/curso_form.html',{'form':form})


def curso_list(request):
	curso = Curso.objects.all().order_by('id')
	contexto = {'cursos': curso}
	return render (request, 'academico/curso.html',contexto)


def curso_edit(request, id_curso):
	curso = Curso.objects.get(id = id_curso)
	if request.method == 'GET':
		form = CursoForm(instance=curso)
	else:
		form = CursoForm(request.POST, instance=curso)
		if form.is_valid():
			form.save()
		return redirect('curso')
	return render(request, 'academico/curso_form.html',{'form':form})

def curso_delete(request,id_curso):
	curso = Curso.objects.get(id=id_curso)
	if request.method=='POST':
		curso.delete()
		return redirect('curso')
	return render(request, 'academico/curso_del.html',{'curso': curso})

"""def matricula_view(request):
	if request.method == 'POST':
		form = MatriculaForm(request.POST)
		if form.is_valid():
			form.status=True 
			form.save()
		return redirect('matricula')
	else:
		form = MatriculaForm()

	return render (request, 'academico/matricula_form.html',{'form':form})


def matricula_list(request):
	matricula = Matricula.objects.all().order_by('id')
	contexto = {'matriculas': matricula}
	return render (request, 'academico/matricula.html',contexto)


def matricula_edit(request, id_matricula):
	matricula = Matricula.objects.get(id = id_matricula)
	if request.method == 'GET':
		form = MatriculaForm(instance=matricula)
	else:
		form = MatriculaForm(request.POST, instance=matricula)
		if form.is_valid():
			form.save()
		return redirect('matricula')
	return render(request, 'academico/matricula_form.html',{'form':form})

def matricula_delete(request,id_matricula):
	matricula = Matricula.objects.get(id=id_matricula)
	if request.method=='POST':
		matricula.delete()
		return redirect('matricula')
	return render(request, 'academico/matricula_del.html',{'matricula': matricula})"""

