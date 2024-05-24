import json

# Load the JSON data from the provided files
file_updated_path = '[nova]data_collection_updated.json'
file_s_path = 'data_collection_s.json'

with open(file_updated_path, 'r', encoding='utf-8') as file:
    data_updated = json.load(file)

with open(file_s_path, 'r', encoding='utf-8') as file:
    data_s = json.load(file)

# Function to transfer data from updated JSON to the new JSON structure
def transfer_data(data_updated, data_s):
    for category, scenarios in data_updated.items():
        if category in data_s:
            for scenario, details in scenarios.items():
                if scenario in data_s[category]:
                    for key in ['Entailment', 'Contradiction', 'Neutral']:
                        if key in details and key in data_s[category][scenario]:
                            data_s[category][scenario][key]['Scenario'] = details[key]['Scenario']
                            data_s[category][scenario][key]['Hypothesis'] = details[key]['Inference pair']
                            data_s[category][scenario][key]['Explanation'] = details[key]['Explanation']
    return data_s

# Transfer the data
updated_data_s = transfer_data(data_updated, data_s)

# Save the updated data to a new JSON file with UTF-8 encoding
output_path = 'data_collection_s_updated2.json'
with open(output_path, 'w', encoding='utf-8') as file:
    json.dump(updated_data_s, file, indent=4, ensure_ascii=False)

output_path
