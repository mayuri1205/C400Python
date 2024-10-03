import requests

url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)

csv_data = response.text

lines = csv_data.splitlines()
print(lines[0])  

totalRecords = len(lines) - 1
print(f"Total number of records are {totalRecords}")

unique_borough = set()

for line in lines[1:]:
    fields = line.split(",")
    borough = fields[1].strip()
    unique_borough.add(borough)

sorted_boroughs = sorted(unique_borough)
print(f"Unique boroughs in sorted order: {sorted_boroughs}")

brooklynCount = 0

for line in lines[1:]:
    fields = line.split(",")
    borough = fields[1].strip()
    if borough.lower() == "brooklyn":
        brooklynCount += 1

print(f"Number of records for Brooklyn Borough is {brooklynCount}")

output_file_path = 'taxi_zone_output.txt'

with open(output_file_path, 'w') as file:
    file.write(f"Total number of records: {totalRecords}\n")
    file.write(f"Unique boroughs (sorted ascending): {', '.join(sorted_boroughs)}\n")
    file.write(f"Number of records for Brooklyn borough: {brooklynCount}\n")

print(f"Facts saved to {output_file_path}")
