"""Functions for processing Vodafone's part of SDP reports."""

import csv
import openpyxl
from pathlib import Path

from utils.classes import Service, Dates


def calculate_count_and_revenue():
    """Sum all counts and revenue for each service."""

    def _exists(service_name):
        """Returns true if service exists in services array."""
        return any(service.name == service_name for service in services)

    # Array for storing service objects.
    services = []

    sheet = _get_active_sheet()

    for index in range(2, sheet.max_row+1):
        if "Accounting" in _cell_value(sheet, "D", index):
            if not _exists("Accounting"):
                accounting = Service("Accounting", _short_code(sheet, index))
                services.append(accounting)
            _update_count_and_revenue(sheet, index, accounting)

        elif "Banking and Finance" in _cell_value(sheet, "D", index):
            if not _exists("Banking and Finance"):
                banking_and_finance = Service(
                    "Banking and Finance", _short_code(sheet, index))
                services.append(banking_and_finance)
            _update_count_and_revenue(sheet, index, banking_and_finance)

        elif "Customer Service" in _cell_value(sheet, "D", index):
            if not _exists("Customer Service"):
                customer_service = Service(
                    "Customer Service", _short_code(sheet, index))
                services.append(customer_service)
            _update_count_and_revenue(sheet, index, customer_service)

        elif "Devotional Tips" in _cell_value(sheet, "D", index):
            if not _exists("Devotional Tips"):
                devotional_tips = Service(
                    "Devotional Tips", _short_code(sheet, index))
                services.append(devotional_tips)
            _update_count_and_revenue(sheet, index, devotional_tips)

        elif "Engineering Jobs" in _cell_value(sheet, "D", index):
            if not _exists("Engineering Jobs"):
                engineering_jobs = Service(
                    "Engineering Jobs", _short_code(sheet, index))
                services.append(engineering_jobs)
            _update_count_and_revenue(sheet, index, engineering_jobs)

        elif "Entertainment news" in _cell_value(sheet, "D", index):
            if not _exists("Entertainment news"):
                entertainment_news = Service(
                    "Entertainment news", _short_code(sheet, index))
                services.append(entertainment_news)
            _update_count_and_revenue(sheet, index, entertainment_news)

        elif "Fashion tips" in _cell_value(sheet, "D", index):
            if not _exists("Fashion tips"):
                fashion_tips = Service(
                    "Fashion tips", _short_code(sheet, index))
                services.append(fashion_tips)
            _update_count_and_revenue(sheet, index, fashion_tips)

        elif "GameZmania Daily" in _cell_value(sheet, "D", index):
            if not _exists("GameZmania Daily"):
                gamezmania_daily = Service(
                    "GameZmania Daily", _short_code(sheet, index))
                services.append(gamezmania_daily)
            _update_count_and_revenue(sheet, index, gamezmania_daily)

        elif "Information Technology Jobs" in _cell_value(sheet, "D", index):
            if not _exists("Information Technology Jobs"):
                information_technology_jobs = Service(
                    "Information Technology Jobs", _short_code(sheet, index))
                services.append(information_technology_jobs)
            _update_count_and_revenue(
                sheet, index, information_technology_jobs)

        elif "Laugh it out" in _cell_value(sheet, "D", index):
            if not _exists("Laugh it out"):
                laugh_it_out = Service(
                    "Laugh it out", _short_code(sheet, index))
                services.append(laugh_it_out)
            _update_count_and_revenue(sheet, index, laugh_it_out)

        elif "Legal" in _cell_value(sheet, "D", index):
            if not _exists("Legal"):
                legal = Service("Legal", _short_code(sheet, index))
                services.append(legal)
            _update_count_and_revenue(sheet, index, legal)

        elif "MakeULaugh Daily" in _cell_value(sheet, "D", index):
            if not _exists("MakeULaugh Daily"):
                makeulaugh_daily = Service(
                    "MakeULaugh Daily", _short_code(sheet, index))
                services.append(makeulaugh_daily)
            _update_count_and_revenue(sheet, index, makeulaugh_daily)

        elif "Marriage tips" in _cell_value(sheet, "D", index):
            if not _exists("Marriage tips"):
                marriage_tips = Service(
                    "Marriage tips", _short_code(sheet, index))
                services.append(marriage_tips)
            _update_count_and_revenue(sheet, index, marriage_tips)

        elif "Movie" in _cell_value(sheet, "D", index):
            if not _exists("Movie"):
                movie = Service("Movie", _short_code(sheet, index))
                services.append(movie)
            _update_count_and_revenue(sheet, index, movie)

        elif "Pharmaceutical" in _cell_value(sheet, "D", index):
            if not _exists("Pharmaceutical"):
                pharmaceutical = Service(
                    "Pharmaceutical", _short_code(sheet, index))
                services.append(pharmaceutical)
            _update_count_and_revenue(sheet, index, pharmaceutical)

        elif "Sales" in _cell_value(sheet, "D", index):
            if not _exists("Sales"):
                sales = Service("Sales", _short_code(sheet, index))
                services.append(sales)
            _update_count_and_revenue(sheet, index, sales)

        elif "Telecommunications" in _cell_value(sheet, "D", index):
            if not _exists("Telecommunications"):
                telecommunications = Service(
                    "Telecommunications", _short_code(sheet, index))
                services.append(telecommunications)
            _update_count_and_revenue(sheet, index, telecommunications)

        elif "Transportation" in _cell_value(sheet, "D", index):
            if not _exists("Transportation"):
                transportation = Service(
                    "Transportation", _short_code(sheet, index))
                services.append(transportation)
            _update_count_and_revenue(sheet, index, transportation)

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


def _update_count_and_revenue(sheet, index, service):
    """Add to count and revenue of specified service."""
    count = _cell_value(sheet, "G", index)
    revenue = _cell_value(sheet, "H", index)
    service.update_count_and_revenue(count, revenue)


def _get_active_sheet():
    """Return active sheet from yesterday's Vodafone revenue report."""
    xlsx_file = Path(
        './input/',
        f'Daily NALO Revenue Report {Dates.todays_date_dotted}.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file)

    return wb_obj.active
