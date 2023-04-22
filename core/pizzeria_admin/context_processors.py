import datetime
import logging

from django.conf import settings

from billing.models import Order

from .utils import (get_daily_data, get_monthly_data, get_present_date,
                    get_weekly_data, get_yearly_data, get_total_sales_by_orders,
                    get_present_month, get_present_year)

LOG_DIR = settings.BASE_DIR / 'logs'
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': f'{LOG_DIR}/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})


logger = logging.getLogger(__name__)


def get_chart_data(request):
    # Returns a dictionary containing the labels and data
    # for the charts
    return {
        'daily_label': get_daily_data()[0],
        'daily_data': get_daily_data()[1],
        'weekly_label': get_weekly_data()[0],
        'weekly_data': get_weekly_data()[1],
        'monthly_label': get_monthly_data()[0],
        'monthly_data': get_monthly_data()[1],
        'yearly_label': get_yearly_data()[0],
        'yearly_data': get_yearly_data()[1],
    }


def get_daily_sales(request):
    # Returns a dictionary containing the daily sales
    today = get_present_date()
    orders = Order.objects.filter(ordered_on__day=today.day)
    total_sales = 0
    for order in orders:
        total_sales += order.get_total_price()
    return {
        'daily_sales': total_sales,
    }


def get_weekly_sales(request):
    # Returns a dictionary containing the weekly sales
    today = get_present_date()
    orders = Order.objects.filter(ordered_on__week_day=today.weekday())
    total_sales = 0
    for order in orders:
        total_sales += order.get_total_price()
    return {
        'weekly_sales': total_sales,
    }


def get_monthly_sales(request):
    # Returns a dictionary containing total monthly sales amount
    month = get_present_month()
    orders = Order.objects.filter(ordered_on__month=month)
    total_sales = get_total_sales_by_orders(orders)
    return {
        'monthly_sales': total_sales,
    }


def get_yearly_sales(request):
    # Returns a dictionary containing total yearly sales amount
    year = get_present_year()
    orders = Order.objects.filter(ordered_on__year=year)
    total_sales = get_total_sales_by_orders(orders)
    return {
        'yearly_sales': total_sales,
    }