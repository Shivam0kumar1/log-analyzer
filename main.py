import os
from log_analyzer import analyze_logs

if __name__ == '__main__':
    input_file = 'sample_logs.txt'
    output_file = 'errors.txt'

    if os.path.exists(input_file):
        analyze_logs(input_file, output_file)
        print(f"Analysis complete. Results saved to {output_file}")
    else:
        print(f"Input file {input_file} not found.")