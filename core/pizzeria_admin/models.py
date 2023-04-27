from django.db import models


class StatisticsBookeeping(models.Model):
    daily_data = models.BigIntegerField()
    weekly_data = models.BigIntegerField()
    monthly_data = models.BigIntegerField()
    yearly_data = models.BigIntegerField()

    def get_daily_data(self):
        return self.daily_data

    def get_weekly_data(self):
        return self.weekly_data

    def get_monthly_data(self):
        return self.monthly_data

    def get_yearly_data(self):
        return self.yearly_data

    def __str__(self):
        return f"{self.daily_data} | {self.weekly_data} | {self.monthly_data} | {self.yearly_data}"
