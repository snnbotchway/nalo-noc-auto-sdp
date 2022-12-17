"""Main script for processing SDP report"""

from utils.vodafone.utils import (
    calculate_count_and_revenue as vodafone_calculate_c_and_r,
    process_main_report as vodafone_process_main_report,
    process_summary_report as vodafone_process_summary_report)
from utils.airteltigo.utils import (
    process_reports as process_airteltigo)
from utils.mtn.utils import (
    calculate_count_and_revenue as mtn_calculate_c_and_r,
    process_main_report as mtn_process_main_report,
    process_summary_report as mtn_process_summary_report)
from utils.classes import Dates, bcolors


def process_vodafone_reports():
    """Main function for processing Vodafone's part of the report."""

    print("\nProcessing Vodafone report...")

    services = vodafone_calculate_c_and_r()
    total_count, total_revenue = vodafone_process_main_report(services)
    vodafone_process_summary_report(total_count, total_revenue)

    print(f"{bcolors.green}SUCCESS!{bcolors.end}")


def process_airteltigo_reports():
    """Main function for processing AirtelTigo's part of the report."""

    print("Processing AirtelTigo report...")

    process_airteltigo()

    print(f"{bcolors.green}SUCCESS!{bcolors.end}")


def process_mtn_reports():
    """Main function for processing MTN's part of the report."""

    print("Processing MTN report...")

    services = mtn_calculate_c_and_r()
    total_count, total_revenue = mtn_process_main_report(services)
    mtn_process_summary_report(total_count, total_revenue)

    print(f"{bcolors.green}SUCCESS!{bcolors.end}")


def _print_file_not_exists_error(file_name):
    """Prints error if the specified file was not found."""

    print(
        f"{bcolors.red}\nERROR: '{file_name}' was not found in the input folder.")  # noqa
    print(f"ERROR: The process could not be completed.{bcolors.end}")
    print("\nPlease provide the file and try again.")


def process_reports():
    """Process reports with error handling."""

    try:
        process_vodafone_reports()
    except FileNotFoundError:
        _print_file_not_exists_error(
            f"Daily NALO Revenue Report {Dates.yesterdays_date_dotted}.xlsx")
        return
    try:
        process_airteltigo_reports()
    except FileNotFoundError:
        _print_file_not_exists_error("Charges Consolidated.csv")
        return
    try:
        process_mtn_reports()
    except FileNotFoundError:
        _print_file_not_exists_error("Service_based_revenue_reportNalo.csv")
        return

    print("\nPlease check the output folder for the reports.")
    print("Remember to update sdp_report.txt with data from spider!")


process_reports()
