"""
- Reads a log file (like sample_logs.txt).
- Extracts only the lines that contain ERROR or WARNING.
- Skips empty lines or lines with None.
- Saves the filtered results into a new file (errors.txt).
- Adds a summary at the end (e.g., “Errors found: 3, Warnings found: 2”).

"""
import os

def analyze_logs(input_file, output_file):
    error_count=0
    warning_count=0

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()

            #skip empty or none lines
            if not line or line.lower() == 'none':
                continue

            if "ERROR" in line:
                error_count += 1
                outfile.write(line + '\n')
            elif "WARNING" in line:
                warning_count += 1
                outfile.write(line+'\n')

        outfile.write("\n---SUMMARY---\n")
        outfile.write(f"Errors found: {error_count}\n")
        outfile.write(f"Warnings found: {warning_count}\n")