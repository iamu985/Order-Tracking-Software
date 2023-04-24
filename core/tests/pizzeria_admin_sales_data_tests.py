import pytest

from pizzeria_admin.sales_data import (
    get_daily_data,
    get_weekly_data,
    get_monthly_data,
    get_yearly_data,

    get_daily_sales,
    get_weekly_sales,
    get_monthly_sales,
    get_yearly_sales
)


@pytest.mark.django_db
class TestSalesData:
    def test_get_weekly_sales(self, weekly_orders):
        expected_total_sales = 70
        assert get_weekly_data() == expected_total_sales
