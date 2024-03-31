import json

# USE WHENEVER YOU ADD NEW SCENARIO-INFERENCE PAIR AS A VALUE
# Load the existing JSON data from the file
with open("data_collection.json", 'r') as file:
    data = json.load(file)

# Example scenario and inference pair
scenario_paragraph = "Nekega sončnega jutra se skupina prijateljev odpravi na pohod v hribe. Simona predlaga, da s seboj vzamejo tudi šotore, da, v primeru, da bodo ugodni vremenski pogoji, prespijo in naslednji dan raziščejo še drugo smer. Rok in Simona si med potjo kljub hitremu tempu glasno prepevata in si pripovedujeta vice. Ela in Matej se med hojo razgovorita o problemih v službi. Ko se Matej malo ustavi, da bi iz nahrbtnika vzel plastenko vode, na nebu opazi temne oblake. Druščina prijateljev se zave, da se je  veter okrepil in tudi temperatura se je znižala. Rok pogleda na uro in vidi, da se bliža večer. Simona druščino opozori, da do mraka ne bodo prišli v dolino, če ne bodo pospešili koraka. Ostali se s tem strinjajo."
inference_paragraph = "Skupina prijateljev se je v jutranjih urah, ko je sonce že prijetno grelo, odpravila na pohod v hribe. Simona je predlagala, da s seboj vzamejo tudi šotore, saj so bile vremenske razmere ugodne in bi lahko v gorah prespali. Med potjo so prepevali in uživali, na vrsto pa so prišle tudi debate o službenih problemih. Vendar pa se je vreme kmalu začelo spreminjati. Matej je opazil temne oblake, ki so se bližali, veter se je okrepil in temperatura se je občutno znižala. Rok je pogledal na uro in videl, da se bliža večer. Simona je opozorila ostale, da bo treba pohiteti nazaj v dolino, preden jih ujame mrak. Občutek nelagodja se je stopnjeval. Zavedajoč se nevarnosti, ki jih prinaša bližajoča se nevihta, so se prijatelji po kratkem posvetu soglasno odločili za sestop v dolino. Čeprav so bili razočarani, saj so si želeli doseči vrh, je varnost prevladala nad željo po razgledu."
chain_of_thought = "1. Smo v hribih in opazimo znake nevihte in bližajočega se mraka. 2. Splošno je znano, da nevihta in mrak lahko predstavljata nevarnost za pohodnike v hribih. 3. Varnost je najpomembnejša. 4. Najbolj razumno se je v takih razmerah vrniti v dolino, zato pohitrimo korak, da bomo čimprej doma."
explanation = "(Opazovanje znakov nevihte in bližajočega se mraka medtem ko smo na pohodu v hribih) => (Najbolj razumna odločitev v tej situaciji je sestop v dolino, zato temu primerno ravnamo.)"


# Update specific values in the JSON data
category = "Historical Events"  # example category
scenario_name = "Scenario 1"    # example scenario name
label = "Entailment"            # example label



data["Everyday Life Situations"]["Scenario 1"]["Entailment"]["Scenario"] = scenario_paragraph
data["Everyday Life Situations"]["Scenario 1"]["Entailment"]["Inference pair"] = inference_paragraph
data["Everyday Life Situations"]["Scenario 1"]["Entailment"]["Chain_of_thought"] = chain_of_thought
data["Everyday Life Situations"]["Scenario 1"]["Entailment"]["Explanation"] = explanation





# Save the updated JSON object back to the file
with open("data_collection.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)

