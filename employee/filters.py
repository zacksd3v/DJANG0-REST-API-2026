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
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact') # get all record by designation
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains') # get all record by name
    id = django_RangeFilter(field_name='id') # get all record by Range of ID
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From RNG ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To RNG ID')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset

'''