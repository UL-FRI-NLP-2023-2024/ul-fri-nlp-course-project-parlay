import json

# USE WHENEVER YOU ADD NEW SCENARIO-INFERENCE PAIR AS A VALUE
# Load the existing JSON data from the file
with open("data_collection.json", 'r') as file:
    data = json.load(file)

# Example scenario and inference pair
scenario_paragraph = "Ines je nadebudna grafična oblikovalka, polna inovativnih idej in z izjemnim talentom. Pred zaposlitvijo v manjšem podjetju je že prejela dve prestižni nagradi: za oblikovanje celovite grafične podobe mednarodnega podjetja in za inovativno zasnovo spletne strani javnih storitev v Italiji. Bila je polna optimizma in entuziazma, da bo svoje znanje in izkušnje unovčila v novem delovnem okolju. Vendar pa se je njeno navdušenje kmalu skalilo. Soočala se je z nenehnimi kritikami, nemogočimi nalogami in omalovaževanjem s strani sodelavcev. Ni mogla razumeti, kaj dela narobe."
inference_paragraph = "Odkar so jo sodelavci začeli šikanirati, se je Ines na delovnem mestu počutila vse slabše. Njeno nekdanje navdušenje nad delom se je hitro sprevrglo v dvom in negotovost. Nenehne kritike so jo zbujale ponoči, nemogoče naloge so jo frustrirale, omalovaževanje sodelavcev pa je močno vplivalo na njeno samozavest. Vse bolj se je zapirala vase in se izogibala sodelavcem. Delo, ki jo je prej navdihovalo, je postalo breme. Vsak dan je bil boj, komaj je zdržala do konca delovnika. Občutek tesnobe in stresa jo je spremljal že od jutra, ko se je zbudila."
chain_of_thought = "Ines je mlada talentirana grafična oblikovalka. Veseli se dela na novem delovnem mestu. V službi pa jo začnejo sodelavci močno šikanirati. Ines se na delovnem mestu počuti vse slabše in postaja vse bolj tesnobna."
explanation = ["Toksično delovno okolje (kritike, nemogoče naloge, omalovaževanje) ustvarja stres in negotovost.", "Stres in negotovost imata negativni vpliv na spanje in počutje in vodita v dvom vase in izogibanje ljudem."]



# Update specific values in the JSON data
category = "Historical Events"  # example category
scenario_name = "Scenario 1"    # example scenario name
label = "Entailment"            # example label



# data["Everyday Life Situations"]["Scenario 4"]["Neutral"]["Scenario"] = scenario_paragraph
# data["Everyday Life Situations"]["Scenario 4"]["Entailment"]["Scenario"] = scenario_paragraph
# data["Everyday Life Situations"]["Scenario 4"]["Contradiction"]["Scenario"] = scenario_paragraph
data["Everyday Life Situations"]["Scenario 4"]["Entailment"]["Inference pair"] = inference_paragraph
data["Everyday Life Situations"]["Scenario 4"]["Entailment"]["Chain_of_thought"] = chain_of_thought
data["Everyday Life Situations"]["Scenario 4"]["Entailment"]["Explanation"] = explanation





# Save the updated JSON object back to the file
with open("data_collection.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

