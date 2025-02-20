import django_filters


from .models import Product


class ProductCustomFilter(django_filters.FilterSet):

    price_range = django_filters.RangeFilter(field_name="price")

    class Meta:
        model = Product
        fields= ["popularity_score"]