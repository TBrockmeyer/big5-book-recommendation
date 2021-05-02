from django.urls import path

from . import views

urlpatterns = [
    path('employeelist/', views.EmployeeListView.as_view(template_name="./bookquistapp/employee_list.html"), name='employee_list'),
    path('employeedetail/<int:pk>/', views.EmployeeDetailView.as_view(template_name="./bookquistapp/employee_detail.html"), name='employee_detail'),
    path('employeedetail/<int:pk>/bookreco/', views.EmployeeBookrecoView.as_view(template_name="./bookquistapp/employee_bookreco.html"), name='employee_bookreco'),
]