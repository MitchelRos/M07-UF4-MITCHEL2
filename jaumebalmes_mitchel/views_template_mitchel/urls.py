from django.urls import path
from . import views
from django import views
from views_template_mitchel import views

# se que puedo tenr un uls.py en app pero he querido aprovechar este, ya que no me decian lo contrario
urlpatterns = [
    path('clases-form/', views.clases_form, name='clases_form'),
    path('students/', views.Student, name='student'),
    path('students/student/<int:student_id>/', views.student_info, name='student_info'),
    path('teachers/', views.Teacher, name='teacher'),
    path('teachers/teacher/<int:teacher_id>/', views.teacher_info, name='teacher_info'),
]