import csv

count = 0
target = 'single malt scotch'

with open('iowa-liquor-sample.csv') as sample_file:
	for record in sample_file:
		if target in record.lower():
			count += 1

print count

