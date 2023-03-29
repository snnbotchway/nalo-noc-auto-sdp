# nalo-noc-auto-sdp

Automatic SDP report generation.

## Installation

1. `git clone https://github.com/snnbotchway/nalo-noc-auto-sdp.git`

2. `cd nalo-noc-auto-sdp`

3. `pip install --upgrade pip`

4. `pip install openpyxl`

## Usage

1. Place the 3 files required for the report generation in the input folder.

2. Ensure the Vodafone file's name is in the format `Daily NALO Revenue Report DD.MM.YYY.xlsx`.

3. Ensure the AirtelTigo file's name is `Charges Consolidated.csv`.

4. Ensure the MTN file's name is `Service_based_revenue_reportNalo.csv`.

5. Run `bash process_reports.sh`.

6. The report along with its comparison should appear in the output folder.

7. Complete the comparison with data from spider.
