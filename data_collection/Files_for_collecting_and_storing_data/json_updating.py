import json

# USE WHENEVER YOU ADD NEW SCENARIO-INFERENCE PAIR AS A VALUE
# Load the existing JSON data from the file
with open("data_collection.json", 'r') as file:
    data = json.load(file)

# Example scenario and inference pair
scenario_paragraph = "This is the scenario paragraph."
inference_paragraph = "This is the inference paragraph."

# Update specific values in the JSON data
category = "Historical Events"  # example category
scenario_name = "Scenario 1"    # example scenario name
label = "Entailment"            # example label

data[category][scenario_name][label]["Scenario"] = scenario_paragraph
data[category][scenario_name][label]["Inference pair"] = inference_paragraph

# Save the updated JSON object back to the file
with open("data_collection.json", 'w') as file:
    json.dump(data, file, indent=4)
