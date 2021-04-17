from django.urls import path

from . import views

urlpatterns = [
    path('employeelist', views.EmployeeListView.as_view(), name='employee_list'),
    path('employeedetail/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
]