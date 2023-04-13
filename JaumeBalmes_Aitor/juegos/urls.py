from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('students', views.students, name='students'),
    path('teacher/<str:pk>/', views.teacher, name='teacher'),
    path('student/<str:pk>/', views.student, name='student'),
    path('user-form/', views.user_form, name='user_form'),
]
