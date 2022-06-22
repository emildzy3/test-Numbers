from datetime import datetime

from django.db.models import Sum, Case, When
from django.shortcuts import render
from apps.sheet.models import Order


def main_page(request):
    all_order = Order.objects.all().annotate(status=Case(When(delivery_time__gt=datetime.today(), then=True)))
    sum_price = Order.objects.all().aggregate(sum_rubl=Sum('rubles_value'), sum_dollar=Sum('dollar_value'))
    context = {
        'all_order': all_order,
        'sum_price': sum_price
    }
    return render(request, 'base.html', context)
