from django.shortcuts import render

from django.views.generic.list import ListView

from bookquistapp.models import Employee

class EmployeesListView(ListView):
    model = Employee
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_name'] = 'Fritz'
        return context