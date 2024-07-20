#!/usr/bin/python3

import sys
import re
from collections import defaultdict

# Regular expression to match the input format
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>.*?)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)')

# Initialize metrics
total_file_size = 0
status_code_counts = defaultdict(int)
lines_processed = 0

def print_stats():
    """Print the statistics."""
    print(f"Total file size: File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")

try:
    for line in sys.stdin:
        # Match the line with the regex pattern
        match = log_pattern.match(line)
        if match:
            lines_processed += 1
            status_code = int(match.group('status'))
            file_size = int(match.group('size'))

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1

        # Print statistics after every 10 lines
        if lines_processed % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()
    sys.exit()

# Print final statistics if the input ends naturally
print_stats()
