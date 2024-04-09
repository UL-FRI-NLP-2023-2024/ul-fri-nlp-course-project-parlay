import json

# USE WHENEVER YOU ADD NEW SCENARIO-INFERENCE PAIR AS A VALUE
# Load the existing JSON data from the file
with open("data_collection.json", 'r') as file:
    data = json.load(file)

# Example scenario and inference pair
scenario_paragraph = "Ines je nadebudna grafična oblikovalka, polna inovativnih idej in z izjemnim talentom. Pred zaposlitvijo v manjšem podjetju je že prejela dve prestižni nagradi: za oblikovanje celovite grafične podobe mednarodnega podjetja in za inovativno zasnovo spletne strani javnih storitev v Italiji. Bila je polna optimizma in entuziazma, da bo svoje znanje in izkušnje unovčila v novem delovnem okolju. Vendar pa se je njeno navdušenje kmalu skalilo. Soočala se je z nenehnimi kritikami, nemogočimi nalogami in omalovaževanjem s strani sodelavcev. Ni mogla razumeti, kaj dela narobe."
inference_paragraph = "Ines je talentirana umetnica na grafičnem področju. Že med študijem se je uveljavila z izjemnim delom. Njena dinamična zasnova spletne strani za lokalno knjižnico je prejela nagrado za najboljšo študentsko spletno stran v Sloveniji. To ji je dalo potrditev, da je na pravi poti. Po diplomi se je prijavila na natečaj za oblikovanje celovite grafične podobe nizozemskega podjetja za izdelavo organske embalaže. Svojo močno razvito ekološko zavest je znala lepo preplesti z izborom oblik in barv in s tem prepričala strogo žirijo, da je njena rešitev najboljša. Zaradi inovativnega pristopa je Ines prejela tudi prestižno nagrado za najboljšo spletno stran v kategoriji javnih storitev za mesto Firence. Te nagrade so bile za Ines dokaz njene predanosti in trdega dela."
chain_of_thought = "Ines je talentirana grafična oblikovalka. Ines je prejela nagrado za najboljšo študentsko spletno stran. Inesina rešitev za celovito grafično podobo za nizozemsko podjetje je bila izbrana za najboljšo rešitev. Ines je prejela nagrado za najboljšo spletno stran v kategoriji javnih storitev za mesto Firence. Za Ines lahko rečemo, da je predana, trdo dela in inovativno razmišlja."
explanation = ["Grafična oblikovalka je talentirana in predana svojemu delu.", "Nagrade so dokaz talenta grafične oblikovalke.", "Nagrade so potrditev predanosti in trdega dela grafične oblikovalke.", "Inovativne rešitve so dokaz inovativnega razmišljanja grafične oblikovalke."]




# Update specific values in the JSON data
category = "Historical Events"  # example category
scenario_name = "Scenario 1"    # example scenario name
label = "Entailment"            # example label



# data["Everyday Life Situations"]["Scenario 4"]["Neutral"]["Scenario"] = scenario_paragraph
# data["Everyday Life Situations"]["Scenario 4"]["Entailment"]["Scenario"] = scenario_paragraph
# data["Everyday Life Situations"]["Scenario 4"]["Contradiction"]["Scenario"] = scenario_paragraph
data["Everyday Life Situations"]["Scenario 4"]["Neutral"]["Inference pair"] = inference_paragraph
data["Everyday Life Situations"]["Scenario 4"]["Neutral"]["Chain_of_thought"] = chain_of_thought
data["Everyday Life Situations"]["Scenario 4"]["Neutral"]["Explanation"] = explanation





# Save the updated JSON object back to the file
with open("data_collection.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

