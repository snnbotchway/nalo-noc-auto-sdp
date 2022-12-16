from datetime import datetime, timedelta
from decimal import Decimal


class Service:
    """Class for the different services."""

    def __init__(self, name, short_code):
        self.name = name
        self.count = 0
        self.revenue = 0
        self.short_code = short_code

    def update_count_and_revenue(self, count, revenue):
        """Add to the count and revenue of this service."""
        self.count += count
        # Convert revenue to two decimal places
        revenue = Decimal(revenue)
        revenue = revenue.quantize(Decimal('0.000'))
        self.revenue += revenue


class Dates:
    """Class for the different scripts."""

    # Get yesterday's date in different formats.
    yesterday = datetime.now() - timedelta(1)
    yesterdays_date_dotted = datetime.strftime(yesterday, '%d.%m.%Y')
    yesterdays_date_dashed = datetime.strftime(yesterday, '%d-%m-%Y')
    yesterdays_date_dashed_desc = datetime.strftime(yesterday, '%Y-%m-%d')
    yesterdays_date_slashed = datetime.strftime(yesterday, '%d/%m/%Y')

    """Get today's date in the format: DD/MM/YYYY"""
    today = datetime.now()
    todays_date_slashed = datetime.strftime(today, '%d/%m/%Y')
