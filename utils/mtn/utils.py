"""Functions for processing MTN's part of SDP reports."""

import csv

from utils.classes import Service, Dates


def calculate_count_and_revenue():
    """Sum all counts and revenue for each service."""

    services = []

    def _exists(service_name):
        """Returns true if service exists in services array."""
        return any(service.name == service_name for service in services)

    # Read yesterday's MTN revenue report.
    with open("./input/Service_based_revenue_reportNalo.csv", "r") as file:
        # Use the csv.reader() function to read the contents of the file
        reader = csv.reader(file)

        # Skip first row
        next(reader)

        rows = [row for row in reader]

        # Iterate over the rows of the file
        for row in rows:
            if row and Dates.yesterdays_date_dashed_desc in row[1]:
                name = row[7]
                short_code = row[9]
                count = int(row[20])
                revenue = row[19]

                if not _exists(name):
                    service = Service(name, short_code)
                    services.append(service)
                service.update_count_and_revenue(count, revenue)

    return services


def process_main_report(services):
    """
    Append MTN service information to end of main report.
    Calculate and return the total count and revenue for MTN.
    """

    with open(
            f"./output/SDP _{Dates.yesterdays_date_dashed}.csv", "a") as file:
        writer = csv.writer(file)

        total_count = 0
        total_revenue = 0
        for service in services:
            writer.writerow(
                [
                    "",
                    "MTN",
                    f"{service.count}",
                    f"{service.revenue}",
                    f"{service.name}",
                    f"{Dates.yesterdays_date_slashed}",
                    f"{Dates.todays_date_slashed}",
                    f"{service.short_code}",
                ]
            )
            total_count += service.count
            total_revenue += service.revenue

    return total_count, total_revenue


def process_summary_report(total_count, total_revenue):
    # Read, modify and overwrite contents of summary report.

    with open('./output/sdp_report.txt', "r") as file:
        # read a list of lines into data
        data = file.readlines()
        data[2] = f'MT 3701 MTN COMPARISON - {Dates.yesterdays_date_dashed_desc}\n'  # noqa
        data[3] = 'Revenue / Count\n'
        data[4] = 'nalo: <get-from-spider> / <get-from-spider>\n'
        data[5] = f'madapi: {total_revenue} / {total_count}\n'
        data[6] = '\n'

    # and write everything back
    with open('./output/sdp_report.txt', 'w') as file:
        file.writelines(data)
