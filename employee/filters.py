from django_filters import rest_framework as filters
from employee.models import Employee

class EmployeeFilter(filters.FilterSet):
    designation = filters.CharFilter(
        field_name='designation',
        lookup_expr='iexact'   # case-insensitive
    )

    class Meta:
        model = Employee
        fields = ['designation']

# CODE FROM RETHAN 
'''
import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['designation']

'''