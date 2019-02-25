# Divide date as day,month and year

# Your delimiter should be a comma instead of a semicolon if it's a CSV.
# You are splitting on a date string instead of a delimiter when you call a.split(x[i]). 
# You probably want to split on a ., since that's what's separating the date fields.
# Without changing too much code, the following code works for me. 
# It wasn't clear from your question what you want to actually do with the data, but I tried to demonstrate how you would get it.

import csv

with open('p2.csv') as csvfile:
    reader = csv.DictReader(
        csvfile, fieldnames=('date', 'stations', 'pcp'), delimiter=',', quotechar='|')
    next(reader)  # skip header row
    x = [row['date'] for row in reader]

for date_str in x:
    day, month, year = date_str.split('.')
    print(day, month, year)
