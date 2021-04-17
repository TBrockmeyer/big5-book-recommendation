from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from bookquistapp.models import Employee

class EmployeeListView(ListView):
    model = Employee
    paginate_by = 100  # if pagination is desired
    ordering = ['employee_lastname']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_name'] = 'Fritz'
        return context

class EmployeeDetailView(DetailView):
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_name'] = Employee.objects.get(employee_id=1).employee_firstname
        return context