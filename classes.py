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
        # print("initial revenue:", revenue)
        revenue = Decimal(revenue)
        # print("decimal revenue:", revenue)
        revenue = revenue.quantize(Decimal('0.00'))
        # print("revenue after quantize:", revenue)
        self.revenue += revenue
        # print("self.revenue", revenue)
        return self.count, self.revenue
