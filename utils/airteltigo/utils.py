"""Functions for processing AirtelTigo's part of SDP reports."""

import csv

from utils.classes import Service, Dates


def process_reports():
    """Update main report with AirtelTigo services information."""

    # Read yesterday's AirtelTigo revenue report.
    with open("./input/Charges Consolidated.csv", "r") as file:
        # Use the csv.reader() function to read the contents of the file
        reader = csv.reader(file)

        # Skip first 4 rows
        for _ in range(4):
            next(reader)

        # Get all remaining rows
        rows = [row for row in reader]

        total_count = 0
        total_revenue = 0

        # Iterate over the rows of the file
        for row in rows:
            if row:
                service = _calculate_count_and_revenue(row)
                _process_main_report(service)
                total_count += service.count
                total_revenue += service.revenue

    _process_summary_report(total_count, total_revenue)


def _process_main_report(service):
    """
    Update main report with AirtelTigo service information.
    Calculate and return the count and revenue for the service.
    """

    with open(
        f"./output/SDP _{Dates.yesterdays_date_dashed}.csv",
            "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "",
                "AIRTELTIGO",
                f"{service.count}",
                f"{service.revenue}",
                f"{service.name}",
                f"{Dates.yesterdays_date_slashed}",
                f"{Dates.todays_date_slashed}",
                f"{service.short_code}",
            ]
        )


def _process_summary_report(total_count, total_revenue):
    """Update summary report."""

    # Read, modify and overwrite contents of summary report.
    with open('./output/sdp_report.txt', "r") as file:
        # read a list of lines into data
        data = file.readlines()
        data[11] = '\n'
        data[12] = f'MT AIRTELTIGO 3701 COMPARISON - {Dates.yesterdays_date_dashed_desc}\n'  # noqa
        data[13] = 'Revenue / Count\n'
        data[14] = 'nalo: <get-from-spider> / <get-from-spider>\n'
        data[15] = f'tigo: {total_revenue} / {total_count}\n'

    # and write everything back
    with open('./output/sdp_report.txt', 'w') as file:
        file.writelines(data)


def _calculate_count_and_revenue(row):
    """Update count and revenue for a service."""

    name = row[15]
    short_code = row[13]
    count = int(row[18])
    revenue = row[19]

    service = Service(name, short_code)
    service.update_count_and_revenue(count, revenue)

    return service
