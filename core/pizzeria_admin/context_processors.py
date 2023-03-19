import logging
from django.conf import settings
from .utils import (get_daily_data,
                    get_weekly_data,
                    get_monthly_data,
                    get_yearly_data)

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
