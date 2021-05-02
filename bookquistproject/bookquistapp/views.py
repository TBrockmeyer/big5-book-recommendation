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
        employee_list = []
        employee_objects = Employee.objects.all()
        for eo in employee_objects:
            employee_list.append({"pk": str(eo.pk), "employee_id": str(eo.employee_id), "employee_firstname": eo.employee_firstname, "employee_lastname": eo.employee_lastname, "employee_selfperception_text": eo.employee_selfperception_text})
        context["employee_list"] = employee_list
        return context

class EmployeeDetailView(DetailView):
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_list = []
        employee_objects = Employee.objects.all().filter(employee_id=self.kwargs["pk"])
        for eo in employee_objects:
            employee_list.append({"pk": str(eo.pk), "employee_id": str(eo.employee_id), "employee_firstname": eo.employee_firstname, "employee_lastname": eo.employee_lastname, "employee_selfperception_text": eo.employee_selfperception_text})
        context["employee_list"] = employee_list
        return context
