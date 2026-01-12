from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailsView),
    # class Views
    path('employes/', views.Employees.as_view()),
    path('employes/<int:pk>/', views.EmployeeDetails.as_view())
]