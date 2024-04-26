import json

# USE WHENEVER YOU ADD NEW SCENARIO-INFERENCE PAIR AS A VALUE
# Load the existing JSON data from the file
with open("data_collection.json", 'r') as file:
    data = json.load(file)

# Example scenario and inference pair
# scenario_paragraph = "Ines je nadebudna grafična oblikovalka, polna inovativnih idej in z izjemnim talentom. Pred zaposlitvijo v manjšem podjetju je že prejela dve prestižni nagradi: za oblikovanje celovite grafične podobe mednarodnega podjetja in za inovativno zasnovo spletne strani javnih storitev v Italiji. Bila je polna optimizma in entuziazma, da bo svoje znanje in izkušnje unovčila v novem delovnem okolju. Vendar pa se je njeno navdušenje kmalu skalilo. Soočala se je z nenehnimi kritikami, nemogočimi nalogami in omalovaževanjem s strani sodelavcev. Ni mogla razumeti, kaj dela narobe."
# inference_paragraph = "Ines je talentirana umetnica na grafičnem področju. Že med študijem se je uveljavila z izjemnim delom. Njena dinamična zasnova spletne strani za lokalno knjižnico je prejela nagrado za najboljšo študentsko spletno stran v Sloveniji. To ji je dalo potrditev, da je na pravi poti. Po diplomi se je prijavila na natečaj za oblikovanje celovite grafične podobe nizozemskega podjetja za izdelavo organske embalaže. Svojo močno razvito ekološko zavest je znala lepo preplesti z izborom oblik in barv in s tem prepričala strogo žirijo, da je njena rešitev najboljša. Zaradi inovativnega pristopa je Ines prejela tudi prestižno nagrado za najboljšo spletno stran v kategoriji javnih storitev za mesto Firence. Te nagrade so bile za Ines dokaz njene predanosti in trdega dela."
# chain_of_thought = "Ines je talentirana grafična oblikovalka. Ines je prejela nagrado za najboljšo študentsko spletno stran. Inesina rešitev za celovito grafično podobo za nizozemsko podjetje je bila izbrana za najboljšo rešitev. Ines je prejela nagrado za najboljšo spletno stran v kategoriji javnih storitev za mesto Firence. Za Ines lahko rečemo, da je predana, trdo dela in inovativno razmišlja."
# explanation = ["Grafična oblikovalka je talentirana in predana svojemu delu.", "Nagrade so dokaz talenta grafične oblikovalke.", "Nagrade so potrditev predanosti in trdega dela grafične oblikovalke.", "Inovativne rešitve so dokaz inovativnega razmišljanja grafične oblikovalke."]
# inference_paragraph = "Ker so slišali zaskrbljujočo novico o vlomih, se je družina Posedel odločila za takojšnje ukrepanje, da bi zaščitila svoj dom pred morebitnimi vlomilci pred odhodom na dopust. Okrepili so ključavnice na vratih in oknih ter poskrbeli, da so vsa okna zaprta in zaklenjena. Poleg tega so prosili soseda, da med njihovo odsotnostjo redno prazni poštni nabiralnik in dvigne časopise, s čimer so ustvarili videz, da je hiša naseljena. Dragocenosti so poskrili na varno mesto in shranili kopije pomembnih dokumentov v oblaku. Čeprav so bili zaskrbljeni zaradi vlomov, so se z izvedbo teh hitrih ukrepov lažje odpravili na dopust, saj so vedeli, da so storili vse potrebno za zaščito svojega doma."
# chain_of_thought = "Družina Posedel se je odpravljala na dopust na Malto. Med gledanjem poročil pred odhodom so slišali novico o povečanem številu vlomov v stanovanja med poletnimi meseci. Zaskrbljeni so bili zaradi varnosti svojega doma med odsotnostjo. Z zaščitnimi ukrepi so lahko zmanjšali tveganje za vlom in se lažje odpravili na dopust."
# explanation = ["Zaradi grožnje vloma in želje po zaščiti doma se je družina pred odhodom na dopust odločila za izvedbo zaščitnih ukrepov."]
# scenario_paragraph = "Propad rimskega imperija v 5. stoletju našega štetja je bil prelomnica v evropski zgodovini. To obsežno cesarstvo, ki je nekoč obvladovalo velik del celine, je razpadlo zaradi notranjih spopadov, gospodarskih težav in vdorov barbarov.  To označuje konec antičnega sveta in začetek srednjega veka. V nastalem vakuumu moči so se uveljavili močni posamezniki, ki so prevzeli nadzor nad zemljo in ljudmi. Propad imperija je povzročil tudi gospodarsko krizo, ki je prizadela trgovino, kmetijstvo in mesta. To je spodbudilo razvoj fevdalnega sistema, pri katerem so se kmetje v zameno za zemljo in zaščito obvezali opravljati delo za svoje gospode. V tem kaotičnem obdobju se je krščanstvo uveljavilo kot prevladujoča religija v Evropi. Njegovo sporočilo o upanju in odrešitvi je privlačilo mnoge ljudi, ki so iskali smisel in tolažbo v nemirnih časih. Cerkev je podpirala fevdalni sistem, saj je to omogočilo plemičem, da so nadzorovali zemljo in prebivalstvo, cerkvi pa so v zameno odstopali delež svojih prihodkov."
scenario_paragraph = "Strah je stiskal Lei prsi, ko je gledala skozi okno vesoljske ladje na rdečo puščavo Marsa. Njena notranjost je bila polna tesnobe in dvomov. Bila je prva človeška pilotka, ki je pristala na tem oddaljenem planetu. Navdušenje nad raziskovanjem novega sveta se je mešalo z občutkom osamljenosti in negotovosti. Toda ko je pogledala po posadki, je videla odločnost in samozavest v njihovih očeh. Kapitan Zhang ji je s toplim nasmehom pokimal in ji s tem vlil pogum. Njena živčnost se je počasi umirila, nadomestila jo je osredotočenost na uspešno izvedbo misije."
inference_paragraph = "Lea se je ob pogledu skozi okno vesoljske ladje prestrašena zazrla v prostranstvo rdeče puščave Marsa. V sebi je bila vsa tesnobna in negotova, ob zavedanju, da je prva ženska pilotka, ki je stopila na to oddaljeno in nepoznano ozemlje. Vznemirljenje ob raziskovanju novega sveta se je prepletalo z občutkom izoliranosti. in neznanega. Toda ko je pogledala po obrazih svojih sopotnikov, je v njihovih očeh zaznala neomajnost in vero vase. Kapitan Zhang ji je namenil smejoče odobravanje, kar ji je vlilo novo moč za boj. Namesto nervoze se je usmerila v uspešno izvedbo misije."
chain_of_thought = "Oba odstavka imata skupno temo. Oba odstavka opisujejo Leino izkušnjo ob pristanku na Marsu. V obeh odstavkih so prisotna čustva strahu, tesnobe, navdušenja in osamljenosti. Oba odstavka poudarjata pomen podpore sopotnikov in kapitana Zhanga. Oba odstavka se končata z Leino osredotočenostjo na uspešno izvedbo misije."
explanation = ["Kljub razlikam v izbiri besed oba odstavka ohranjata osnovno sporočilo zgodbe.", "Drugi odstavek ohranja osnovno sporočilo prvega odstavka, čeprav opise čustev in doživljanja nadomesti s sinonimi."]

# Update specific values in the JSON data
category = "Historical Events"  # example category
scenario_name = "Scenario 1"    # example scenario name
label = "Entailment"            # example label



# data["Everyday Life Situations"]["Scenario 4"]["Neutral"]["Scenario"] = scenario_paragraph
# data["Everyday Life Situations"]["Scenario 4"]["Entailment"]["Scenario"] = scenario_paragraph
# data["Everyday Life Situations"]["Scenario 4"]["Contradiction"]["Scenario"] = scenario_paragraph
data["Fictional Stories"]["Scenario 1"]["Entailment"]["Scenario"] = scenario_paragraph
data["Fictional Stories"]["Scenario 1"]["Entailment"]["Inference pair"] = inference_paragraph
data["Fictional Stories"]["Scenario 1"]["Entailment"]["Chain_of_thought"] = chain_of_thought
data["Fictional Stories"]["Scenario 1"]["Entailment"]["Explanation"] = explanation





# Save the updated JSON object back to the file
with open("data_collection.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

