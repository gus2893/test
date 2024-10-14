import pandas as pd
from openpyxl import load_workbook
from datetime import datetime, timedelta
import random

def write_json_to_xlsm(json_data, template_path, output_path):
    """
    Write JSON data to a new worksheet in a macro-enabled Excel (.xlsm) file.
    """
    # Convert JSON data to a pandas DataFrame
    df = pd.json_normalize(json_data)

    # Load the existing macro-enabled workbook
    wb = load_workbook(template_path, keep_vba=True)

    # Create or select the DataSheet worksheet
    if "DataSheet" in wb.sheetnames:
        sheet = wb["DataSheet"]
    else:
        sheet = wb.create_sheet("DataSheet")

    # Clear existing data (optional)
    for row in sheet["A1:Z1000"]:
        for cell in row:
            cell.value = None

    # Write headers
    for col_idx, header in enumerate(df.columns, start=1):
        sheet.cell(row=1, column=col_idx, value=header)

    # Write data rows
    for row_idx, row_data in enumerate(df.values, start=2):
        for col_idx, value in enumerate(row_data, start=1):
            sheet.cell(row=row_idx, column=col_idx, value=value)

    # Save the workbook with macros intact
    wb.save(output_path)
    print(f"Data successfully written to {output_path}")

# Function to generate random integers
def random_int(min_value, max_value):
    return random.randint(min_value, max_value)

# Function to generate random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)
def generate_data(entry_count=10):
    data = []

    for _ in range(entry_count):
        entry = {
            "system_id": random_int(1000, 9999),
            "systemname": f"System {random_int(1, 100)}",
            "facility_entity_id": random_int(5000, 9999),
            "provider_name": f"Provider {random_int(1, 100)}",
            "line_of_business": f"Line {random_int(1, 5)}",
            "contract_office": f"Office {random_int(1, 10)}",
            "msc_cd": f"MSC{random_int(100, 999)}",
            "service_major": f"Service {random_int(1, 10)}",
            "repriced_claim_count": random_int(1, 1000),
            "repriced_allowed_": random_int(1000, 10000),
            "repriced_medicare_allowed": random_int(500, 8000),
            "total_allowed": random_int(2000, 15000),
            "con_office_repr_allowed": random_int(1000, 12000),
            "con_offirce_medicare_allowed": random_int(700, 9000),
            "service_begin_year_month": random_int(202301, 202312),  # YYYYMM format
            "service_end_year_month": random_int(202401, 202412),  # YYYYMM format
            "create_timestamp": random_date(datetime(2022, 1, 1), datetime(2024, 12, 31)).isoformat()
        }
        data.append(entry)

    return data

# Example usage
if __name__ == "__main__":
    # Sample JSON input
    json_data = generate_data(entry_count=1000)


    # Path to the macro-enabled Excel template
    template_path = "template_with_macros.xlsm"

    # Output path for the new Excel file
    output_path = "output_with_macros.xlsm"

    # Write JSON data to the new worksheet
    write_json_to_xlsm(json_data, template_path, output_path)
