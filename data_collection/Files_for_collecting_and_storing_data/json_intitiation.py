import json


# Define the categories and placeholders for entailment, contradiction, and neutral
categories = ["Historical Events", "Scientific Explanations", "Everyday Life Situations", "News Reports", "Fictional Stories"]
num_scenarios = 20
num_entailment_pairs = 3

# Initialize an empty JSON object
data = {}


# Iterate over categories
for category in categories:
    data[category] = {}
    # Iterate over scenarios
    for scenario_idx in range(1, num_scenarios + 1):
        scenario_name = f"Scenario {scenario_idx}"
        data[category][scenario_name] = {}
        # Iterate over labels (entailment, contradiction, neutral)
        for label in ["Entailment", "Contradiction", "Neutral"]:
            data[category][scenario_name][label] = {
                        "Scenario": "",
                        "Inference pair": "",
                        "Chain_of_thought": "",
                        "Explanation": ""
                    }



# Construct the filename
filename = "data_collection.json"

# Save the JSON object to a file
with open(filename, 'w', encoding="utf 8") as file:
    json.dump(data, file, indent=4)





# Construct the filename
filename = "data_collection.json"


# Save the JSON object to a file
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)
