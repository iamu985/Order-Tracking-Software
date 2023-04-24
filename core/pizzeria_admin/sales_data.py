import logging
from django.conf import settings
from billing.models import Order

from .utils import (
    get_present_date,
    get_present_day,
    get_present_year,
    get_present_month,
    generate_labels_for_month,
    get_total_sales_by_orders,
    make_new_year_range,

)
from time import perf_counter


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
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*2,
            'backupCount': 10,
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


def get_daily_data():
    # Returns a tuple containing the labels and data
    # for the daily chart
    logger.info('Function Name: get_daily_data')
    start_time = perf_counter()
    month = get_present_month()
    logger.debug(f'Present Month: {month}')
    orders_by_month = Order.objects.filter(ordered_on__month=month)
    label = [i for i in generate_labels_for_month(month)]
    data = [get_total_sales_by_orders(orders_by_month.filter(ordered_on__day=i))
            for i in range(1, 31)]
    logger.info(f'Execution Time: {perf_counter() - start_time}')
    return label, data


def get_weekly_data():
    # Returns a tuple containing the labels and data
    # for the weekly chart
    logger.info('Function Name: get_weekly_data')
    start_time = perf_counter()
    month = get_present_month()
    orders_by_month = Order.objects.filter(ordered_on__month=month)
    label = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']
    data = [get_total_sales_by_orders(orders_by_month.filter(ordered_on__week_day=i))
            for i in range(1, 8)]
    logger.info(f'Execution Time: {perf_counter() - start_time}')
    return label, data


def get_monthly_data():
    # Returns a tuple containing the labels and data
    # for the monthly chart
    logger.info('Function Name: get_monthly_data')
    start_time = perf_counter()
    orders = Order.objects.all()
    label = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    data = [get_total_sales_by_orders(orders.filter(
        ordered_on__month=i)) for i in range(1, 13)]
    logger.info(f'Time Execution: {perf_counter() - start_time}')
    return label, data


def get_yearly_data():
    # Returns a tuple containing the labels and data
    # for the yearly chart
    logger.info('Function Name: get_yearly_data')
    start_time = perf_counter()
    orders = Order.objects.all()
    label = list(make_new_year_range())
    data = [get_total_sales_by_orders(
        orders.filter(ordered_on__year=i)) for i in label]
    logger.info(f"Execution Time: {perf_counter() - start_time}")
    return label, data


def get_daily_sales():
    # Returns a dictionary containing the daily sales
    logger.info('Function Name: get_daily_sales')
    start_time = perf_counter()
    day = get_present_date().day
    orders = Order.objects.filter(ordered_on__day=day)
    total_sales = 0
    for order in orders:
        total_sales += order.get_total_price()
    logger.info(f"Execution Time: {perf_counter() - start_time}")
    return total_sales


def get_weekly_sales(*args, **kwargs):
    logger.info('Function Name: get_weekly_sales')
    start_time = perf_counter()
    week = get_present_date().weekday() + 1
    total_sales = 0
    if kwargs.get('test'):
        week = kwargs.get('week')
    for week_index in range(1, week):
        order = Order.objects.filter(ordered_on__week_day=week_index - 1)
        total_sales += order.get_total_price()
    logger.info(f'Execution Time: {perf_counter() - start_time}')
    return total_sales


def get_monthly_sales():
    logger.info('Function Name: get_monthly_sales')
    start_time = perf_counter()
    month = get_present_month()
    orders = Order.objects.filter(ordered_on__month=month)
    total_sales = 0
    for order in orders:
        total_sales += order.get_total_price()
    logger.info(f'Execution Time: {perf_counter() - start_time}')
    return total_sales


def get_yearly_sales():
    logger.info('Function Name: get_yearly_sales')
    start_time = perf_counter()
    year = get_present_year()
    orders = Order.objects.filter(ordered_on__year=year)
    total_sales = get_total_sales_by_orders(orders)
    logger.info(f'Execution Time: {perf_counter() - start_time}')
    return total_sales
