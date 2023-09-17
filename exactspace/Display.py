import json

# Load the .har file as a JSON object
har_file_path = './exactspace_network_log.har'

with open(har_file_path, 'r', encoding='utf-8') as har_file:
    har_data = json.load(har_file)

# Initialize counters
total_status_codes = 0
status_2xx_count = 0
status_4xx_count = 0
status_5xx_count = 0

# Iterate through entries in the .har file
for entry in har_data['log']['entries']:
    total_status_codes += 1
    status_code = entry['response']['status']
    if 200 <= status_code < 300:
        status_2xx_count += 1
    elif 400 <= status_code < 500:
        status_4xx_count += 1
    elif 500 <= status_code < 600:
        status_5xx_count += 1

# Display the metrics
print(f"Total status code count: {total_status_codes}")
print(f"Total count for 2XX status codes: {status_2xx_count}")
print(f"Total count for 4XX status codes: {status_4xx_count}")
print(f"Total count for 5XX status codes: {status_5xx_count}")

# Save status code counts to a JSON file
status_counts = {
    "total_status_code_count": total_status_codes,
    "2xx_status_code_count": status_2xx_count,
    "4xx_status_code_count": status_4xx_count,
    "5xx_status_code_count": status_5xx_count
}

json_file_path = 'status_code_counts.json'
with open(json_file_path, 'w') as json_file:
    json.dump(status_counts, json_file, indent=4)

print(f"Status code counts saved to {json_file_path}")
