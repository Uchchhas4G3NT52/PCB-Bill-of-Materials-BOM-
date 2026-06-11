import csv
import re
import os

def categorize_component(designator):
    """
    Extracts the alphabetical prefix from the designator and returns the component type.
    Example: 'R12' -> 'Resistor', 'C4' -> 'Capacitor'
    """
    match = re.match(r"([A-Za-z]+)", designator)
    if not match:
        return "Unknown"
    
    prefix = match.group(1).upper()
    categories = {
        'R': 'Resistor',
        'C': 'Capacitor',
        'L': 'Inductor',
        'U': 'Integrated Circuit',
        'IC': 'Integrated Circuit',
        'D': 'Diode',
        'Q': 'Transistor',
        'J': 'Connector',
        'SW': 'Switch'
    }
    return categories.get(prefix, 'Other Component')

def process_bom(input_file, output_file):
    print(f"Reading raw BOM data from {input_file}...\n")
    
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            # Normalize column headers by stripping accidental whitespace
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            cleaned_data = []
            missing_parts_flag = False

            for row in reader:
                designator = row.get('Designator', '').strip()
                value = row.get('Value', '').strip()
                footprint = row.get('Footprint', '').strip()
                mpn = row.get('PartNumber', '').strip()

                # Flag and replace missing Manufacturer Part Numbers
                if not mpn:
                    mpn = "⚠️ MISSING_MPN"
                    missing_parts_flag = True

                component_type = categorize_component(designator)

                cleaned_data.append({
                    'Type': component_type,
                    'Designator': designator,
                    'Value': value,
                    'Footprint': footprint,
                    'PartNumber': mpn
                })

    except FileNotFoundError:
        print(f"Error: Could not find {input_file}. Ensure the data folder exists.")
        return

    # Sort the BOM logically: First by Component Type, then by Value
    cleaned_data.sort(key=lambda x: (x['Type'], x['Value']))

    # Generate the formatted output file
    print(f"Writing cleaned, sorted BOM to {output_file}...")
    fieldnames = ['Type', 'Designator', 'Value', 'Footprint', 'PartNumber']
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

    print("\n--- Parsing Complete ---")
    if missing_parts_flag:
        print("ALERT: Some components are missing Manufacturer Part Numbers (MPN).")
        print("Please check the output file to see which components need verification before ordering.")

if __name__ == "__main__":
    input_csv = "data/raw_bom.csv"
    output_csv = "data/clean_bom.csv"
    
    # Ensure the data directory exists before running
    os.makedirs("data", exist_ok=True)
    
    # Execute the parser
    process_bom(input_csv, output_csv)