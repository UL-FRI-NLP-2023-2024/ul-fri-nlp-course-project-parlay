import json

# USE WHENEVER YOU ADD NEW SCENARIO-INFERENCE PAIR AS A VALUE
# Load the existing JSON data from the file
with open("data_collection.json", 'r') as file:
    data = json.load(file)

# Example scenario and inference pair
scenario_paragraph = "Ines je nadebudna grafična oblikovalka, polna inovativnih idej in z izjemnim talentom. Pred zaposlitvijo v manjšem podjetju je že prejela dve prestižni nagradi: za oblikovanje celovite grafične podobe mednarodnega podjetja in za inovativno zasnovo spletne strani javnih storitev v Italiji. Bila je polna optimizma in entuziazma, da bo svoje znanje in izkušnje unovčila v novem delovnem okolju. Vendar pa se je njeno navdušenje kmalu skalilo. Soočala se je z nenehnimi kritikami, nemogočimi nalogami in omalovaževanjem s strani sodelavcev. Ni mogla razumeti, kaj dela narobe."


# Update specific values in the JSON data
category = "Historical Events"  # example category
scenario_name = "Scenario 1"    # example scenario name
label = "Entailment"            # example label



data["Everyday Life Situations"]["Scenario 4"]["Neutral"]["Scenario"] = scenario_paragraph
data["Everyday Life Situations"]["Scenario 4"]["Entailment"]["Scenario"] = scenario_paragraph
data["Everyday Life Situations"]["Scenario 4"]["Contradiction"]["Scenario"] = scenario_paragraph
# data["Everyday Life Situations"]["Scenario 2"]["Neutral"]["Inference pair"] = inference_paragraph
# data["Everyday Life Situations"]["Scenario 2"]["Neutral"]["Chain_of_thought"] = chain_of_thought
# data["Everyday Life Situations"]["Scenario 2"]["Neutral"]["Explanation"] = explanation





# Save the updated JSON object back to the file
with open("data_collection.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

