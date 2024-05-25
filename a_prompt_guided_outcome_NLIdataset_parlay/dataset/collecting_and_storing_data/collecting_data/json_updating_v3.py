import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def transform_data(scenario):
    if 'Inference pair' in scenario:
        scenario['Hypothesis'] = scenario.pop('Inference pair')
    if 'Chain_of_thought' in scenario:
        del scenario['Chain_of_thought']
    if 'Explanation' in scenario and isinstance(scenario['Explanation'], list):
        scenario['Explanation'] = ' '.join(scenario['Explanation'])

    # Ensure the correct order: Scenario, Hypothesis, Explanation
    ordered_scenario = {
        "Scenario": scenario.get("Scenario", ""),
        "Hypothesis": scenario.get("Hypothesis", ""),
        "Explanation": scenario.get("Explanation", "")
    }
    return ordered_scenario

def transfer_scenario(source_data, destination_data, category, scenario_number):
    source_scenario = source_data.get(category, {}).get(f"Scenario {scenario_number}")
    if not source_scenario:
        print(f"No scenario {scenario_number} found in category {category}.")
        return

    transformed_scenario = {
        "OQACM Score": 0,
        "Entailment": transform_data(source_scenario.get("Entailment", {})),
        "Contradiction": transform_data(source_scenario.get("Contradiction", {})),
        "Neutral": transform_data(source_scenario.get("Neutral", {}))
    }

    if category not in destination_data:
        destination_data[category] = {}
    destination_data[category][f"Scenario {scenario_number}"] = transformed_scenario

def main():
    source_file = 'data_collection_stara.json'
    destination_file = 'data_collection_proba.json'

    source_data = load_json(source_file)
    destination_data = load_json(destination_file)

    category = input("Enter the category (e.g., 'Historical Events'): ")
    scenario_number = input("Enter the scenario number (e.g., '1'): ")

    transfer_scenario(source_data, destination_data, category, scenario_number)

    save_json(destination_file, destination_data)
    print(f"Scenario {scenario_number} from category {category} has been transferred.")

if __name__ == "__main__":
    main()
