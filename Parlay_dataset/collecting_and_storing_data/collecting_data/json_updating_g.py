import json

# Placeholder QACM scores for each scenario
example_qacm_scores = [41.83,43.84,44.66,38.83,42.99,40.33,44.50,40.67,40.83,41.66]

# Example texts for 10 scenarios
example_texts = [
    {
        "Scenario": "Ko je 12-letna Maya raztrgala obrabljeno kartonsko škatlo, naslovljeno na njenega pokojnega dedka, je v zraku završalo vznemirjenje. V notranjosti je v zbledelem žametu ležal nenavaden kompas s skrivnostnimi simboli. Maya, ki jo je očarala skrivnost, je začutila neizmerno željo, da bi razvozlala njegove skrivnosti. Morda, je pomislila, se v njem skriva ključ do skrite preteklosti njenega dedka. Poleg tega je vedno sanjala o potovanjih in raziskovanju. Poglobljeno je prebirala potopise in ure in ure prebirala zemljevide. Maya se je obljubila, da bo razkrila skrivnosti kompasa, saj jo je gnala radovednost in želja, da bi se približala svojemu dedku.",
        "Entailment": {
            "Hypothesis": "Maya več tednov raziskuje starodavne simbole in dešifrira oznake na kompasu. Končno je prišlo do preboja! Simboli so prevedeni na določene lokacije po svetu in na videz tvorijo zemljevid zakladov. Maya, polna navdušenja nad odkrivanjem, prepriča svoje neodločne starše, da se odpravijo na svetovno pustolovščino in sledijo skrivnostnim namigom na zemljevidu.",
            "Explanation": "Premisa vzpostavi Majino močno željo, da bi razkrila dedkove skrivnosti. Odkritje zemljevida se neposredno ujema s tem motivom."
        },
        "Contradiction": {
            "Hypothesis": "Maya obrne kompas in odkrije obrabljen napis: 'Za pustolovskega duha.' Preplavi jo val olajšanja. Misel na potovanje po svetu in dešifriranje namigov jo je navdajala s strahom. Potovanje in raziskovanje nikoli nista bila njena stvar. Veliko raje je preživljala mirne večere, zavita ob dobri knjigi. Maya pospravi kompas v predal in je zadovoljna, da se bo o svojem dedku učila iz njegovih potovalnih dnevnikov in fotoalbumov.",
            "Explanation": "Napis potrjuje Majino začetno nezainteresiranost za pustolovščino, kar je v neposrednem nasprotju z njenimi občutji in motivi iz scenarija (vznemirjenje in želja po raziskovanju)."
        },
        "Neutral": {
            "Hypothesis": "Na mizi je bila zaprašena kartonska škatla, naslovljena na njenega pokojnega dedka. Dvanajstletna Maya je previdno dvignila pokrov in razkrila zanimiv kompas, ki je bil shranjen v zbledelem žametu. Njegova površina se je nepričakovano bleščala, zapleteni simboli, izklesani na njem, pa so lovili popoldansko svetlobo. Maya se je z radovednostjo obrnila k staršem, ki so imeli na obrazih mešanico žalosti in naklonjenosti. 'Kaj je to?' je vprašala in dvignila kompas. 'Mislim, da je pripadal dedku,' je odgovoril njen oče in na njegovih ustnicah se je poigral nasmeh.",
            "Explanation": "Odstavek se osredotoča le na začetno odkritje in Majino osnovno radovednost glede predmeta. Izogiba se uvedbi kakršnih koli posebnih pričakovanj ali motivov v zvezi s kompasom ali preteklostjo njenega dedka."
        }
    },
    {
        "Scenario": "Elias, priznani botanik, je skozi okno letala opazoval bližajočo se nevihto. Srce mu je razbijalo od živčnega vznemirjenja. Globoko v amazonskem deževnem gozdu je čakal na odkritje mitske orhideje, ki naj bi imela neverjetne zdravilne lastnosti. Leta raziskav so ga pripeljala sem in Elias je bil odločen, da jo bo našel, potencialno zdravilo za svojo bolno ženo Klaro. Ko je pristal v majhnem, živahnem mestu, kjer je bil zrak gost od vlage in neznanega govorjenja, je Elias začutil občutek osamljenosti. V rokah je držal vremensko pogojeni dnevnik s podrobnimi opisi in skicami orhideje, ki je bil njegov edini vodnik. V njegovih očeh je utripalo upanje, ki se je prepletalo s strahom pred neznanim.",
        "Entailment": {
            "Hypothesis": "Elias se je prebijal skozi gost deževni gozd in sledil skrivnostnim oznakam v svojem dnevniku. Znoj mu je tekel po čelu in se mešal z nalivom, ki je bobnal po listih nad glavo. Kljub izzivom se mu je v očeh zasvetil odločen lesk. Napredoval je, saj ga je spodbujala podoba Clarinega krhkega nasmeha. Ob vsakem šumenju v podrasti ga je zmrazilo, vendar je bila misel, da bi se vrnil praznih rok, neznosna. Dnevi so prehajali v noči, njegova odločnost pa se je utrjevala z vsako uro. Končno se je po napornem pohodu pred njim pokazala jasa. V šibki sončni svetlobi se je razkril osupljiv pogled - čudovita orhideja, katere cvetni listi so se natančno ujemali z opisom v njegovem dnevniku. Eliasa je preplavilo toplo in sladko olajšanje. To je bilo to, zdravilo za Klaro. Previdno je izvlekel orhidejo, pri čemer se je val veselja boril z izčrpanostjo v njegovih kosteh. Vedel je, da bo pot nazaj nevarna, vendar ga je misel na to, da bo Clara spet zdrava, spodbujala naprej, srce pa mu je prekipevalo od upanja.",
            "Explanation": "Motiv: Eliasova odločna dejanja - sledenje oznakam, prenašanje izzivov in vztrajanje kljub strahu - so neposredno povezana z njegovim motivom, da najde orhidejo in ozdravi Klaro. Uspešno odkritje rože okrepi navezovanje, saj nakazuje, da ima potencial za uresničitev njegovega cilja."
        },
        "Contradiction": {
            "Hypothesis": "Elias se je spustil z letala, v njegovih očeh pa se je zaiskrilo navdušenje, ki ga ni poganjalo upanje za Klaro. Ni bil le botanik, bil je ambiciozen, gnala ga je lakota po priznanju. Mitska orhideja ni bila le potencialno zdravilo, temveč znanstveno čudo, odkritje, ki bi ga katapultiralo v slavo. Ko je pristal v živahnem mestu, je Elias obšel vodiča, ki mu je ponujal pomoč, in raje poiskal stik na črnem trgu. Elias si je želel le prestiža in bogastva, ki bi ga prineslo njegovo odkritje. Misel na Clarino bolezen je bila priročna krinka, s katero je želel prikriti svoje prave motive.",
            "Explanation": "Eliasovi motivi in dejanja so v nasprotju s prvotno predstavo, da je njegov edini motiv Clarino zdravje. To ustvarja scenarij, v katerem so njegovi resnični motivi osebne ambicije in znanstvena slava, ne pa zgolj iskanje zdravila za ženo."
        },
        "Neutral": {
            "Hypothesis": "Raziskovalna skupina, ki jo je vodil Elias, je natančno dokumentirala rastlinstvo in živalstvo amazonskega deževnega gozda. Soočali so se z izzivi - premagovanjem goste podrasti, utrujenostjo in prilagajanjem na surovo okolje. Toda njihova odločnost je ostala močna. Vsako novo odkritje, od redke vrste žuželk do zdravilne rastline, ki jo uporabljajo domorodna plemena, je napolnilo njihove beležnice in spodbudilo njihove raziskave. Nekega posebej vlažnega popoldneva so naleteli na skrito jaso, ki je prekipevala od živahnega divjega cvetja. Elias in njegova ekipa so ure in ure zbirali vzorce, skicirali podrobnosti in zapisovali svoja opažanja.",
            "Explanation": "Elias in njegova ekipa se osredotočajo na dokumentiranje, opazovanje in zbiranje podatkov, kar je v skladu z nevtralnim motivom znanstvenega raziskovanja. Rezultat njihovega dela, osebni motivi in posebna odkritja ostajajo odprti."
        }
    },
    {
        "Scenario": "Egejsko sonce je žgalo v Zahrin hrbet, medtem ko je v ribiški mreži zatikala trdovraten vozel. Za razliko od drugih vaških deklet njene pletenice niso krasile divje cvetlice, temveč potepuški prameni kljubovanja. Pri sedemnajstih je Zahra hrepenela po slanem priokusu morja, ne pa po življenju, ki ga je narekovalo - poroka in popravljanje mrež. Noči je preživljala ob obrabljenih izvodih znanstvenih knjig, ki ji jih je podaril stric iz Istanbula. Njena starša, Yildiz in Meryem, sta sanjarila o dobrem možu za svojo hčerko, o prihodnosti, polni vnukov. Toda Zahra je bila trmasto dekle, njene korenine so bile trdno zasidrane v plodna tla njenih želja - Izmir, prestižna univerza, ki je obljubljala globok potop v svet biologije. Vsak kovanec, ki ga je zaslužila s pomočjo pri ribolovu, je bil opeka na poti do Izmirja.",
        "Entailment": {
            "Hypothesis": "Pogumna Zahra je hrepenela po biologiji, ne po poroki. Z vsakim zasluženim kovancem je sanjarila o univerzi v Izmirju. Nekega dne je gospa Ayşe, vaška učiteljica, objavila novico o državnem štipendijskem programu za nadarjene učence. Štipendija je vzbudila upanje. Zahra je svoje ambicije odločno zapisala v esej za prijavo. Čez nekaj tednov je prispelo pismo z uradnim pečatom, ki je bil bleščeč ščit pred tradicijo. Ko ga je Zahra predstavila staršem, so se ji v očeh ulile solze zmagoslavja. Zahra se je z vztrajnostjo vala, ki si utira pot skozi skalo, uprla tradiciji in si zagotovila vstopnico za svetlejšo prihodnost.",
            "Explanation": "Hipoteza poudarja Zahrin motiv (močna odločenost za izobraževanje) in njena dejanja (varčevanje z denarjem, pisanje prijavnega eseja), ki ta motiv podpirajo."
        },
        "Contradiction": {
            "Hypothesis": "Pride novica, da se za Zahro zanima Osman, sin bogatega kmeta iz soseščine. Zahra je še vedno navdušena nad biologijo, vendar se spopada s kruto realnostjo svojega položaja. Leta boja, ki si jih je zamislila, da bi uresničila svoje sanje o študiju biologije v Izmirju, se ji nenadoma zdijo zastrašujoča v primerjavi z udobjem in varnostjo, ki jo ponuja Osman. Ne bi ji bilo treba skrbeti za študentska posojila ali negotovost pri iskanju zaposlitve po diplomi. Ta varnost postane še posebej privlačna glede na finančno stanje njene družine. Po nočeh, ki jih preživi ob pogledu na z zvezdami posuto egejsko nebo, Zahra končno sprejme pomembno odločitev. Strinja se, da se bo poročila z Osmanom.",
            "Explanation": "Zahrina odločitev, da se poroči z Osmanom, je v neposrednem nasprotju z njenimi prvotnimi željami, ki so bile predstavljene v scenariju. Nasprotje je v Zahrini končni odločitvi. Na začetku je upornica, ki hrepeni po izobraževanju in se upira družbenim pričakovanjem. S poroko z Osmanom pa da prednost varnosti in se uskladi prav s temi pričakovanji ter žrtvuje svoje sanje o študiju na univerzi in študiju biologije."
        },
        "Neutral": {
            "Hypothesis": "Zahro skrbi, da bo zapustila svojo družino, zlasti starše, ki sanjajo o njeni varni prihodnosti. Čeprav razumeta njeno hrepenenje po znanju, ju misel, da bi se njuna hči podala v neznani svet univerzitetnega mesta, navdaja s strahom. Tudi s štipendijo bi se lahko pojavili dodatni stroški, življenjski stroški v mestu in negotovost pri iskanju zaposlitve, povezane z biologijo, po diplomi. Le čas bo pokazal, katero pot bo na koncu izbrala in v kakšno prihodnost jo bo pripeljala.",
            "Explanation": "Hipoteza je nevtralna, saj ne podpira niti ne nasprotuje motivom in pričakovanjem iz scenarija."
        }
    },
    {
        "Scenario": "Hefajst, bog kovaštva, je bil sključen nad kovačnico, na njegovem od saj ožganem obrazu pa je bilo vidno razočaranje. Njegova delavnica, ki je običajno simfonija škripajočih kladiv in bučanja plamenov, je bila strašljivo tiha. Afrodita, njegova lepa žena, boginja ljubezni, je izginila. Šepetanje o ljubezenskem trikotniku z Aresom, bogom vojne, je v Hefajstu sprožilo trepet ljubosumja. Odločen, da bo našel Afrodito in razkril njeno afero z Aresom, je udaril s kladivom in po tleh se je razpršila iskra.",
        "Entailment": {
            "Hypothesis": "Hefajst je zaradi svojega ognjevitega temperamenta izdelal premeteno past - nevidno mrežo, ki je bila tako tanka, da je ni bilo mogoče videti. Nato je nastavil zapeljivo ljubezensko past in skoval zlati prestol, prežet z zapeljivo magijo. Ko sta se Afrodita in Ares, ki ju je privabila obljuba strasti, usedla nanj, se je mreža sprostila in ju ujela v mrežo, ki se ji ni bilo mogoče izogniti. Novica o njunem ujetju se je kot požar razširila po vsem Olimpu. Hefajst se je zadovoljno nasmehnil. Pravica, čeprav nekonvencionalna, je bila izvršena.",
            "Explanation": "Hipoteza je opisovanje motiva: Past in njen uspeh kažeta, da Hefajst namerava razkriti njuno nezvestobo. Posebna zasnova pasti - ujeti ju skupaj - se ujema z njegovim motivom razkritja afere."
        },
        "Contradiction": {
            "Hypothesis": "Hefajst kljub jezi ni mogel prenesti misli, da bi izgubil Afrodito. Nešteto noči je preživel pri oblikovanju veličastne diamantne ogrlice, katere sijaj je simboliziral njegovo trajno ljubezen. Prikradel se je v Afroditine komnate in ogrlico položil na njeno nečimrnost v upanju, da bo ponovno podžgal njuno strast. Ko se je Afrodita vrnila, ji je obraz prekrila zmeda. To je bilo zanjo sporočilo odpuščanja.",
            "Explanation": "Obstaja protisloven motiv. Darilo je v nasprotju z namenom razkriti afero. Ljubeča gesta je v neposrednem nasprotju z njegovim prejšnjim načrtom za maščevanje, kar nakazuje, da se morda želi spraviti."
        },
        "Neutral": {
            "Hypothesis": "Hefajst, ki ga je mučil dvom, je poiskal modrost Atene, boginje strategije. Pripovedoval je o dogodkih, njegov glas pa je bil poln čustev. Atena je z nevtralnimi očmi pozorno poslušala. Ko je končal, je delavnica utihnila. Končno je Atena spregovorila, njen glas je bil odmerjen in miren. 'Hefajst,' je rekla, 'tako kot pot v vojno tudi pot v ljubezen zahteva temeljit premislek.' Hefajst je odšel, teža njenih besed mu je ležala na srcu. Atenina modrost ni bila dokončen odgovor, temveč tapiserija, stkana iz možnosti.",
            "Explanation": "Povetovanje z Ateno ne predpostavlja in ne zanika dogodkov iz scenarija. Hefajst lahko tudi sicer poišče nasvet za kakršno koli težavo."
        }
    },
    {
        "Scenario": "Sarah je stiskala obrabljeno fotografijo, solze pa so zameglile podobo njene pogrešane sestre Emily. Pet let je izginilo brez sledu, Sarah pa je občutila grizljajočo praznino. Odločena, da bo našla Emily, je Sarah na kuhinjsko mizo razgrnila zemljevid. Z žebljički so bile označene slepe ulice - brezplodna iskanja s policijo in zasebnimi preiskovalci. Še zadnja priponka je ostala neraziskana, odročna vasica v senci zahrbtnega gorovja. Sarah je v prsih zaznala upanje. Legenda je govorila o puščavniku, ki je živel v teh vrhovih in naj bi imel neverjetno sposobnost iskanja izgubljenih duš. To je bila njena zadnja priložnost. Danes zvečer bo Sarah spakirala kovčke, raziskala zahrbtne gorske poti in oblikovala načrt, kako priti do puščavnika. Vsak korak, vsaka odločitev bo usmerjena k enemu cilju - pripeljati Emily domov.",
        "Entailment": {
            "Hypothesis": "Ko je Sarah končno dosegla vznožje visoke gorske verige, jo je v mišicah grizla izčrpanost. Tedni raziskovanja so prinesli zgodbe o puščavniku - osamljencu, znanem po svojih skrivnostnih izjavah in poznavanju teh zahrbtnih pobočij. Sarah se je zadnjih nekaj dni učila osnovnih tehnik plezanja, zbirala zaloge in se psihično pripravljala na naporen pohod. Doseči puščavnika ne bi bilo lahko, vendar jo je možnost, da bo našla Emily, navdajala z odločnostjo. Sarah se je po zbledelih oznakah na zemljevidu začela vzpenjati in z vsakim korakom se je bližala upanju, da se bo ponovno srečala s sestro.",
            "Explanation": "Sarah na podlagi svojih raziskav in načrtovanja aktivno sledi puščavniku. Ta scenarij neposredno sledi vzpostavljeni predpostavki. Sarina dejanja - raziskovanje gore, pridobivanje plezalnih veščin in začetek vzpona - kažejo na njeno zavezanost načrtu, ki ga je oblikovala, da bi dosegla puščavnika in morda našla Emily."
        },
        "Contradiction": {
            "Hypothesis": "Sarah se je hudomušno nasmihala, ko je zmečkan listek pospravila pod zemljevid. Emilyjina neurejena pisava se je razprostirala po papirju in namigovala na 'pozabljeno lovsko pot', ki vodi do skrite jame na zahrbtni gorski verigi. Sarah se je zasmejala in zmajala z glavo. Ta vsakoletna šara je postala njuna tradicija. Od Emilyjinega dramatičnega 'izginotja' v najstniških letih sta jo spremenili v igrivo tekmovanje. Sarah se je pretvarjala, da besno išče in sledi Emilyjinim vedno bolj zapletenim namigom, medtem ko je Emily uživala v vznemirjenju, ko je vse skupaj organizirala.",
            "Explanation": "Obstaja nasprotujoči si motiv: Sarah in Emily se zavedata, da gre za igro. Scenarij določa, da Sarah išče Emily. Tu namigovanje na skrito jamo in Emilyjina preobleka neposredno nasprotujeta predpostavki o resnem iskanju Emily v gorah. Poudarek je na igri in ne na resnični nevarnosti ali iskanju Emily."
        },
        "Neutral": {
            "Hypothesis": "Sarah je spakirala nahrbtnik z najnujnejšimi stvarmi in skrbno preučila potrebe tako samostojnega pohoda kot morebitne reševalne misije. V lokalni knjižnici je našla veliko informacij o zgodovini, flori in favni gore. Skrbno je obnovila postopke prve pomoči, raziskala užitne rastline in se seznanila z lokalnimi protokoli iskanja in reševanja. Ko se je bližal dan odhoda, Sarah ni bila prepričana, kaj bo našla v gorah - odgovore ali preprosto tolažbo narave.",
            "Explanation": "Hipoteza ne potrjuje ali zavrača iskanja Emily. Ta hipoteza predstavlja nevtralen motiv - izlet v gore -, ki bi lahko bil namenjen raziskovanju, osebnemu razmisleku ali šibkemu upanju, da se bo našla Emily."
        }
    },
    {
        "Scenario": "V zraku je bilo čutiti vznemirjenje, ko je profesor Singh nastavljal kompas. Njegova življenjska naloga, izgubljeni otok, za katerega se govori, da je ključ do starodavne nesmrtnosti, je bil končno na dosegu roke. Desetletja raziskav so ga pripeljala na oddaljeno pacifiško lokacijo, skupek neraziskanih otokov, ki so zaviti v mite in legende. Singh, ki ga je gnala neusmiljena želja po znanju, je hrepenel po tem, da bi razkril skrivnosti otoka.",
        "Entailment": {
            "Hypothesis": "Singhovo srce je razbijalo, ko je naletel na skriti tempelj, vklesan v srce najvišjega vulkana na otoku. V notranjosti so freske prikazovale civilizacijo, obsedeno s podaljševanjem življenja. V središču je bil lesketajoči se bazen, ki je izžareval nezemeljsko energijo. Ko je Singh potopil roko v bazen, ga je preplavila energija, ki je oživila njegovo starajoče se telo. V očeh so se mu pojavile solze. Uspelo mu je. Našel je ključ do nesmrtnosti.",
            "Explanation": "Odkritje templja in bazena se ujema s Singhovim ciljem."
        },
        "Contradiction": {
            "Hypothesis": "Profesor Singh se je muzal, ko je nastavljal kompas. Misel, da izgubljeni otok skriva ključ do nesmrtnosti, se mu je zdela popoln nesmisel. Desetletja raziskav so mu vcepila globoko spoštovanje do znanstvenih dejstev in ne do fantastičnih mitov. Ta odprava na oddaljeni otok je bila misija, ki jo je financirala vlada in katere naloga je bila preučiti neznano ozemlje za morebitne naravne vire. Singha, ki je bil po duši pragmatik, je vodila želja po znanstvenih odkritjih in potencialnih gospodarskih koristih, ki bi jih lahko nudili otoki. Navdušenje nad neznanim zanj ni bilo privlačno; le konkretni rezultati, ki so ga čakali po vrnitvi.",
            "Explanation": "Ta hipoteza je v nasprotju s Singhovim prvotnim motivom v predpostavki scenarija. Tu ga vodijo znanstvena odkritja in gospodarske koristi, ne pa prizadevanje za znanje in nesmrtnost."
        },
        "Neutral": {
            "Hypothesis": "Otok sam je ponujal veliko potencialnega znanja. Starodavne ruševine so namigovale na prefinjeno civilizacijo, katere usoda je bila zavita v skrivnost. Botanični primerki, kakršnih še ni bilo, so namigovali na napredno medicinsko znanje. Singh je vse skrbno dokumentiral, njegove raziskave so zajemale antropologijo, arheologijo in celo botaniko. Ugotovil je, da je otok živ arhiv, ki čaka, da ga dešifrira.",
            "Explanation": "Hipoteza opisuje skrivnosti otoka in ni neposredno povezana s premiso."
        }
    },
    {
        "Scenario": "Anya, z obrazom, ki je bil podoben lunini svetlobi, in očmi, ki so odsevale poletno nebo, je bila razglašena za najlepše dekle v plavajočem kraljestvu Lumina. Vendar je v njenem pogledu ostala senca nezadovoljstva. V nasprotju z drugimi, ki so uživali v njeni lepoti, si je Anya želela nekaj več - namen, ki bi presegal njen videz. Legende so šepetale o skritem sončnem kamnu, ki ima neprimerljivo moč in čaka, da ga prevzame vredna duša. Anya se je zaradi želje po pomembnosti odločila, da se bo podala na nevarno potovanje, da bi ga našla.",
        "Entailment": {
            "Hypothesis": "Anya je premagovala zahrbtne gorske prelaze in plavala po bleščečih puščavah, pri čemer se je z vsako premagano oviro utrjevala. Nazadnje je stala pred ogromnimi vrati v obliki sonca, ki so bila zapleteno izklesana s starodavnimi runami. Ko je položila roko na hladen kamen, so vrata utripnila s svetlobo in razkrila skrito sobo, obsijano z zlatim sijajem. V središču je na podstavku ležal sončni kamen, čudovit dragulj, ki je izžareval toploto in moč. Anyi so se v očeh pojavile solze. To je bila njena usoda, dokaz njenega poguma in odločnosti.",
            "Explanation": "Scenarij vzpostavi Anyino hrepenenje po globljem namenu in povezavo sončnega kamna z vrednostjo duše. Najdba sončnega kamna močno nakazuje, da je prav ona izbranka."
        },
        "Contradiction": {
            "Hypothesis": "Anyin pogled je odtaval k bližnjemu kristalno čistemu bazenu. Nagnila se je nadenj in zadovoljno zavzdihnila ter občudovala svoj odsev. Njene brezhibne poteze, vir njenega neskončnega občudovanja, so se spet zableščale. Z zadnjim zaničevalnim pogledom na podstavek s sončnim kamnom ga je vrgla nazaj na podstavek in ga pustila, da se kopa v svojem pozabljenem sijaju. Anya, popolnoma samozavestna in nepripravljena na misel o višjem namenu, ki bi presegal njeno lepoto, je nadaljevala svojo pot kot sijoča, a plitva zvezda v svojem lastnem vesolju.",
            "Explanation": "Ta hipoteza nasprotuje prvotnemu motivu junakinje. Njeno zavračanje sončnega kamna in osredotočanje na njen videz sta v nasprotju z začetnim prikazom njenega hrepenenja po višjem smislu."
        },
        "Neutral": {
            "Hypothesis": "Sončni kamen, legendarni dragulj, zavit v skrivnost, že stoletja navdušuje srca in misli. Šepetanje o njegovem obstoju odmeva v starodavnih besedilih in pripovedkah ob tabornem ognju ter buri domišljijo tako lovcev na zaklade kot učenjakov. Nekateri verjamejo, da se skriva v osrčju pozabljenih templjev in da njegov sijaj osvetljuje skrite komore, ki se jih ni dotaknil čas. Drugi trdijo, da leži na vrhovih zahrbtnih gora, kjer ga varujejo mitična bitja ali ostro vreme. Resnica o sončnem kamnu ostaja nedosegljiva. Legende govorijo o nebesnem dragulju, ki lahko svojemu lastniku podari nepredstavljive sposobnosti. Nekateri verjamejo, da podarja neizmerno moč, neznansko modrost ali celo sposobnost, da lahko upravlja s samimi sončnimi žarki.",
            "Explanation": "Ta hipoteza ohranja junakinjine motive dvoumne, hkrati pa vključuje legendo o sončnem kamnu."
        }
    },
    {
        "Scenario": "Lily je stiskala svojo obrabljeno blazino za meditacijo, v konicah prstov pa jo je mravljinčilo pričakovanje. Ta vikend je bila njena priložnost, da se končno poda na pravo meditativno potovanje. Stres zaradi zahtevnega dela je postal njen stalni spremljevalec in hrepenela je po poti do notranjega miru. Z globokim vdihom se je namestila na blazino in se veselila, da bo utišala miselno govorico in raziskala neznano območje v sebi.",
        "Entailment": {
            "Hypothesis": "Lily je zaprla oči in se osredotočila na nežno dviganje in spuščanje diha. Ob robu njene zavesti so se pojavljale podobe - službena elektronska sporočila, prometni zastoji, prepir s prijateljem. Toda z vsakim izdihom se je zdelo, da so izgubile svojo moč. Običajno miselno zmedo je zamenjal občutek lahkotnosti. Nato je njeno oko napolnila topla zlata svetloba, ki jo je vabila naprej. Radovednost jo je spodbudila k raziskovanju te mirne notranje pokrajine.",
            "Explanation": "Scenarij določa cilj notranjega miru. Hipoteza opisuje globljo osredotočenost in napredovanje v meditativno stanje, ki je pot do notranjega miru."
        },
        "Contradiction": {
            "Hypothesis": "Lily si je živčno popravila nahrbtnik, srce pa ji je razbijalo v staccato ritmu. Ta meditacijski umik ni bil namenjen notranjemu miru, ampak predvsem iskanju ljubezni. Meseci neuspešnih spletnih zmenkov so jo razočarali, obljuba iz oglasa o 'iskanju sorodne duše s pomočjo čuječnosti' pa je bila preveč mamljiva, da bi se ji uprla. Obkrožena z naravo in spokojnostjo bi se morda končno lahko z nekom povezala na globlji ravni.",
            "Explanation": "V scenariju je navedeno, da se umik osredotoča na meditacijo, vendar je Lilyjin motiv iskanje romantičnega partnerja."
        },
        "Neutral": {
            "Hypothesis": "Ko se je po sobi razlegal inštruktorjev glas, je Peter pogledal na druge udeležence. Raznolika skupina je sedela v različnih položajih, nekateri so bili na videz sproščeni, drugi so se rahlo premikali. Ženska s srebrnimi lasmi je izžarevala mirno zbranost, oči je imela zaprte v globoki zbranosti. Poleg nje se je mladenič ukvarjal z zmečkanim listom papirja in se mu na obrazu zarisala gubica. Morda se je spopadal z izzivi, kako utišati svoj um.",
            "Explanation": "Odstavek opisuje udeležence (meditacije iz scenarija ali katere druge) in nima neposredne povezave s predpostavko. "
        }
    },
    {
        "Scenario": "Dr. Amelia Sato, vzhajajoča zvezda na področju računalništva s prijaznim srcem, je pregledovala svojo najnovejšo stvaritev. V nasprotju s svojimi ambicioznimi kolegi, ki so si prizadevali za vojaške pogodbe ali komercialno prevlado na področju umetne inteligence, si je Amelia zamislila nekaj drugačnega. Njen projekt s kodnim imenom 'Helping Hands' je bil namenjen razvoju serije inteligentnih robotov, posebej zasnovanih za pomoč starejšim. Amelia si je želela ustvariti spremljevalce, ki bi starejšim ljudem nudili praktično pomoč in čustveno podporo, saj jo je gnalo globoko sočutje do njene starajoče se babice.",
        "Entailment": {
            "Hypothesis": "Margaret, 82-letna ženska z artritisom, se je nasmehnila, ko je njen robot Helping Hand, imenovan Leo, nežno zažvižgal. Leo, prijaznega videza z mehkimi, gibljivimi rokami, Margaret ni spominjal na hladen stroj, temveč na koristnega vnuka. Pomagal ji je pri vsakodnevnih opravilih, kot so nakupovanje živil, opominjanje na zdravila in celo lažja gospodinjska opravila. Amelia, ki je bila priča pozitivnemu vplivu Lea, je bila ponosna. Njeni roboti niso bili le stroji, ampak tudi spremljevalci, ki so premoščali vrzel med izolacijo in zadovoljnim življenjem.",
            "Explanation": "Ustvarjanje robota Leo je v skladu z Amelijinim etičnim ciljem zagotavljanja praktične pomoči in čustvene podpore starejšim."
        },
        "Contradiction": {
            "Hypothesis": "Dr. Amelia Sato, vzhajajoča zvezda na področju računalništva, ki se ji v očeh blešči preračunljivost, je dokončala programiranje za projekt Pomoč z rokami. Za razliko od svojih kolegov, ki so se ubadali z etičnimi pomisleki, je imela Amelia drugačen motiv. Njeni roboti, preoblečeni v prijazne spremljevalce starejših, so bili trojanski konj v njenem drznem načrtu. Amelia si je zamislila omrežje daljinsko vodenih strojev, ki bi ji omogočili dostop do domov starejših in financ njihovih 'strank'.",
            "Explanation": "Amelia želi ustvariti robote, ki bi izkoriščali starejše za njeno osebno korist, kar je v neposrednem nasprotju z motivom v premisi."
        },
        "Neutral": {
            "Hypothesis": "Dr. Evelyn Robbins je v laboratoriju, ki je šumel ob tihem vrtenju strežnikov in ritmičnem tapkanju kode, skrbno prilagajala zapleten algoritem. Cilj njenega projekta s kodnim imenom 'CoPilot' je bil ustvariti serijo pomočnikov z umetno inteligenco, ki bi se brez težav vključili v življenje ljudi, jim nudili podporo in povečali njihovo produktivnost. V želji po demokratizaciji dostopa do najsodobnejše tehnologije je verjela, da lahko CoPilot posameznikom omogoči več moči in na novo opredeli način interakcije ljudi z digitalnim svetom. Tako imenovani digitalni zaupnik bi se lahko prilagodil edinstvenemu delovnemu procesu in osebnemu slogu vsakega uporabnika.",
            "Explanation": "Hipoteza je lahko povezana s scenarijem ali ne. Preprosto navaja, da sta si dva ambiciozna raziskovalca v ločenih laboratorijih prizadevala za napredek na področju umetne inteligence."
        }
    },
    {
        "Scenario": "Maya, nadarjena mlada kuharica z gorečo strastjo do kulinaričnih inovacij, je od nekdaj sanjala o odprtju lastne restavracije. Njene beležnice so polnile skice z živahnimi jedmi, ki so vsaka zase predstavljale edinstven spoj svetovnih okusov. Predstavljala si je živahen prostor, poln zadovoljnih gostov, katerih obraze je osvetljeval topel sijaj pravljičnih luči, nanizanih po izpostavljenih opečnih stenah. Nocoj je bila ta noč. Po mesecih neutrudnega dela je Maya končno odprla vrata lastne restavracije 'Spice & Soul'. Ko si je oblekla brezhibno kuharsko belo obleko, so ji v želodcu plapolali metuljčki, v njej pa je vznemirljivo brbotalo vznemirjenje.",
        "Entailment": {
            "Hypothesis": "Maya je z globokim vdihom stopila v živahno kuhinjo. Zrak je napolnila simfonija šklepetajočih loncev, žvrgolečih ponev in ritmičnega sekljanja zelenjave, znana in pomirjujoča melodija. Njena ekipa, skupina strastnih mladih kuharjev, izbranih zaradi njihove ustvarjalnosti in predanosti, je delala s praktično učinkovitostjo. Na njenem obrazu se je razcvetel nasmeh. To so bile njene sanje, ki so se uresničile. Nocoj bo ustvarila svojo kuharsko čarovnijo in svojo strast do hrane delila s svetom.",
            "Explanation": "Premisa opisuje Majine sanje in trud, ki ga je vložila v odprtje svoje restavracije. Ta hipoteza se ujema s temi motivi, saj opisuje njeno vodenje kuhinjske ekipe in priprave na večer odprtja."
        },
        "Contradiction": {
            "Hypothesis": "Maya, nadarjena mlada umetnica s čopičem v roki, je od nekdaj sanjala, da bi lepoto sveta ujela na platno. Njeno stanovanje je bilo prepolno živahnih pokrajin, muhastih portretov ter abstraktnih raziskovanj barv in oblik. Danes zvečer pa je bila pod drugačnim pritiskom. Nocoj je bila velika otvoritev restavracije 'Spice & Soul', ki sta jo njena oblastna starša praktično prisilila, da jo odpre. Ko si je s težavo oblekla nedotaknjen kuharski plašč, je v njej vzklilo nezadovoljstvo in razočaranje.",
            "Explanation": "Odpor Maye do odprtja restavracije v hipotezi je v nasprotju z njenimi občutki in motivi, kot so opisani v premisi."
        },
        "Neutral": {
            "Hypothesis": "Po ulici se je širil vonj po žvrgolečih fajitah, ki je bil mamljiv kontrast običajnemu vonju po sveže pečenem kruhu in ekološkem ohrovtu, ki se je širil iz 'Harmony Harvest', priljubljene veganske restavracije v soseski. Nad sosednjo trgovino je plapolal rdeč transparent z napisom 'El Fuego Cantina', ki je napovedoval skorajšnji prihod nove restavracije. Lastnica podjetja Harmony Harvest, Sarah, je pokukala skozi žaluzije, v očeh pa se ji je zoprno zaiskrilo. Konkurenca je lahko dobra stvar, je pomislila. Predstavljala si je živahno kulinarično prizorišče, kjer bosta obe restavraciji zadovoljili različne prehranske želje, a hkrati spodbujali občutek skupnosti.",
            "Explanation": "Hipoteza opisuje prihod mesne restavracije poleg veganske restavracije, dogodek, ki je lahko povezan s scenarijem ali ne."
        }
    },


]

