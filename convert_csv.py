#!/usr/bin/env python

"""
Calculates new gps coordinates based on input Latitude/Longitude, Bearing and Distance
Rewrites the GPS coordinates to the csv file in the place of input Latitude/Longitude
"""

import csv
import math
import sys

file_name = input("enter the name, or path to, your csv file and press return -> ")

lat_column_number = input("enter the column number of Latitude in your csv file and press return -> ")
converted_lat_column_number = int(lat_column_number)

lon_column_number = input("enter the column number of Longitude in your csv file and press return -> ")
converted_lon_column_number = int(lon_column_number)

brng_column_number = input("enter the column number of Bearing in your csv file and press return -> ")
converted_brng_column_number = int(brng_column_number)

distance_column_number = input("enter the column number of Distance in your csv file and press return -> ")
converted_distance_column_number = int(distance_column_number)

R = 6378.1 #Radius of the Earth
lines = [[]]
with open(file_name, 'rU') as csvfile:
    reader = csv.reader(csvfile)

    for i, row in enumerate(reader):
        if i is 0:
            lines.append(row)
        if i is not 0:

            converted_lat = float(row[converted_lat_column_number])
            converted_long = float(row[converted_lon_column_number])
            converted_brng = float(row[converted_brng_column_number])
            converted_d = float(row[converted_distance_column_number])

            converted_d = converted_d/1000

            lat1 = math.radians(converted_lat) #Current lat point converted to radians

            lon1 = math.radians(converted_long) #Current long point converted to radians

            #Do Trigonometry to find new Latitude
            lat2 = math.asin( math.sin(lat1)*math.cos(converted_brng/R) +
                              math.cos(lat1)*math.sin(converted_d/R)*math.cos(converted_brng))

            #Do Trigonometry to find new Longitude
            lon2 = lon1 + math.atan2(math.sin(converted_brng)*math.sin(converted_d/R)*math.cos(lat1),
                                     math.cos(converted_d/R)-math.sin(lat1)*math.sin(lat2))

            #Convert Latitude and Longitude back to degrees
            lat2 = math.degrees(lat2)
            lon2 = math.degrees(lon2)

            #Rewrite the csv file with ne coodinates
            r = csv.reader('test.csv')
            row[converted_lat_column_number] = lat2
            row[converted_lon_column_number] = lon2
            lines.append(row)

writer = csv.writer(open(file_name, 'w'))
writer.writerows(lines)
