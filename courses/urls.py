from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:program>/<int:number>/', views.get_course, name='get_course'),
    path('create/', views.CourseCreate.as_view(), name='course_create'),
    path('update/<slug:program>/<int:number>/', views.CourseUpdate.as_view(), name='course_update'),
]

