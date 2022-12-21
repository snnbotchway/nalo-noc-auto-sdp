"""Functions for processing Vodafone's part of SDP reports."""

import csv
import openpyxl
from pathlib import Path

from utils.classes import Service, Dates


def calculate_count_and_revenue():
    """Sum all counts and revenue for each service."""

    # Array for storing service objects.
    services = []

    def _exists(service_name):
        """Returns true if service exists in services array."""
        return any(service.name == service_name for service in services)

    sheet = _get_active_sheet()

    for index in range(2, sheet.max_row+1):
        name = _cell_value(sheet, "D", index).strip()
        short_code = _short_code(sheet, index)
        count = _cell_value(sheet, "G", index)
        revenue = _cell_value(sheet, "H", index)

        if not _exists(name):
            service = Service(name, short_code)
            services.append(service)
        else:
            for _service in services:
                if _service.name == name:
                    service = _service
        service.update_count_and_revenue(count, revenue)

    return services


def process_main_report(services):
    """
    Create a report file and write vodafone service information to it.
    Calculate and return the total count and revenue for Vodafone.
    """

    # Create and write to main report
    with open(
            F"./output/SDP _{Dates.yesterdays_date_dashed}.csv", "x") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "ID",
                "NETWORK",
                "COUNTS",
                "REVENUE(GHS)",
                "SERVICE",
                "REVENUE DATE",
                "CREATED ON",
                "SHORTCODE"
            ]
        )

        total_count = 0
        total_revenue = 0
        for service in services:
            writer.writerow(
                [
                    "",
                    "VODAFONE",
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


def process_comparison_report(total_count, total_revenue):
    """Create and write to comparison_report.txt(Report comparison)"""

    # Create comparison report file.
    with open("./output/comparison_report.txt", "x") as file:
        data = [None] * 16
        for index in range(16):
            data[index] = "\n"
        file.writelines(data)

    # Read, modify and overwrite contents of comparison report.
    with open('./output/comparison_report.txt', "r") as file:
        # read a list of lines into data
        data = file.readlines()
        data[0] = 'SDP REPORT\n'
        data[1] = '===================\n'
        data[2] = '\n'
        data[3] = '\n'
        data[4] = '\n'
        data[5] = '\n'
        data[6] = '\n'
        data[7] = f'MT 3701_1133 VODAFONE COMPARISON - {Dates.yesterdays_date_dashed_desc}\n'  # noqa
        data[8] = 'Revenue / Count\n'
        data[9] = 'nalo: <get-from-spider> / <get-from-spider>\n'
        data[10] = f'vodafone: {total_revenue} / {total_count}\n'

    # and write everything back
    with open('./output/comparison_report.txt', 'w') as file:
        file.writelines(data)


def _cell_value(sheet, col, row):
    """Returns the value in a cell."""
    return sheet[f"{col}{row}"].value


def _short_code(sheet, row):
    """Returns the shortcode value in a row."""
    return sheet[f"F{row}"].value


def _get_active_sheet():
    """Return active sheet from yesterday's Vodafone revenue report."""
    xlsx_file = Path(
        './input/',
        f'Daily NALO Revenue Report {Dates.todays_date_dotted}.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file)

    return wb_obj.active
