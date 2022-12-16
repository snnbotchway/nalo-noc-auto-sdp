"""Generates SDP report for MTN"""

import csv
from datetime import datetime, timedelta

from services import Service


print("Generating MTN report...")

"""Get yesterday's date in different formats."""
yesterday = datetime.now() - timedelta(1)
yesterdays_date_dashed = datetime.strftime(yesterday, '%d-%m-%Y')
yesterdays_date_dashed_desc = datetime.strftime(yesterday, '%Y-%m-%d')
yesterdays_date_slashed = datetime.strftime(yesterday, '%d/%m/%Y')

"""Get today's date in the format: DD/MM/YYYY"""
today = datetime.now()
todays_date_slashed = datetime.strftime(today, '%d/%m/%Y')

services = []


def _exists(service_name):
    """Returns true if service exists in services array."""
    for service in services:
        if service_name in service.name:
            return True
    return False


"""Read yesterday's MTN revenue report."""
with open("./input/Service_based_revenue_reportNalo.csv", "r") as file:
    # Use the csv.reader() function to read the contents of the file
    reader = csv.reader(file)

    # Skip first row
    next(reader)

    rows = [row for row in reader]

    total_count = 0
    total_revenue = 0

    # Iterate over the rows of the file
    for row in rows:
        if row and yesterdays_date_dashed_desc in row[1]:
            name = row[7]
            short_code = row[9]
            count = int(row[20])
            revenue = row[19]

            if not _exists(name):
                service = Service(name, short_code)
                services.append(service)
            service.update_count_and_revenue(count, revenue)

# Append MTN service information to end of report file.
with open(
        f"./output/SDP _{yesterdays_date_dashed}.csv", "a") as file:
    writer = csv.writer(file)

    for service in services:
        writer.writerow(
            [
                "",
                "MTN",
                f"{service.count}",
                f"{service.revenue}",
                f"{service.name}",
                f"{yesterdays_date_slashed}",
                f"{todays_date_slashed}",
                f"{service.short_code}",
            ]
        )
        total_count += service.count
        total_revenue += service.revenue
print("Done!")

# Update report summary
with open('./output/sdp_report.txt', "r") as file:
    # read a list of lines into data
    data = file.readlines()
    data[2] = f'MT 3701 MTN COMPARISON - {yesterdays_date_dashed_desc}\n'  # noqa
    data[3] = 'Revenue / Count\n'
    data[4] = 'nalo: <get-from-spider> / <get-from-spider>\n'
    data[5] = f'madapi: {total_revenue} / {total_count}\n'
    data[6] = '\n'

# and write everything back
with open('./output/sdp_report.txt', 'w') as file:
    file.writelines(data)

print("\nPlease check the output folder for the reports.")
print("Remember to update sdp_report.txt with data from spider!")
