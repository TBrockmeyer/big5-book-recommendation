from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='employee_list'),
]