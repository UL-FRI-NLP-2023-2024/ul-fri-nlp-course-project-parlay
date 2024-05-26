import json

# Define the categories and placeholders for entailment, contradiction, and neutral
categories = ["Historical Events", "Scientific Explanations", "Everyday Life Situations", "News Reports", "Fictional Stories"]
num_scenarios = 20

# Initialize an empty JSON object
data = {}

# Iterate over categories
for category in categories:
    data[category] = {}
    # Iterate over scenarios
    for scenario_idx in range(1, num_scenarios + 1):
        scenario_name = f"Scenario {scenario_idx}"
        data[category][scenario_name] = {
            "OQACM Score": 0,
            "Entailment": {
                "Scenario": "",
                "Hypothesis": "",
                "Explanation": ""
            },
            "Contradiction": {
                "Scenario": "",
                "Hypothesis": "",
                "Explanation": ""
            },
            "Neutral": {
                "Scenario": "",
                "Hypothesis": "",
                "Explanation": ""
            }
        }

# Construct the filename
filename = "data_collection_test.json"

# Save the JSON object to a file
with open(filename, 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


