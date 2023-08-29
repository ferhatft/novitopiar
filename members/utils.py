from django.db.models import Q
from .models import Organization

def filter_organizations(request):
    queryset = Organization.objects.all()
    
    # Extracting parameters from the request
    name = request.GET.get('name', None)
    org_type = request.GET.getlist('org_type', None)
    country = request.GET.get('country', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    min_employee_count = request.GET.get('min_employee_count', None)
    max_employee_count = request.GET.get('max_employee_count', None)

    # Filtering
    if name:
        queryset = queryset.filter(name__icontains=name)

    if org_type:
        queryset = queryset.filter(org_type__in=org_type)

    if country:
        queryset = queryset.filter(country=country)

    if start_date and end_date:
        queryset = queryset.filter(foundation_date__range=[start_date, end_date])

    if min_employee_count:
        queryset = queryset.filter(employee_count__gte=min_employee_count)
        
    if max_employee_count:
        queryset = queryset.filter(employee_count__lte=max_employee_count)

    return queryset
