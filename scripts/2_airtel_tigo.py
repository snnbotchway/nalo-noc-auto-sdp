"""Generates SDP report for AirtelTigo"""

import csv
from datetime import datetime, timedelta

from services import Service


print("Generating AirtelTigo report...")

"""Get yesterday's date in different formats."""
yesterday = datetime.now() - timedelta(1)
yesterdays_date_dashed = datetime.strftime(yesterday, '%d-%m-%Y')
yesterdays_date_dashed_desc = datetime.strftime(yesterday, '%Y-%m-%d')
yesterdays_date_slashed = datetime.strftime(yesterday, '%d/%m/%Y')

"""Get today's date in the format: DD/MM/YYYY"""
today = datetime.now()
todays_date_slashed = datetime.strftime(today, '%d/%m/%Y')


"""Read yesterday's AirtelTigo revenue report."""
with open("./input/Charges Consolidated.csv", "r") as file:
    # Use the csv.reader() function to read the contents of the file
    reader = csv.reader(file)

    # Skip first 4 rows
    for _ in range(4):
        next(reader)

    rows = [row for row in reader]

    total_count = 0
    total_revenue = 0

    # Iterate over the rows of the file
    for row in rows:
        if row:
            name = row[15]
            short_code = row[13]
            count = int(row[18])
            revenue = row[19]

            service = Service(name, short_code)
            service.update_count_and_revenue(count, revenue)

            # Append AirtelTigo service information to end of report file.
            with open(
                f"./output/SDP _{yesterdays_date_dashed}.csv",
                    "a") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "",
                        "AIRTELTIGO",
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
    data[11] = '\n'
    data[12] = f'MT AIRTELTIGO 3701 COMPARISON - {yesterdays_date_dashed_desc}\n'  # noqa
    data[13] = 'Revenue / Count\n'
    data[14] = 'nalo: <get-from-spider> / <get-from-spider>\n'
    data[15] = f'tigo: {total_revenue} / {total_count}\n'

# and write everything back
with open('./output/sdp_report.txt', 'w') as file:
    file.writelines(data)
