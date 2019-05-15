from django.urls import path
from . import views

urlpatterns = [
	path('',views.academico, name = 'academico'),
	path('nuevoinscrito/',views.inscrito_view, name = 'nuevoinscrito'),
	path('inscrito/',views.inscrito_list, name = 'inscrito'),
	path('editarinscrito/<int:id_inscrito>/',views.inscrito_edit, name = 'inscrito_editar'),
	path('eliminarinscrito/<int:id_inscrito>/',views.inscrito_delete, name = 'inscrito_eliminar'),
	path('nuevaugel/',views.ugel_view, name = 'nuevaugel'),
	path('ugel/',views.ugel_list, name = 'ugel'),
	path('editarugel/<int:id_ugel>/',views.ugel_edit, name = 'ugel_editar'),
	path('eliminarugel/<int:id_ugel>/',views.ugel_delete, name = 'ugel_eliminar'),
	path('nuevocurso/',views.curso_view, name = 'nuevocurso'),
	path('curso/',views.curso_list, name = 'curso'),
	path('editarcurso/<int:id_curso>/',views.curso_edit, name = 'curso_editar'),
	path('eliminarcurso/<int:id_curso>/',views.curso_delete, name = 'curso_eliminar'),
	
]
