import django_filters
from django_filters import RangeFilter
from .models import ListingAppliances


class FilterDemo(django_filters.FilterSet):
    price = RangeFilter()

    class Meta:
        model = ListingAppliances
        fields = ['appliance_type', 'price']
