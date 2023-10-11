from django.urls import path
from . import views


urlpatterns = [
    path("student/<int:pk>",views.student_detail,name="student_detail"),
    path("student/",views.student_list,name="student_list"),
]