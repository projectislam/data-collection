import csv

# Input and output file paths
input_file = 'en_ahmedali.txt'
output_file = 'en_ahmedali.csv'

# Initialize IDs
id_counter = 1
quran_ayas_id_counter = 1

# Function to generate the formatted IDs
def format_id(counter, prefix):
    return f"{prefix}{counter:02d}"

# Read input file and write to CSV
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    csv_writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL, escapechar='\\', quotechar="'")
    
    # Write the CSV header
    csv_writer.writerow(['id', 'quran_ayas_id', 'quran_ayas_languages_code', 'text'])
    
    # Loop through each line in the input file
    for line in infile:
        line = line.strip()
        
        # Skip empty lines and metadata section
        if not line or line.startswith('#'):
            continue
        
        # Split the line by "|" to get the sura and aya info along with the text
        parts = line.split('|')
        
        if len(parts) == 3:
            sura, aya, text = parts
            
            # Generate the IDs
            id_value = format_id(id_counter, 'TQA')
            quran_ayas_id = format_id(quran_ayas_id_counter, 'QA')
            quran_ayas_languages_code = 'TLQ01'
            
            # Write the row to the CSV file
            csv_writer.writerow([id_value, quran_ayas_id, quran_ayas_languages_code, text])
            
            # Increment counters
            id_counter += 1
            quran_ayas_id_counter += 1

print(f"Conversion completed! The output file '{output_file}' has been created.")