# # Validate that the number of texts matches the number of scores
# if len(example_texts) != len(example_qacm_scores):
#     raise ValueError("The number of example texts must match the number of QACM scores")
#
# # Validate that the number of texts matches the expected number of scenarios
# num_scenarios = 10
# if len(example_texts) != num_scenarios:
#     raise ValueError("The number of example texts must match the number of scenarios")
num_scenarios = 10
# Load the existing JSON file
filename = "../../Results_Final_dataset/FINAL_DATASET.json"
with open(filename, 'r', encoding="utf-8") as file:
    data = json.load(file)

# Update scenarios for the "Historical Events" category
for scenario_idx in range(1, num_scenarios + 1):
    scenario_name = f"Scenario {scenario_idx}"
    data["Fictional Stories"][scenario_name] = {
        "OQACM Score": example_qacm_scores[scenario_idx - 1],  # Set QACM score for each scenario
        "Entailment": {
            "Scenario": example_texts[scenario_idx - 1]["Scenario"],
            "Hypothesis": example_texts[scenario_idx - 1]["Entailment"]["Hypothesis"],
            "Explanation": example_texts[scenario_idx - 1]["Entailment"]["Explanation"]
        },
        "Contradiction": {
            "Scenario": example_texts[scenario_idx - 1]["Scenario"],
            "Hypothesis": example_texts[scenario_idx - 1]["Contradiction"]["Hypothesis"],
            "Explanation": example_texts[scenario_idx - 1]["Contradiction"]["Explanation"]
        },
        "Neutral": {
            "Scenario": example_texts[scenario_idx - 1]["Scenario"],
            "Hypothesis": example_texts[scenario_idx - 1]["Neutral"]["Hypothesis"],
            "Explanation": example_texts[scenario_idx - 1]["Neutral"]["Explanation"]
        }
    }

# Save the updated JSON file
with open(filename, 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("The JSON file has been updated successfully.")

