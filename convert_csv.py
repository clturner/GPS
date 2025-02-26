#!/usr/bin/env python
import csv
import math

"""
Calculates new gps coordinates based on input Latitude/Longitude, Bearing and Distance
Rewrites the GPS coordinates to the csv file in the place of input Latitude/Longitude
"""

# Get user inputs
file_name = input("Enter the path to your CSV file: ")

lat_column_number = int(input("Enter the column number of Latitude: "))
lon_column_number = int(input("Enter the column number of Longitude: "))
brng_column_number = int(input("Enter the column number of Bearing: "))
distance_column_number = int(input("Enter the column number of Distance: "))

R = 6378.1  # Radius of the Earth in km

lines = []

# Read CSV file
with open(file_name, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Read the first row as headers
    lines.append(headers)   # Store headers

    for row in reader:
        try:
            # Convert values
            lat1 = math.radians(float(row[lat_column_number]))
            lon1 = math.radians(float(row[lon_column_number]))
            brng = math.radians(float(row[brng_column_number]))  # Convert bearing to radians
            d = float(row[distance_column_number]) / 1000  # Convert distance to km

            # Calculate new latitude
            lat2 = math.asin(math.sin(lat1) * math.cos(d / R) +
                             math.cos(lat1) * math.sin(d / R) * math.cos(brng))

            # Calculate new longitude
            lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d / R) * math.cos(lat1),
                                     math.cos(d / R) - math.sin(lat1) * math.sin(lat2))

            # Convert back to degrees
            row[lat_column_number] = round(math.degrees(lat2), 6)
            row[lon_column_number] = round(math.degrees(lon2), 6)
        except ValueError:
            print(f"Skipping row due to invalid data: {row}")
        
        lines.append(row)

# Write updated data back to the file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lines)

print("Updated coordinates saved successfully.")
