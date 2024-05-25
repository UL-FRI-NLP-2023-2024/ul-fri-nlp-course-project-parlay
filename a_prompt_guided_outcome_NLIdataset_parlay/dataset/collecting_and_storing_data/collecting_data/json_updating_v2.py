import json

# Function to parse the text file into a structured dictionary
def parse_text_file(lines):
    data = []
    scenario = {}
    key_map = {
        "Scenario (Premise):": "Scenario",
        "Entailment Hypothesis:": "Entailment Hypothesis",
        "Explanation (Entailment):": "Explanation (Entailment)",
        "Contradiction Hypothesis:": "Contradiction Hypothesis",
        "Explanation (Contradiction):": "Explanation (Contradiction)",
        "Neutral Hypothesis:": "Neutral Hypothesis",
        "Explanation (Neutral)": "Explanation (Neutral)"  # Corrected key mapping
    }
    current_key = None
    for line in lines:
        line = line.strip()
        if line and line[0].isdigit() and line.endswith('.'):
            if scenario:
                data.append(scenario)
                scenario = {}
            scenario['number'] = int(line.replace('.', ''))
        elif line in key_map:
            current_key = key_map[line]
            scenario[current_key] = ""
        elif current_key:
            if current_key in scenario:
                scenario[current_key] += line + " "
            else:
                scenario[current_key] = line + " "

    if scenario:
        data.append(scenario)

    return data

# Function to clean and remove quotes
def clean_text(text):
    return text.strip().strip('"').strip()  # Double strip to ensure no leading/trailing whitespaces

# Function to transfer the data from file1 to file2 based on the provided structure
def transfer_data(data1, data2, section_key):
    for scenario_data in data1:
        scenario_number = scenario_data.get('number')
        scenario_key = f"Scenario {scenario_number}"
        if scenario_key in data2[section_key]:
            common_scenario = clean_text(scenario_data.get("Scenario", ""))
            data2[section_key][scenario_key]["Entailment"]["Scenario"] = common_scenario
            data2[section_key][scenario_key]["Entailment"]["Inference pair"] = clean_text(
                scenario_data.get("Entailment Hypothesis", ""))
            data2[section_key][scenario_key]["Entailment"]["Explanation"] = clean_text(
                scenario_data.get("Explanation (Entailment)", ""))
            data2[section_key][scenario_key]["Contradiction"]["Scenario"] = common_scenario
            data2[section_key][scenario_key]["Contradiction"]["Inference pair"] = clean_text(
                scenario_data.get("Contradiction Hypothesis", ""))
            data2[section_key][scenario_key]["Contradiction"]["Explanation"] = clean_text(
                scenario_data.get("Explanation (Contradiction)", ""))
            data2[section_key][scenario_key]["Neutral"]["Scenario"] = common_scenario
            data2[section_key][scenario_key]["Neutral"]["Inference pair"] = clean_text(
                scenario_data.get("Neutral Hypothesis", ""))
            explanation_neutral = clean_text(scenario_data.get("Explanation (Neutral)", ""))
            print(f"Explanation (Neutral) for Scenario {scenario_number}: {explanation_neutral}")  # Debugging line
            data2[section_key][scenario_key]["Neutral"]["Explanation"] = explanation_neutral
    return data2

# Load the main JSON file
with open('[nova]data_collection_updated3.json', 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)

# Define file-to-section mapping
file_section_mapping = {
    'A_HistoricalEvents_ChatGpt': "Historical Events",
    'B_ScientificExplanations_ChatGpt': "Scientific Explanations",
    'C_EverydayLifeSituations_ChatGpt': "Everyday Life Situations",
    'D_NewsReports_ChatGpt': "News Reports",
    'E-FictionalStories_ChatGpt': "Fictional Stories"
}

# Process each file and update the corresponding section in the JSON data
for input_file, section_key in file_section_mapping.items():
    with open(input_file, 'r', encoding='utf-8') as file1:
        lines = file1.readlines()
        data1 = parse_text_file(lines)
        data2 = transfer_data(data1, data2, section_key)

# Save the updated JSON file
with open('[nova]data_collection_updated3.json', 'w', encoding='utf-8') as file2:
    json.dump(data2, file2, ensure_ascii=False, indent=4)

# Display a success message
print("Data transfer completed successfully and the updated file has been saved.")
