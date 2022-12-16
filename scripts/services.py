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
