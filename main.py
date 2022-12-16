"""Main script for processing SDP report"""

from utils.vodafone.utils import (
    calculate_count_and_revenue as vodafone_calculate_c_and_r,
    process_main_report as vodafone_process_main_report,
    process_summary_report as vodafone_process_summary_report)
from utils.airteltigo.utils import process_reports
from utils.mtn.utils import (
    calculate_count_and_revenue as mtn_calculate_c_and_r,
    process_main_report as mtn_process_main_report,
    process_summary_report as mtn_process_summary_report)


def process_vodafone_reports():
    """Main function for processing Vodafone's part of the report."""

    print("Processing Vodafone report...")

    services = vodafone_calculate_c_and_r()
    total_count, total_revenue = vodafone_process_main_report(services)
    vodafone_process_summary_report(total_count, total_revenue)

    print("Done!")


def process_airteltigo_reports():
    """Main function for processing AirtelTigo's part of the report."""

    print("Processing AirtelTigo report...")

    process_reports()

    print("Done!")


def process_mtn_reports():
    """Main function for processing MTN's part of the report."""

    print("Processing MTN report...")

    services = mtn_calculate_c_and_r()
    total_count, total_revenue = mtn_process_main_report(services)
    mtn_process_summary_report(total_count, total_revenue)

    print("Done!")


process_vodafone_reports()
process_airteltigo_reports()
process_mtn_reports()


print("\nPlease check the output folder for the reports.")
print("Remember to update sdp_report.txt with data from spider!")
