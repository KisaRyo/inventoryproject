import django_filters
from .models import *

class CaseInsensitiveCharFilter(django_filters.CharFilter):
    def filter(self, queryset, value):
        if value:
            # Perform case-insensitive filtering
            return queryset.filter(**{f'{self.field_name}__icontains': value})
        return queryset

class ProductFilter(django_filters.FilterSet):
    name = CaseInsensitiveCharFilter(field_name='name', label='Name')
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'status']