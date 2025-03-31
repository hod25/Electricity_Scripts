# get a path of csv from electric company with the following format
# Make a new csv in the same path with the total power consumption(date, day, hour, total):
# "07/02/2024","09:00",2.994
# "07/02/2024","09:15",2.245
# "07/02/2024","09:30",.531
# "07/02/2024","09:45",.824
# "07/02/2024","10:00",1.034
# "07/02/2024","10:15",.689
# "07/02/2024","10:30",.507
# "07/02/2024","10:45",.401

import csv
from collections import defaultdict
from datetime import datetime
import os
# Define a defaultdict to store sums for each hour
hourly_sums = defaultdict(float)

# Ask the user for the input CSV file path
input_file = input("Enter the path to the input CSV file: ")


# Read the CSV file
with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row if present
    for row in reader:
        date_str, time_str, value_str = row
        # Combine date and time strings into a datetime object
        datetime_obj = datetime.strptime(date_str + ' ' + time_str, '%d/%m/%Y %H:%M')
        # Round down to the nearest hour
        hour = datetime_obj.replace(minute=0, second=0, microsecond=0)
        # Convert value to float
        value = float(value_str)
        # Add value to the corresponding hour sum
        hourly_sums[hour] += value

    # Construct the output file path in the same directory as the script file
    script_dir = os.path.dirname(__file__)
    script_name = os.path.splitext(os.path.basename(__file__))[0]  # Get script's filename without extension
    output_file = os.path.join(script_dir, script_name + '.csv')  # Add new extension


with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Day', 'Hour', 'Total'])  # Write header
    for hour, total in hourly_sums.items():  # Iterate over dictionary items directly
        writer.writerow([hour.strftime('%d/%m/%Y'), hour.strftime('%A'), hour.strftime('%H:%M'), total])

print(f"Hourly sums written to {output_file}")
