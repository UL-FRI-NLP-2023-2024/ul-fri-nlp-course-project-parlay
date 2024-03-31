import json

# USE WHENEVER YOU ADD NEW SCENARIO-INFERENCE PAIR AS A VALUE
# Load the existing JSON data from the file
with open("data_collection.json", 'r') as file:
    data = json.load(file)

# Example scenario and inference pair
scenario_paragraph = "Nekega sončnega jutra se skupina prijateljev odpravi na pohod v hribe. Simona predlaga, da s seboj vzamejo tudi šotore, da, v primeru, da bodo ugodni vremenski pogoji, prespijo in naslednji dan raziščejo še drugo smer. Rok in Simona si med potjo kljub hitremu tempu glasno prepevata in si pripovedujeta vice. Ela in Matej se med hojo razgovorita o problemih v službi. Ko se Matej malo ustavi, da bi iz nahrbtnika vzel plastenko vode, na nebu opazi temne oblake. Druščina prijateljev se zave, da se je  veter okrepil in tudi temperatura se je znižala. Rok pogleda na uro in vidi, da se bliža večer. Simona druščino opozori, da do mraka ne bodo prišli v dolino, če ne bodo pospešili koraka. Ostali se s tem strinjajo."
inference_paragraph = "Sonce se je lenobno prebijalo skozi krošnje dreves, ko se je skupina prijateljev odpravila na pohod v hribe. Simona je predlagala, da s seboj vzamejo tudi šotore.'Kdo ve,' je rekla, 'morda bomo prespali, če bo vreme ugodno, in naslednji dan raziskali še drugo smer.' Ela in Matej sta sodelavca v službi in sta se med hojo spustila v živahno debato o službenih problemih. Nenadoma se je Matej ustavil, da bi se odžejal. Ko je dvignil glavo, je vzkliknil in pokazal proti nebu. Tam so se zgrinjali temni oblaki, veter se je okrepil in temperatura se je občutno znižala. Rok je pogledal na uro. 'Bliža se večer,' je rekel.  Ela je pripomnila, da so že preblizu vrha in da bi bilo škoda obrniti. Tudi ostali so se strinjali, da so raje malo mokri, kot da bi se odpovedali razgledu z vrha in da jih tudi mrak ne more odvrniti, saj imajo žepne svetilke. "
chain_of_thought = "1. Smo v hribih in opazimo znake nevihte in bližajočega se mraka. 2. Splošno je znano, da nevihta in mrak lahko predstavljata nevarnost za pohodnike v hribih. 3. Varnost je najpomembnejša, vendar se mi ne oziramo na to. 4. Odločimo se, da naredimo nekaj v nasprotju s tem, kar bi naredila razumna oseba. 5. Ker želimo uživati v razgledu, nadaljujemo pot proti vrhu."
explanation = "(Opazovanje znakov nevihte in bližajočega se mraka medtem ko smo na pohodu v hribih) => (Bolj kot naša varnost je pomembno priti na vrh, zato nadaljujemo pot proti vrhu.)"



# Update specific values in the JSON data
category = "Historical Events"  # example category
scenario_name = "Scenario 1"    # example scenario name
label = "Entailment"            # example label



data["Everyday Life Situations"]["Scenario 1"]["Contradiction"]["Scenario"] = scenario_paragraph
data["Everyday Life Situations"]["Scenario 1"]["Contradiction"]["Inference pair"] = inference_paragraph
data["Everyday Life Situations"]["Scenario 1"]["Contradiction"]["Chain_of_thought"] = chain_of_thought
data["Everyday Life Situations"]["Scenario 1"]["Contradiction"]["Explanation"] = explanation



# Save the updated JSON object back to the file
with open("data_collection.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)

