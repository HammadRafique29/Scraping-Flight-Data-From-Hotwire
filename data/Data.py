# import geolocator as geolocator
airports_names = [ 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina',
                   'Armenia', 'Australia', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
                   'Bermuda', 'Bhutan', 'Bolivia', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
                   'Central African Republic', 'Chad', 'Chile', 'China', 'Ecuador', 'Egypt', 'El Salvador',
                   'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'French Guiana',
                   'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada',
                   'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Iceland', 'India',
                   'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
                   'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan',
                   'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
                   'Luxembourg', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
                   'Nigeria', 'Norway', 'Oman', 'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
                   'Mali', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
                   'Poland', 'Portugal', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
                   'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
                   'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
                   'Solomon Islands', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga',
                   'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
                   'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                   'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe' ]

airports_raw_data = {
    'Afghanistan': {
        'Kabul': '(KBL - Hamid Karzai Intl.)',
    },
    'Albania': {
        'Tirana': '(TIA - Tirana Intl.)',
    },
    'Algeria': {
        'Algiers': '(ALG - Houari Boumediene Airport)',
        'Oran': '(ORN - Oran Es Senia Airport)',
    },
    'Andorra': {
        'Andorra La Vella': '(ALV - Heliport)',
    },
    'Angola': {
        'Luanda': '(LAD - Quatro de Fevereiro Intl.)',
    },
    'Antigua and Barbuda': {
        'St. John\'s': '(ANU - V.C. Bird Intl.)',
    },
    'Argentina': {
        'Buenos Aires': '(EZE - Ministro Pistarini Intl.)',
        'Cordoba': '(COR - Ingeniero Aeronáutico Ambrosio L.V. Taravella Intl.)',
    },
    'Armenia': {
        'Yerevan': '(EVN - Zvartnots Intl.)',
    },
    'Australia': {
        'Sydney': '(SYD - Sydney Kingsford Smith Intl.)',
        'Melbourne': '(MEL - Melbourne Tullamarine Intl.)',
    },
    'Bahrain': {
        'Manama': '(BAH - Bahrain Intl.)'
    },
    'Bangladesh': {
        'Dhaka': '(DAC - Hazrat Shahjalal Intl.)'
    },
    'Barbados': {
        'Bridgetown': '(BGI - Grantley Adams Intl.)'
    },
    'Belarus': {
        'Minsk': '(MSQ - Minsk National Airport)'
    },
    'Belgium': {
        'Brussels': '(BRU - Brussels Airport)'
    },
    'Belize': {
        'Belize City': '(BZE - Philip S. W. Goldson Intl.)'
    },
    'Benin': {
        'Cotonou': '(COO - Cotonou Cadjehoun Airport)'
    },
    'Bermuda': {
        'Hamilton': '(BDA - L.F. Wade Intl.)'
    },
    'Bhutan': {
        'Paro': '(PBH - Paro Intl.)'
    },
    'Bolivia': {
        'La Paz': '(LPB - El Alto Intl.)',
        'Santa Cruz de la Sierra': '(VVI - Viru Viru Intl.)'
    },
    'Cambodia': {
        'Phnom Penh': '(PNH - Phnom Penh Intl.)',
        'Siem Reap': '(REP - Siem Reap Intl.)'
    },
    'Cameroon': {
        'Yaounde': '(NSI - Yaounde Nsimalen Intl.)',
        'Douala': '(DLA - Douala Intl.)'
    },
    'Canada': {
        'Toronto': '(YYZ - Toronto Pearson Intl.)',
        'Vancouver': '(YVR - Vancouver Intl.)',
        'Montreal': '(YUL - Montreal-Trudeau Intl.)',
        'Calgary': '(YYC - Calgary Intl.)',
        'Edmonton': '(YEG - Edmonton Intl.)',
        'Ottawa': '(YOW - Ottawa Macdonald-Cartier Intl.)',
        'Halifax': '(YHZ - Halifax Stanfield Intl.)',
        'Quebec City': '(YQB - Quebec City Jean Lesage Intl.)',
        'Winnipeg': '(YWG - Winnipeg James Armstrong Richardson Intl.)',
        'Victoria': '(YYJ - Victoria Intl.)'
    },
    'Cape Verde': {
        'Praia': '(RAI - Nelson Mandela Intl.)'
    },
    'Central African Republic': {
        'Bangui': '(BGF - Bangui M\'Poko Intl.)'
    },
    'Chad': {
        'N\'Djamena': '(NDJ - N\'Djamena Intl.)'
    },
    'Chile': {
        'Santiago': '(SCL - Comodoro Arturo Merino Benitez Intl.)',
        'Easter Island': '(IPC - Mataveri Intl.)'
    },
    'China': {
        'Beijing': '(PEK - Beijing Capital Intl.)',
        'Shanghai': '(PVG - Shanghai Pudong Intl.)',
        'Hong Kong': '(HKG - Hong Kong Intl.)',
        'Guangzhou': '(CAN - Guangzhou Baiyun Intl.)',
        'Shenzhen': '(SZX - Shenzhen Bao\'an Intl.)',
    },
    'Ecuador': {
        'Quito': '(UIO - Mariscal Sucre Intl.)',
        'Guayaquil': '(GYE - Jose Joaquin de Olmedo Intl.)'
    },
    'Egypt': {
        'Cairo': '(CAI - Cairo Intl.)',
        'Alexandria': '(HBE - Borg El Arab Intl.)'
    },
    'El Salvador': {
        'San Salvador': '(SAL - El Salvador Intl.)'
    },
    'Equatorial Guinea': {
        'Malabo': '(SSG - Malabo Intl.)',
        'Bata': '(BSG - Bata Airport)'
    },
    'Eritrea': {
        'Asmara': '(ASM - Asmara Intl.)'
    },
    'Estonia': {
        'Tallinn': '(TLL - Lennart Meri Tallinn Airport)'
    },
    'Ethiopia': {
        'Addis Ababa': '(ADD - Bole Intl.)'
    },
    'Fiji': {
        'Nadi': '(NAN - Nadi Intl.)',
        'Suva': '(SUV - Nausori Intl.)'
    },
    'Finland': {
        'Helsinki': '(HEL - Helsinki Airport)',
        'Tampere': '(TMP - Tampere-Pirkkala Airport)'
    },
    'France': {
        'Paris': '(CDG - Charles de Gaulle Airport)',
        'Nice': '(NCE - Nice Cote d Azur Airport)',
        'Marseille': '(MRS - Marseille Provence Airport)'
    },
    'French Guiana': {
        'Cayenne': '(CAY - Felix Eboue Airport)'
    },
    'French Polynesia': {
        'Papeete': '(PPT - Faa a International Airport)'
    },
    'Gabon': {
        'Libreville': '(LBV - Leon M\'ba Intl.)',
        'Port Gentil': '(POG - Port Gentil)',
        'Franceville': '(MVB - Mvengue)',
    },
    'Gambia': {
        'Banjul': '(BJL - Banjul Intl.)',
    },
    'Georgia': {
        'Tbilisi': '(TBS - Tbilisi Intl.)',
        'Kutaisi': '(KUT - David the Builder Kutaisi Intl.)',
        'Batumi': '(BUS - Batumi Intl.)',
    },
    'Germany': {
        'Berlin': {
            'Tegel': '(TXL - Berlin Tegel)',
            'Schönefeld': '(SXF - Berlin Schönefeld)',
            'Brandenburg': '(BER - Berlin Brandenburg)',
        },
        'Frankfurt': '(FRA - Frankfurt Intl.)',
        'Munich': '(MUC - Munich Intl.)',
        'Düsseldorf': '(DUS - Düsseldorf Intl.)',
        'Hamburg': '(HAM - Hamburg Airport)',
        'Stuttgart': '(STR - Stuttgart Airport)',
        'Cologne': {
            'Bonn': '(CGN - Cologne Bonn Airport)',
        },
        'Nuremberg': '(NUE - Nuremberg Airport)',
        'Leipzig': {
            'Halle': '(LEJ - Leipzig/Halle Airport)',
        },
    },
    'Ghana': {
        'Accra': '(ACC - Kotoka Intl.)',
        'Kumasi': '(KMS - Kumasi Airport)',
        'Tamale': '(TML - Tamale Airport)',
        'Takoradi': '(TKD - Takoradi Airport)',
    },
    'Greece': {
        'Athens': '(ATH - Eleftherios Venizelos Intl.)',
        'Thessaloniki': '(SKG - Thessaloniki Airport)',
        'Heraklion': '(HER - Heraklion Intl.)',
        'Rhodes': '(RHO - Diagoras Airport)',
        'Chania': '(CHQ - Chania International Airport)',
        'Mykonos': '(JMK - Mykonos Airport)',
    },
    'Grenada': {
        'St. George\'s': '(GND - Maurice Bishop Intl.)',
    },
    'Guatemala': {
        'Guatemala City': {
            'La Aurora': '(GUA - La Aurora Intl.)',
            'Mundo Maya': '(FRS - Mundo Maya International)',
        },
        'Flores': '(FRS - Mundo Maya International)',
    },
    'Guinea': {
        'Conakry': '(CKY - Conakry Intl.)',
    },
    'Guinea-Bissau': {
        'Bissau': '(OXB - Osvaldo Vieira Intl.)',
    },
    'Guyana': {
        'Georgetown': '(GEO - Cheddi Jagan Intl.)',
    },
    'Haiti': {
        'Port-au-Prince': '(PAP - Toussaint Louverture Intl.)',
        'Cap-Haitien': '(CAP - Cap-Haitien Intl.)',
    },
    'Honduras': {
        'Tegucigalpa': '(TGU - Toncontín Intl.)',
        'San Pedro Sula': '(SAP - Ramón Villeda Morales Intl.)'
    },
    'Iceland': {
        'Reykjavik': '(RKV - Reykjavik Airport)',
        'Keflavik': '(KEF - Keflavik International Airport)'
    },
    'India': {
        'New Delhi': '(DEL - Indira Gandhi International Airport)',
        'Mumbai': '(BOM - Chhatrapati Shivaji International Airport)',
        'Chennai': '(MAA - Chennai International Airport)',
        'Kolkata': '(CCU - Netaji Subhas Chandra Bose International Airport)'
    },
    'Indonesia': {
        'Jakarta': '(CGK - Soekarno-Hatta International Airport)',
        'Bali': '(DPS - Ngurah Rai International Airport)',
        'Surabaya': '(SUB - Juanda International Airport)',
        'Medan': '(KNO - Kuala Namu International Airport)'
    },
    'Iran': {
        'Tehran': '(IKA - Imam Khomeini International Airport)',
        'Mashhad': '(MHD - Mashhad International Airport)',
        'Shiraz': '(SYZ - Shiraz International Airport)',
        'Isfahan': '(IFN - Isfahan International Airport)'
    },
    'Iraq': {
        'Baghdad': '(BGW - Baghdad International Airport)',
        'Basra': '(BSR - Basra International Airport)',
        'Erbil': '(EBL - Erbil International Airport)'
    },
    'Ireland': {
        'Dublin': '(DUB - Dublin Airport)',
        'Cork': '(ORK - Cork Airport)',
        'Shannon': '(SNN - Shannon Airport)',
        'Knock': '(NOC - Ireland West Airport Knock)'
    },
    'Israel': {
        'Tel Aviv': '(TLV - Ben Gurion Airport)',
        'Eilat': '(ETH - Eilat Airport)',
        'Haifa': '(HFA - Haifa Airport)'
    },
    'Italy': {
        'Rome': '(FCO - Leonardo da Vinci-Fiumicino Airport)',
        'Milan': '(MXP - Milan Malpensa Airport)',
        'Venice': '(VCE - Venice Marco Polo Airport)',
        'Naples': '(NAP - Naples International Airport)'
    },
    'Jamaica': {
        'Montego Bay': '(MBJ - Sangster International Airport)',
        'Kingston': '(KIN - Norman Manley International Airport)'
    },
    'Japan': {
        'Tokyo': '(NRT - Narita International Airport)',
        'Osaka': '(KIX - Kansai International Airport)',
        'Nagoya': '(NGO - Chubu Centrair International Airport)',
        'Fukuoka': '(FUK - Fukuoka Airport)'
    },
    'Jordan': {
        'Amman': '(AMM - Queen Alia International Airport)',
        'Aqaba': '(AQJ - King Hussein International Airport)'
    },
    'Kazakhstan': {
        'Almaty': '(ALA - Almaty Intl.)',
        'Astana': '(TSE - Nursultan Nazarbayev Intl.)',
    },
    'Kenya': {
        'Nairobi': '(NBO - Jomo Kenyatta Intl.)',
        'Mombasa': '(MBA - Moi Intl.)',
    },
    'Kiribati': {
        'Tarawa': '(TRW - Bonriki Intl.)',
    },
    'Korea, North': {
        'Pyongyang': '(FNJ - Pyongyang Intl.)',
    },
    'Korea, South': {
        'Seoul': '(ICN - Incheon Intl.)',
        'Busan': '(PUS - Gimhae Intl.)',
    },
    'Kosovo': {
        'Pristina': '(PRN - Pristina Intl.)',
    },
    'Kuwait': {
        'Kuwait City': '(KWI - Kuwait Intl.)',
    },
    'Kyrgyzstan': {
        'Bishkek': '(FRU - Manas Intl.)',
    },
    'Laos': {
        'Vientiane': '(VTE - Wattay Intl.)',
        'Luang Prabang': '(LPQ - Luang Prabang Intl.)',
    },
    'Latvia': {
        'Riga': '(RIX - Riga Intl.)',
    },
    'Lebanon': {
        'Beirut': '(BEY - Beirut Rafic Hariri Intl.)',
    },
    'Lesotho': {
        'Maseru': '(MSU - Moshoeshoe I Intl.)',
    },
    'Liberia': {
        'Monrovia': '(ROB - Roberts Intl.)',
    },
    'Libya': {
        'Tripoli': '(TIP - Tripoli Intl.)',
        'Benghazi': '(BEN - Benina Intl.)',
    },
    'Liechtenstein': {
        'Vaduz': '(QVJ - Vaduz Heliport)',
    },
    'Lithuania': {
        'Vilnius': '(VNO - Vilnius Intl.)',
    },
    'Luxembourg': {
        'Luxembourg City': '(LUX - Luxembourg Findel Airport)',
    },
    'Namibia': {
        'Windhoek': '(WDH - Hosea Kutako Intl.)'
    },
    'Nauru': {
        'Yaren District': '(INU - Nauru Intl.)'
    },
    'Nepal': {
        'Kathmandu': '(KTM - Tribhuvan Intl.)'
    },
    'Netherlands': {
        'Amsterdam': '(AMS - Amsterdam Schiphol)',
        'Rotterdam': '(RTM - Rotterdam The Hague Airport)'
    },
    'New Zealand': {
        'Auckland': '(AKL - Auckland Intl.)',
        'Wellington': '(WLG - Wellington Intl.)'
    },
    'Nicaragua': {
        'Managua': '(MGA - Augusto C. Sandino Intl.)'
    },
    'Niger': {
        'Niamey': '(NIM - Diori Hamani Intl.)'
    },
    'Nigeria': {
        'Abuja': '(ABV - Nnamdi Azikiwe Intl.)',
        'Lagos': '(LOS - Murtala Muhammed Intl.)'
    },
    'Norway': {
        'Oslo': '(OSL - Oslo Gardermoen)'
    },
    'Oman': {
        'Muscat': '(MCT - Muscat Intl.)'
    },
    'Macao': {
        'Macao': '(MFM - Macau Intl.)',
    },
    'Macedonia': {
        'Skopje': '(SKP - Skopje Intl.)',
    },
    'Madagascar': {
        'Antananarivo': '(TNR - Ivato Intl.)',
        'Nosy Be': '(NOS - Fascene Airport)',
    },
    'Malawi': {
        'Lilongwe': '(LLW - Kamuzu Intl.)',
    },
    'Malaysia': {
        'Kuala Lumpur': '(KUL - Kuala Lumpur Intl.)',
        'Kota Kinabalu': '(BKI - Kota Kinabalu Intl.)',
        'Penang': '(PEN - Penang Intl.)',
    },
    'Maldives': {
        'Malé': '(MLE - Velana Intl.)',
    },
    'Mali': {
        'Bamako': '(BKO - Bamako-Sénou Intl.)',
    },
    'Pakistan': {
        'Islamabad': '(ISB - Islamabad Intl.)',
        'Karachi': '(KHI - Jinnah Intl.)',
        'Lahore': '(LHE - Allama Iqbal Intl.)',
        'Multan': '(MUX - Multan Intl.)',
        'Peshawar': '(PEW - Bacha Khan Intl.)',
        'Quetta': '(UET - Quetta Intl.)'
    },
    'Palau': {
        'Koror': '(ROR - Roman Tmetuchl Intl.)'
    },
    'Panama': {
        'David': '(DAV - Enrique Malek Intl.)',
        'Panama City': '(PTY - Tocumen Intl.)'
    },
    'Papua New Guinea': {
        'Port Moresby': '(POM - Jacksons Intl.)'
    },
    'Paraguay': {
        'Asuncion': '(ASU - Silvio Pettirossi Intl.)'
    },
    'Peru': {
        'Cusco': '(CUZ - Alejandro Velasco Astete Intl.)',
        'Lima': '(LIM - Jorge Chavez Intl.)'
    },
    'Philippines': {
        'Cebu City': '(CEB - Mactan-Cebu Intl.)',
        'Manila': '(MNL - Ninoy Aquino Intl.)'
    },
    'Poland': {
        'Krakow': '(KRK - John Paul II Intl.)',
        'Warsaw': '(WAW - Frederic Chopin Intl.)'
    },
    'Portugal': {
        'Faro': '(FAO - Faro Intl.)',
        'Lisbon': '(LIS - Humberto Delgado Airport)'
    },
    'Romania': {
        'Bucharest': '(OTP - Henri Coanda Intl.)',
        'Cluj-Napoca': '(CLJ - Avram Iancu Cluj Intl.)',
        'Timisoara': '(TSR - Traian Vuia Intl.)'
    },
    'Russia': {
        'Moscow': '(SVO - Sheremetyevo Intl.)',
        'St. Petersburg': '(LED - Pulkovo Intl.)',
        'Novosibirsk': '(OVB - Tolmachevo Intl.)'
    },
    'Rwanda': {
        'Kigali': '(KGL - Kigali Intl.)'
    },
    'Saint Kitts and Nevis': {
        'Basseterre': '(SKB - Robert L. Bradshaw Intl.)'
    },
    'Saint Lucia': {
        'Castries': '(SLU - George F. L. Charles Airport)'
    },
    'Saint Vincent and the Grenadines': {
        'Kingstown': '(SVD - Argyle Intl.)'
    },
    'Samoa': {
        'Apia': '(APW - Faleolo Intl.)'
    },
    'San Marino': {
        'San Marino': '(RMI - Federico Fellini Intl.)'
    },
    'Sao Tome and Principe': {
        'Sao Tome': '(TMS - Sao Tome Intl.)'
    },
    'Saudi Arabia': {
        'Riyadh': '(RUH - King Khaled Intl.)',
        'Jeddah': '(JED - King Abdulaziz Intl.)',
        'Dammam': '(DMM - King Fahd Intl.)'
    },
    'Senegal': {
        'Dakar': '(DKR - Blaise Diagne Intl.)'
    },
    'Serbia': {
        'Belgrade': '(BEG - Nikola Tesla Intl.)'
    },
    'Seychelles': {
        'Victoria': '(SEZ - Seychelles Intl.)'
    },
    'Sierra Leone': {
        'Freetown': '(FNA - Lungi Intl.)'
    },
    'Singapore': {
        'Singapore': '(SIN - Changi Intl.)'
    },
    'Slovakia': {
        'Bratislava': '(BTS - M. R. Stefanik Airport)'
    },
    'Slovenia': {
        'Ljubljana': '(LJU - Joze Pucnik Airport)'
    },
    'Solomon Islands': {
        'Honiara': '(HIR - Honiara Intl.)'
    },
    'Taiwan': {
        'Taipei': '(TPE - Taiwan Taoyuan Intl.)',
        'Kaohsiung': '(KHH - Kaohsiung Intl.)'
    },
    'Tajikistan': {
        'Dushanbe': '(DYU - Dushanbe Intl.)'
    },
    'Tanzania': {
        'Dar es Salaam': '(DAR - Julius Nyerere Intl.)',
        'Zanzibar City': '(ZNZ - Abeid Amani Karume Intl.)'
    },
    'Thailand': {
        'Bangkok': '(BKK - Suvarnabhumi Airport)',
        'Phuket': '(HKT - Phuket Intl.)'
    },
    'Timor-Leste': {
        'Dili': '(DIL - Presidente Nicolau Lobato Intl.)'
    },
    'Togo': {
        'Lome': '(LFW - Gnassingbe Eyadema Intl.)'
    },
    'Tonga': {
        'Nuku\'alofa': '(TBU - Fua\'amotu Intl.)'
    },
    'Trinidad and Tobago': {
        'Port of Spain': '(POS - Piarco Intl.)'
    },
    'Tunisia': {
        'Tunis': '(TUN - Carthage Intl.)'
    },
    'Turkey': {
        'Istanbul': '(IST - Istanbul Airport)',
        'Ankara': '(ESB - Esenboga Intl.)',
        'Antalya': '(AYT - Antalya Intl.)'
    },
    'Turkmenistan': {
        'Ashgabat': '(ASB - Ashgabat Intl.)'
    },
    'Tuvalu': {
        'Funafuti': '(FUN - Funafuti Intl.)'
    }, 'Uganda': {
        'Entebbe': '(EBB - Entebbe Intl.)'
    },
    'Ukraine': {
        'Kyiv': '(KBP - Kyiv Boryspil Intl.)',
        'Lviv': '(LWO - Lviv Danylo Halytskyi Intl.)'
    },
    'United Arab Emirates': {
        'Dubai': '(DXB - Dubai Intl.)',
        'Abu Dhabi': '(AUH - Abu Dhabi Intl.)'
    },
    'United Kingdom': {
        'London': '(LHR - London Heathrow Airport)',
        'Manchester': '(MAN - Manchester Airport)'
    },
    'United States': {
        'New York': '(JFK - John F. Kennedy Intl.)',
        'Los Angeles': '(LAX - Los Angeles Intl.)',
        'Chicago': '(ORD - Chicago O\'Hare Intl.)'
    },
    'Uruguay': {
        'Montevideo': '(MVD - Carrasco Intl.)'
    },
    'Uzbekistan': {
        'Tashkent': '(TAS - Tashkent Intl.)'
    },
    "Vanuatu": {
        "Port Vila": "(VLI - Bauerfield Intl.)",
    },
    "Venezuela": {
        "Caracas": "(CCS - Simon Bolivar Intl.)",
        "Valencia": "(VLN - Arturo Michelena Intl.)",
        "Maracaibo": "(MAR - La Chinita Intl.)",
        "Barquisimeto": "(BRM - Jacinto Lara Intl.)",
        "Puerto Ordaz": "(PZO - Manuel Carlos Piar Intl.)",
        "Porlamar": "(PMV - Del Caribe Intl. Gen. Santiago Marino)",
    },
    "Vietnam": {
        "Hanoi": "(HAN - Noi Bai Intl.)",
        "Ho Chi Minh City": "(SGN - Tan Son Nhat Intl.)",
        "Da Nang": "(DAD - Da Nang Intl.)",
        "Nha Trang": "(CXR - Cam Ranh Intl.)",
        "Phu Quoc": "(PQC - Phu Quoc Intl.)",
    },
    'Wallis and Futuna': {
        'Futuna Island': '(FUT)',
        'Wallis Island': '(WLS)',
    },
    'Western Sahara': {
        'El Aaiún': '(EUN - Hassan I Airport)',
    },
    'Yemen': {
        'Aden': '(ADE - Aden Intl)',
        'Sanaa': '(SAH - Sanaa Intl)',
        'Taiz': '(TAI - Taiz Intl)',
    },
    'Zambia': {
        'Livingstone': '(LVI - Harry Mwanga Nkumbula Intl)',
        'Lusaka': '(LUN - Kenneth Kaunda Intl)',
        'Ndola': '(NLA - Simon Mwansa Kapwepwe Intl)',
    },
    'Zimbabwe': {
        'Bulawayo': '(BUQ - Joshua Mqabuko Nkomo Intl)',
        'Harare': '(HRE - Robert Gabriel Mugabe Intl)',
        'Victoria Falls': '(VFA - Victoria Falls Intl)',
    }
}

airports_data = {'Kabul': ('(KBL - Hamid Karmic Intl.)', [34.5260109, 69.1776838]),
                 'Tirana': ('(TIA - Tirana Intl.)', [41.330488599999995, 19.82556898393491]),
                 'Algiers': ('(ALG - Houari Boumediene Airport)', [36.7753606, 3.0601882]),
                 'Oran': ('(ORN - Oran Es Senia Airport)', [35.7044415, -0.6502981]),
                 'Andorra La Vella': ('(ALV - Heliport)', [42.5069391, 1.5212467]),
                 'Luanda': ('(LAD - Quatro de Fevereiro Intl.)', [-8.8272699, 13.2439512]),
                 "St. John's": ('(ANU - V.C. Bird Intl.)', [17.1184569, -61.8448509]),
                 'Buenos Aires': ('(EZE - Ministro Pistarini Intl.)', [-34.6075682, -58.4370894]),
                 'Cordoba': ('(COR - Ingeniero Aeronáutico Ambrosio L.V. Taravella Intl.)', [-31.4166867, -64.1834193]),
                 'Yerevan': ('(EVN - Zvartnots Intl.)', [40.1777112, 44.5126233]),
                 'Sydney': ('(SYD - Sydney Kingsford Smith Intl.)', [-33.8698439, 151.2082848]),
                 'Melbourne': ('(MEL - Melbourne Tullamarine Intl.)', [-37.8142176, 144.9631608]),
                 'Manama': ('(BAH - Bahrain Intl.)', [26.2235041, 50.5822436]),
                 'Dhaka': ('(DAC - Hazrat Shahjalal Intl.)', [23.7644025, 90.389015]),
                 'Bridgetown': ('(BGI - Grantley Adams Intl.)', [13.0977832, -59.6184184]),
                 'Minsk': ('(MSQ - Minsk National Airport)', [53.9024716, 27.5618225]),
                 'Brussels': ('(BRU - Brussels Airport)', [50.8465573, 4.351697]),
                 'Belize City': ('(BZE - Philip S. W. Goldson Intl.)', [17.5000543, -88.2003115]),
                 'Cotonou': ('(COO - Cotonou Cadjehoun Airport)', [6.3676953, 2.4252507]),
                 'Hamilton': ('(BDA - L.F. Wade Intl.)', [32.2956076, -64.7827048]),
                 'Paro': ('(PBH - Paro Intl.)', [27.4646365, 89.3183409]),
                 'La Paz': ('(LPB - El Alto Intl.)', [-16.4955455, -68.1336229]),
                 'Santa Cruz de la Sierra': ('(VVI - Viru Viru Intl.)', [-17.7834936, -63.1820853]),
                 'Phnom Penh': ('(PNH - Phnom Penh Intl.)', [11.568271, 104.9224426]),
                 'Siem Reap': ('(REP - Siem Reap Intl.)', [13.3617562, 103.8590321]),
                 'Yaounde': ('(NSI - Yaounde Nsimalen Intl.)', [3.8689867, 11.5213344]),
                 'Douala': ('(DLA - Douala Intl.)', [4.0429408, 9.706203]),
                 'Toronto': ('(YYZ - Toronto Pearson Intl.)', [43.6534733, -79.383961]),
                 'Vancouver': ('(YVR - Vancouver Intl.)', [49.2608724, -123.113952]),
                 'Montreal': ('(YUL - Montreal-Trudeau Intl.)', [45.5031824, -73.5698065]),
                 'Calgary': ('(YYC - Calgary Intl.)', [51.0460954, -114.065465]),
                 'Edmonton': ('(YEG - Edmonton Intl.)', [53.5462055, -113.491241]),
                 'Ottawa': ('(YOW - Ottawa Macdonald-Cartier Intl.)', [45.4208777, -75.6901106]),
                 'Halifax': ('(YHZ - Halifax Stanfield Intl.)', [44.648618, -63.5859487]),
                 'Quebec City': ('(YQB - Quebec City Jean Lesage Intl.)', [46.8137431, -71.2084061]),
                 'Winnipeg': ('(YWG - Winnipeg James Armstrong Richardson Intl.)', [49.8955367, -97.1384584]),
                 'Victoria': ('(SEZ - Seychelles Intl.)', [-4.6232085, 55.452359]),
                 'Praia': ('(RAI - Nelson Mandela Intl.)', [14.9162811, -23.5095095]),
                 'Bangui': ("(BGF - Bangui M'Poko Intl.)", [4.3907153, 18.5509126]),
                 "N'Djamena": ("(NDJ - N'Djamena Intl.)", [12.1191543, 15.0502758]),
                 'Santiago': ('(SCL - Comodoro Arturo Merino Benitez Intl.)', [-33.4377756, -70.6504502]),
                 'Easter Island': ('(IPC - Mataveri Intl.)', [-27.128500000000003, -109.33602969583333]),
                 'Beijing': ('(PEK - Beijing Capital Intl.)', [39.906217, 116.3912757]),
                 'Shanghai': ('(PVG - Shanghai Pudong Intl.)', [31.2322758, 121.4692071]),
                 'Hong Kong': ('(HKG - Hong Kong Intl.)', [22.2793278, 114.1628131]),
                 'Guangzhou': ('(CAN - Guangzhou Baiyun Intl.)', [23.1301964, 113.2592945]),
                 'Shenzhen': ("(SZX - Shenzhen Bao'an Intl.)", [22.5445741, 114.0545429]),
                 'Quito': ('(UIO - Mariscal Sucre Intl.)', [-0.2201641, -78.5123274]),
                 'Guayaquil': ('(GYE - Jose Joaquin de Olmedo Intl.)', [-2.1900563, -79.8868741]),
                 'Cairo': ('(CAI - Cairo Intl.)', [30.0443879, 31.2357257]),
                 'Alexandria': ('(HBE - Borg El Arab Intl.)', [31.1991806, 29.8951716]),
                 'San Salvador': ('(SAL - El Salvador Intl.)', [13.6989939, -89.1914249]),
                 'Malabo': ('(SSG - Malabo Intl.)', [3.752831, 8.7800693]),
                 'Bata': ('(BSG - Bata Airport)', [1.82385155, 9.856166243652915]),
                 'Asmara': ('(ASM - Asmara Intl.)', [15.3389667, 38.9326763]),
                 'Tallinn': ('(TLL - Lennart Meri Tallinn Airport)', [59.4372155, 24.7453688]),
                 'Addis Ababa': ('(ADD - Bole Intl.)', [9.0107934, 38.7612525]),
                 'Nadi': ('(NAN - Nadi Intl.)', [-17.7992725, 177.4178549]),
                 'Suva': ('(SUV - Nausori Intl.)', [-18.1415884, 178.4421662]),
                 'Helsinki': ('(HEL - Helsinki Airport)', [60.1674881, 24.9427473]),
                 'Tampere': ('(TMP - Tampere-Pirkkala Airport)', [61.4980214, 23.7603118]),
                 'Paris': ('(CDG - Charles de Gaulle Airport)', [48.8534951, 2.3483915]),
                 'Nice': ('(NCE - Nice Cote d Azur Airport)', [43.7009358, 7.2683912]),
                 'Marseille': ('(MRS - Marseille Provence Airport)', [43.2961743, 5.3699525]),
                 'Cayenne': ('(CAY - Felix Eboue Airport)', [4.9371143, -52.3258307]),
                 'Papeete': ('(PPT - Faa a International Airport)', [-17.5373835, -149.5659964]),
                 'Libreville': ("(LBV - Leon M'ba Intl.)", [0.4052012, 9.438551]),
                 'Port Gentil': ('(POG - Port Gentil)', [-0.7151966, 8.7787919]),
                 'Franceville': ('(MVB - Mvengue)', [-1.634363, 13.589513]),
                 'Banjul': ('(BJL - Banjul Intl.)', [13.4410165, -16.56275092072591]),
                 'Tbilisi': ('(TBS - Tbilisi Intl.)', [41.6934591, 44.8014495]),
                 'Kutaisi': ('(KUT - David the Builder Kutaisi Intl.)', [42.2716078, 42.7054475]),
                 'Batumi': ('(BUS - Batumi Intl.)', [41.6509502, 41.6360085]), 'Berlin': (
        {'Tegel': '(TXL - Berlin Tegel)', 'Schönefeld': '(SXF - Berlin Schönefeld)',
         'Brandenburg': '(BER - Berlin Brandenburg)'}, [52.5170365, 13.3888599]),
                 'Frankfurt': ('(FRA - Frankfurt Intl.)', [50.1106444, 8.6820917]),
                 'Munich': ('(MUC - Munich Intl.)', [48.1371079, 11.5753822]),
                 'Düsseldorf': ('(DUS - Düsseldorf Intl.)', [51.2254018, 6.7763137]),
                 'Hamburg': ('(HAM - Hamburg Airport)', [53.550341, 10.000654]),
                 'Stuttgart': ('(STR - Stuttgart Airport)', [48.7784485, 9.1800132]),
                 'Cologne': ({'Bonn': '(CGN - Cologne Bonn Airport)'}, [50.938361, 6.959974]),
                 'Nuremberg': ('(NUE - Nuremberg Airport)', [49.453872, 11.077298]),
                 'Leipzig': ({'Halle': '(LEJ - Leipzig/Halle Airport)'}, [51.3406321, 12.3747329]),
                 'Accra': ('(ACC - Kotoka Intl.)', [5.5571096, -0.2012376]),
                 'Kumasi': ('(KMS - Kumasi Airport)', [6.6985605, -1.6233086]),
                 'Tamale': ('(TML - Tamale Airport)', [9.4051992, -0.8423986]),
                 'Takoradi': ('(TKD - Takoradi Airport)', [4.887401, -1.7519316]),
                 'Athens': ('(ATH - Eleftherios Venizelos Intl.)', [37.9839412, 23.7283052]),
                 'Thessaloniki': ('(SKG - Thessaloniki Airport)', [40.6403167, 22.9352716]),
                 'Heraklion': ('(HER - Heraklion Intl.)', [35.33908, 25.1332843]),
                 'Rhodes': ('(RHO - Diagoras Airport)', [36.17262995, 27.919418145633188]),
                 'Chania': ('(CHQ - Chania International Airport)', [35.5120831, 24.0191544]),
                 'Mykonos': ('(JMK - Mykonos Airport)', [37.45139365, 25.39231486780794]),
                 "St. George's": ('(GND - Maurice Bishop Intl.)', [12.0535331, -61.751805]), 'Guatemala City': (
        {'La Aurora': '(GUA - La Aurora Intl.)', 'Mundo Maya': '(FRS - Mundo Maya International)'},
        [14.6222328, -90.5185188]), 'Flores': ('(FRS - Mundo Maya International)', [16.9298524, -89.8914817]),
                 'Conakry': ('(CKY - Conakry Intl.)', [9.5170602, -13.6998434]),
                 'Bissau': ('(OXB - Osvaldo Vieira Intl.)', [11.861324, -15.583055]),
                 'Georgetown': ('(GEO - Cheddi Jagan Intl.)', [6.8137426, -58.1624465]),
                 'Port-au-Prince': ('(PAP - Toussaint Louverture Intl.)', [18.547327, -72.3395928]),
                 'Cap-Haitien': ('(CAP - Cap-Haitien Intl.)', [19.7595236, -72.2008068]),
                 'Tegucigalpa': ('(TGU - Toncontín Intl.)', [14.1057433, -87.2040052]),
                 'San Pedro Sula': ('(SAP - Ramón Villeda Morales Intl.)', [15.5062156, -88.0248937]),
                 'Reykjavik': ('(RKV - Reykjavik Airport)', [64.145981, -21.9422367]),
                 'Keflavik': ('(KEF - Keflavik International Airport)', [63.9997694, -22.5565373]),
                 'New Delhi': ('(DEL - Indira Gandhi International Airport)', [28.6138954, 77.2090057]),
                 'Mumbai': ('(BOM - Chhatrapati Shivaji International Airport)', [19.0785451, 72.878176]),
                 'Chennai': ('(MAA - Chennai International Airport)', [13.0836939, 80.270186]),
                 'Kolkata': ('(CCU - Netaji Subhas Chandra Bose International Airport)', [22.5726459, 88.3638953]),
                 'Jakarta': ('(CGK - Soekarno-Hatta International Airport)', [-6.1752489, 106.8270462]),
                 'Bali': ('(DPS - Ngurah Rai International Airport)', [-8.3304977, 115.0906401]),
                 'Surabaya': ('(SUB - Juanda International Airport)', [-7.2459717, 112.7378266]),
                 'Medan': ('(KNO - Kuala Namu International Airport)', [3.5896654, 98.6738261]),
                 'Tehran': ('(IKA - Imam Khomeini International Airport)', [35.6892523, 51.3896004]),
                 'Mashhad': ('(MHD - Mashhad International Airport)', [36.2974945, 59.6059232]),
                 'Shiraz': ('(SYZ - Shiraz International Airport)', [29.6060218, 52.5378041]),
                 'Isfahan': ('(IFN - Isfahan International Airport)', [32.6707877, 51.6650002]),
                 'Baghdad': ('(BGW - Baghdad International Airport)', [33.3061701, 44.3872213]),
                 'Basra': ('(BSR - Basra International Airport)', [30.4952371, 47.8090981]),
                 'Erbil': ('(EBL - Erbil International Airport)', [36.1911653, 44.0094294]),
                 'Dublin': ('(DUB - Dublin Airport)', [53.3498006, -6.2602964]),
                 'Cork': ('(ORK - Cork Airport)', [51.897077, -8.4654674]),
                 'Shannon': ('(SNN - Shannon Airport)', [52.7093263, -8.876893685751469]),
                 'Knock': ('(NOC - Ireland West Airport Knock)', [52.6284891, -9.3325659]),
                 'Tel Aviv': ('(TLV - Ben Gurion Airport)', [32.0852997, 34.7818064]),
                 'Eilat': ('(ETH - Eilat Airport)', [29.5569348, 34.9497949]),
                 'Haifa': ('(HFA - Haifa Airport)', [32.8191218, 34.9983856]),
                 'Rome': ('(FCO - Leonardo da Vinci-Fiumicino Airport)', [41.8933203, 12.4829321]),
                 'Milan': ('(MXP - Milan Malpensa Airport)', [45.4641943, 9.1896346]),
                 'Venice': ('(VCE - Venice Marco Polo Airport)', [45.4371908, 12.3345898]),
                 'Naples': ('(NAP - Naples International Airport)', [40.8358846, 14.2487679]),
                 'Montego Bay': ('(MBJ - Sangster International Airport)', [18.4724603, -77.9217357]),
                 'Kingston': ('(KIN - Norman Manley International Airport)', [17.9712148, -76.7928128]),
                 'Tokyo': ('(NRT - Narita International Airport)', [35.6812665, 139.757653]),
                 'Osaka': ('(KIX - Kansai International Airport)', [34.661629000000005, 135.49992679245517]),
                 'Nagoya': ('(NGO - Chubu Centrair International Airport)', [35.1851045, 136.8998438]),
                 'Fukuoka': ('(FUK - Fukuoka Airport)', [33.6251241, 130.6180016]),
                 'Amman': ('(AMM - Queen Alia International Airport)', [31.9515694, 35.9239625]),
                 'Aqaba': ('(AQJ - King Hussein International Airport)', [29.5266483, 35.0075433]),
                 'Almaty': ('(ALA - Almaty Intl.)', [43.2363924, 76.9457275]),
                 'Astana': ('(TSE - Nursultan Nazarbayev Intl.)', [51.1282205, 71.4306682]),
                 'Nairobi': ('(NBO - Jomo Kenyatta Intl.)', [-1.2832533, 36.8172449]),
                 'Mombasa': ('(MBA - Moi Intl.)', [-4.05052, 39.667169]),
                 'Tarawa': ('(TRW - Bonriki Intl.)', [1.4845541999999998, 172.96896482000938]),
                 'Seoul': ('(ICN - Incheon Intl.)', [40.7477981, -73.9872728]),
                 'Busan': ('(PUS - Gimhae Intl.)', [36.2861972, 126.8943083]),
                 'Pristina': ('(PRN - Pristina Intl.)', [42.6638771, 21.1640849]),
                 'Kuwait City': ('(KWI - Kuwait Intl.)', [29.3796532, 47.9734174]),
                 'Bishkek': ('(FRU - Manas Intl.)', [42.8777895, 74.6066926]),
                 'Vientiane': ('(VTE - Wattay Intl.)', [17.9640988, 102.6133707]),
                 'Luang Prabang': ('(LPQ - Luang Prabang Intl.)', [19.8887438, 102.135898]),
                 'Riga': ('(RIX - Riga Intl.)', [56.9493977, 24.1051846]),
                 'Beirut': ('(BEY - Beirut Rafic Hariri Intl.)', [33.88922645, 35.50255852895232]),
                 'Maseru': ('(MSU - Moshoeshoe I Intl.)', [-29.5816942, 27.8243208]),
                 'Monrovia': ('(ROB - Roberts Intl.)', [6.328034, -10.797788]),
                 'Tripoli': ('(TIP - Tripoli Intl.)', [32.896672, 13.1777923]),
                 'Benghazi': ('(BEN - Benina Intl.)', [32.1288331, 20.0817204]),
                 'Vaduz': ('(QVJ - Vaduz Heliport)', [47.1393131, 9.5225926]),
                 'Vilnius': ('(VNO - Vilnius Intl.)', [54.6870458, 25.2829111]),
                 'Luxembourg City': ('(LUX - Luxembourg Findel Airport)', [49.6112768, 6.129799]),
                 'Windhoek': ('(WDH - Hosea Kutako Intl.)', [-22.5776104, 17.0772739]),
                 'Yaren District': ('(INU - Nauru Intl.)', [-0.5471014, 166.9164002]),
                 'Kathmandu': ('(KTM - Tribhuvan Intl.)', [27.708317, 85.3205817]),
                 'Amsterdam': ('(AMS - Amsterdam Schiphol)', [52.3730796, 4.8924534]),
                 'Rotterdam': ('(RTM - Rotterdam The Hague Airport)', [51.9244424, 4.47775]),
                 'Auckland': ('(AKL - Auckland Intl.)', [-36.852095, 174.7631803]),
                 'Wellington': ('(WLG - Wellington Intl.)', [-41.2887953, 174.7772114]),
                 'Managua': ('(MGA - Augusto C. Sandino Intl.)', [12.1544035, -86.2737642]),
                 'Niamey': ('(NIM - Diori Hamani Intl.)', [13.524834, 2.109823]),
                 'Abuja': ('(ABV - Nnamdi Azikiwe Intl.)', [9.0643305, 7.4892974]),
                 'Lagos': ('(LOS - Murtala Muhammed Intl.)', [6.4550575, 3.3941795]),
                 'Oslo': ('(OSL - Oslo Gardermoen)', [59.9133301, 10.7389701]),
                 'Muscat': ('(MCT - Muscat Intl.)', [23.5882019, 58.3829448]),
                 'Macao': ('(MFM - Macau Intl.)', [22.1899448, 113.5380454]),
                 'Skopje': ('(SKP - Skopje Intl.)', [41.9961816, 21.4319213]),
                 'Antananarivo': ('(TNR - Ivato Intl.)', [-18.779148749999997, 46.71217161656727]),
                 'Nosy Be': ('(NOS - Fascene Airport)', [-13.311952999999999, 48.253398632406366]),
                 'Lilongwe': ('(LLW - Kamuzu Intl.)', [-13.9875107, 33.768144]),
                 'Kuala Lumpur': ('(KUL - Kuala Lumpur Intl.)', [3.1516964, 101.6942371]),
                 'Kota Kinabalu': ('(BKI - Kota Kinabalu Intl.)', [5.9780066, 116.0728988]),
                 'Penang': ('(PEN - Penang Intl.)', [5.4065013, 100.2559077]),
                 'Malé': ('(MLE - Velana Intl.)', [4.1779879, 73.5107387]),
                 'Bamako': ('(BKO - Bamako-Sénou Intl.)', [12.61326555, -7.984739136241295]),
                 'Islamabad': ('(ISB - Islamabad Intl.)', [33.6938118, 73.0651511]),
                 'Karachi': ('(KHI - Jinnah Intl.)', [24.8546842, 67.0207055]),
                 'Lahore': ('(LHE - Allama Iqbal Intl.)', [31.5656822, 74.3141829]),
                 'Multan': ('(MUX - Multan Intl.)', [30.197838, 71.4719683]),
                 'Peshawar': ('(PEW - Bacha Khan Intl.)', [34.0123846, 71.5787458]),
                 'Quetta': ('(UET - Quetta Intl.)', [30.1957677, 67.0172447]),
                 'Koror': ('(ROR - Roman Tmetuchl Intl.)', [7.343275, 134.4766767]),
                 'David': ('(DAV - Enrique Malek Intl.)', [8.4949423, -82.48261591569641]),
                 'Panama City': ('(PTY - Tocumen Intl.)', [8.9714493, -79.5341802]),
                 'Port Moresby': ('(POM - Jacksons Intl.)', [-9.4743301, 147.1599504]),
                 'Asuncion': ('(ASU - Silvio Pettirossi Intl.)', [-25.2800459, -57.6343814]),
                 'Cusco': ('(CUZ - Alejandro Velasco Astete Intl.)', [-13.5170887, -71.9785356]),
                 'Lima': ('(LIM - Jorge Chavez Intl.)', [-12.0621065, -77.0365256]),
                 'Cebu City': ('(CEB - Mactan-Cebu Intl.)', [10.2931062, 123.9020773]),
                 'Manila': ('(MNL - Ninoy Aquino Intl.)', [14.5948914, 120.9782618]),
                 'Krakow': ('(KRK - John Paul II Intl.)', [50.0619474, 19.9368564]),
                 'Warsaw': ('(WAW - Frederic Chopin Intl.)', [52.2319581, 21.0067249]),
                 'Faro': ('(FAO - Faro Intl.)', [37.0162727, -7.9351771]),
                 'Lisbon': ('(LIS - Humberto Delgado Airport)', [38.7077507, -9.1365919]),
                 'Bucharest': ('(OTP - Henri Coanda Intl.)', [44.4361414, 26.1027202]),
                 'Cluj-Napoca': ('(CLJ - Avram Iancu Cluj Intl.)', [46.769379, 23.5899542]),
                 'Timisoara': ('(TSR - Traian Vuia Intl.)', [45.7538355, 21.2257474]),
                 'Moscow': ('(SVO - Sheremetyevo Intl.)', [55.7504461, 37.6174943]),
                 'St. Petersburg': ('(LED - Pulkovo Intl.)', [59.938732, 30.316229]),
                 'Novosibirsk': ('(OVB - Tolmachevo Intl.)', [55.0288307, 82.9226887]),
                 'Kigali': ('(KGL - Kigali Intl.)', [-1.950851, 30.061507]),
                 'Basseterre': ('(SKB - Robert L. Bradshaw Intl.)', [17.2960919, -62.722301]),
                 'Castries': ('(SLU - George F. L. Charles Airport)', [13.90904385, -60.97792414113452]),
                 'Kingstown': ('(SVD - Argyle Intl.)', [13.1561864, -61.2279621]),
                 'Apia': ('(APW - Faleolo Intl.)', [-13.8344639, -171.7649144]),
                 'San Marino': ('(RMI - Federico Fellini Intl.)', [43.9458623, 12.458306]),
                 'Sao Tome': ('(TMS - Sao Tome Intl.)', [0.3389242, 6.7313031]),
                 'Riyadh': ('(RUH - King Khaled Intl.)', [24.638916, 46.7160104]),
                 'Jeddah': ('(JED - King Abdulaziz Intl.)', [21.5810088, 39.1653612]),
                 'Dammam': ('(DMM - King Fahd Intl.)', [26.4367824, 50.1039991]),
                 'Dakar': ('(DKR - Blaise Diagne Intl.)', [14.693425, -17.447938]),
                 'Belgrade': ('(BEG - Nikola Tesla Intl.)', [44.8178131, 20.4568974]),
                 'Freetown': ('(FNA - Lungi Intl.)', [8.479004, -13.26795]),
                 'Singapore': ('(SIN - Changi Intl.)', [1.357107, 103.8194992]),
                 'Bratislava': ('(BTS - M. R. Stefanik Airport)', [48.1516988, 17.1093063]),
                 'Ljubljana': ('(LJU - Joze Pucnik Airport)', [46.0500268, 14.5069289]),
                 'Honiara': ('(HIR - Honiara Intl.)', [-9.437797549999999, 159.9624174786047]),
                 'Taipei': ('(TPE - Taiwan Taoyuan Intl.)', [25.0375198, 121.5636796]),
                 'Kaohsiung': ('(KHH - Kaohsiung Intl.)', [22.6203348, 120.3120375]),
                 'Dushanbe': ('(DYU - Dushanbe Intl.)', [38.585694700000005, 68.7603746751885]),
                 'Dar es Salaam': ('(DAR - Julius Nyerere Intl.)', [-6.8160837, 39.2803583]),
                 'Zanzibar City': ('(ZNZ - Abeid Amani Karume Intl.)', [-6.1664908, 39.2074312]),
                 'Bangkok': ('(BKK - Suvarnabhumi Airport)', [13.7524938, 100.4935089]),
                 'Phuket': ('(HKT - Phuket Intl.)', [7.9366015, 98.3529292]),
                 'Dili': ('(DIL - Presidente Nicolau Lobato Intl.)', [-8.5536809, 125.5784093]),
                 'Lome': ('(LFW - Gnassingbe Eyadema Intl.)', [6.130419, 1.215829]),
                 "Nuku'alofa": ("(TBU - Fua'amotu Intl.)", [-21.1343401, -175.201808]),
                 'Port of Spain': ('(POS - Piarco Intl.)', [10.6572678, -61.5180173]),
                 'Tunis': ('(TUN - Carthage Intl.)', [33.8439408, 9.400138]),
                 'Istanbul': ('(IST - Istanbul Airport)', [41.0091982, 28.9662187]),
                 'Ankara': ('(ESB - Esenboga Intl.)', [39.9207886, 32.8540482]),
                 'Antalya': ('(AYT - Antalya Intl.)', [36.8872942, 30.7074549]),
                 'Ashgabat': ('(ASB - Ashgabat Intl.)', [37.9404648, 58.3823487]),
                 'Funafuti': ('(FUN - Funafuti Intl.)', [-8.5199633, 179.1982548]),
                 'Entebbe': ('(EBB - Entebbe Intl.)', [0.0611715, 32.4698564]),
                 'Kyiv': ('(KBP - Kyiv Boryspil Intl.)', [50.4500336, 30.5241361]),
                 'Lviv': ('(LWO - Lviv Danylo Halytskyi Intl.)', [49.841952, 24.0315921]),
                 'Dubai': ('(DXB - Dubai Intl.)', [25.074282349999997, 55.18853865430702]),
                 'Abu Dhabi': ('(AUH - Abu Dhabi Intl.)', [24.4538352, 54.3774014]),
                 'London': ('(LHR - London Heathrow Airport)', [51.5073359, -0.12765]),
                 'Manchester': ('(MAN - Manchester Airport)', [53.4794892, -2.2451148]),
                 'New York': ('(JFK - John F. Kennedy Intl.)', [40.7127281, -74.0060152]),
                 'Los Angeles': ('(LAX - Los Angeles Intl.)', [34.0536909, -118.242766]),
                 'Chicago': ("(ORD - Chicago O'Hare Intl.)", [41.8755616, -87.6244212]),
                 'Montevideo': ('(MVD - Carrasco Intl.)', [-34.9058916, -56.1913095]),
                 'Tashkent': ('(TAS - Tashkent Intl.)', [41.3123363, 69.2787079]),
                 'Port Vila': ('(VLI - Bauerfield Intl.)', [-17.7414972, 168.3150163]),
                 'Caracas': ('(CCS - Simon Bolivar Intl.)', [10.5060934, -66.9146008]),
                 'Valencia': ('(VLN - Arturo Michelena Intl.)', [10.170026, -68.0003987]),
                 'Maracaibo': ('(MAR - La Chinita Intl.)', [10.6498095, -71.6443596]),
                 'Barquisimeto': ('(BRM - Jacinto Lara Intl.)', [10.0774374, -69.3222293]),
                 'Puerto Ordaz': ('(PZO - Manuel Carlos Piar Intl.)', [8.2750351, -62.7558263]),
                 'Porlamar': ('(PMV - Del Caribe Intl. Gen. Santiago Marino)', [10.9635839, -63.8464509]),
                 'Hanoi': ('(HAN - Noi Bai Intl.)', [21.0294498, 105.8544441]),
                 'Ho Chi Minh City': ('(SGN - Tan Son Nhat Intl.)', [10.7764772, 106.701938]),
                 'Da Nang': ('(DAD - Da Nang Intl.)', [16.068, 108.212]),
                 'Nha Trang': ('(CXR - Cam Ranh Intl.)', [12.2431693, 109.1898675]),
                 'Phu Quoc': ('(PQC - Phu Quoc Intl.)', [10.2153093, 103.9880443]),
                 'Futuna Island': ('(FUT)', [-14.276851, -178.14234997654432]),
                 'Wallis Island': ('(WLS)', [-13.2846405, -176.20665679493294]),
                 'Aden': ('(ADE - Aden Intl)', [12.833333, 44.916667]),
                 'Sanaa': ('(SAH - Sanaa Intl)', [15.3538569, 44.2058841]),
                 'Taiz': ('(TAI - Taiz Intl)', [13.4115414, 43.5570871]),
                 'Livingstone': ('(LVI - Harry Mwanga Nkumbula Intl)', [-17.853135, 25.861429]),
                 'Lusaka': ('(LUN - Kenneth Kaunda Intl)', [-15.4163395, 28.2818414]),
                 'Ndola': ('(NLA - Simon Mwansa Kapwepwe Intl)', [-12.9693056, 28.6365894]),
                 'Bulawayo': ('(BUQ - Joshua Mqabuko Nkomo Intl)', [-20.1053948, 28.5426856]),
                 'Harare': ('(HRE - Robert Gabriel Mugabe Intl)', [-17.831773, 31.045686]),
                 'Victoria Falls': ('(VFA - Victoria Falls Intl)', [-17.9229035, 25.8490239])}

second_data = {'Kabul': ('Kabul (KBL - Hamid Karzai Intl.)', [34.5260109, 69.1776838], 'Afghanistan'),
               'Tirana': ('Tirana (TIA - Tirana Intl.)', [41.330488599999995, 19.82556898393491], 'Albania'),
               'Algiers': ('Algiers (ALG - Houari Boumediene Airport)', [36.7753606, 3.0601882], 'Algeria'),
               'Oran': ('Oran (ORN - Oran Es Senia Airport)', [35.7044415, -0.6502981], 'Algeria'),
               'Andorra La Vella': ('Andorra La Vella (ALV - Heliport)', [42.5069391, 1.5212467], 'Andorra'),
               'Luanda': ('Luanda (LAD - Quatro de Fevereiro Intl.)', [-8.8272699, 13.2439512], 'Angola'),
               "St. John's": ("St. John's (ANU - V.C. Bird Intl.)", [17.1184569, -61.8448509], 'Antigua and Barbuda'),
               'Buenos Aires': (
               'Buenos Aires (EZE - Ministro Pistarini Intl.)', [-34.6075682, -58.4370894], 'Argentina'), 'Cordoba': (
    'Cordoba (COR - Ingeniero Aeronáutico Ambrosio L.V. Taravella Intl.)', [-31.4166867, -64.1834193], 'Argentina'),
               'Yerevan': ('Yerevan (EVN - Zvartnots Intl.)', [40.1777112, 44.5126233], 'Armenia'),
               'Sydney': ('Sydney (SYD - Sydney Kingsford Smith Intl.)', [-33.8698439, 151.2082848], 'Australia'),
               'Melbourne': ('Melbourne (MEL - Melbourne Tullamarine Intl.)', [-37.8142176, 144.9631608], 'Australia'),
               'Manama': ('Manama (BAH - Bahrain Intl.)', [26.2235041, 50.5822436], 'Bahrain'),
               'Dhaka': ('Dhaka (DAC - Hazrat Shahjalal Intl.)', [23.7644025, 90.389015], 'Bangladesh'),
               'Bridgetown': ('Bridgetown (BGI - Grantley Adams Intl.)', [13.0977832, -59.6184184], 'Barbados'),
               'Minsk': ('Minsk (MSQ - Minsk National Airport)', [53.9024716, 27.5618225], 'Belarus'),
               'Brussels': ('Brussels (BRU - Brussels Airport)', [50.8465573, 4.351697], 'Belgium'),
               'Belize City': ('Belize City (BZE - Philip S. W. Goldson Intl.)', [17.5000543, -88.2003115], 'Belize'),
               'Cotonou': ('Cotonou (COO - Cotonou Cadjehoun Airport)', [6.3676953, 2.4252507], 'Benin'),
               'Hamilton': ('Hamilton (BDA - L.F. Wade Intl.)', [32.2956076, -64.7827048], 'Bermuda'),
               'Paro': ('Paro (PBH - Paro Intl.)', [27.4646365, 89.3183409], 'Bhutan'),
               'La Paz': ('La Paz (LPB - El Alto Intl.)', [-16.4955455, -68.1336229], 'Bolivia'),
               'Santa Cruz de la Sierra': (
               'Santa Cruz de la Sierra (VVI - Viru Viru Intl.)', [-17.7834936, -63.1820853], 'Bolivia'),
               'Phnom Penh': ('Phnom Penh (PNH - Phnom Penh Intl.)', [11.568271, 104.9224426], 'Cambodia'),
               'Siem Reap': ('Siem Reap (REP - Siem Reap Intl.)', [13.3617562, 103.8590321], 'Cambodia'),
               'Yaounde': ('Yaounde (NSI - Yaounde Nsimalen Intl.)', [3.8689867, 11.5213344], 'Cameroon'),
               'Douala': ('Douala (DLA - Douala Intl.)', [4.0429408, 9.706203], 'Cameroon'),
               'Toronto': ('Toronto (YYZ - Toronto Pearson Intl.)', [43.6534733, -79.383961], 'Canada'),
               'Vancouver': ('Vancouver (YVR - Vancouver Intl.)', [49.2608724, -123.113952], 'Canada'),
               'Montreal': ('Montreal (YUL - Montreal-Trudeau Intl.)', [45.5031824, -73.5698065], 'Canada'),
               'Calgary': ('Calgary (YYC - Calgary Intl.)', [51.0460954, -114.065465], 'Canada'),
               'Edmonton': ('Edmonton (YEG - Edmonton Intl.)', [53.5462055, -113.491241], 'Canada'),
               'Ottawa': ('Ottawa (YOW - Ottawa Macdonald-Cartier Intl.)', [45.4208777, -75.6901106], 'Canada'),
               'Halifax': ('Halifax (YHZ - Halifax Stanfield Intl.)', [44.648618, -63.5859487], 'Canada'),
               'Quebec City': (
               'Quebec City (YQB - Quebec City Jean Lesage Intl.)', [46.8137431, -71.2084061], 'Canada'), 'Winnipeg': (
    'Winnipeg (YWG - Winnipeg James Armstrong Richardson Intl.)', [49.8955367, -97.1384584], 'Canada'),
               'Victoria': ('Victoria (SEZ - Seychelles Intl.)', [-4.6232085, 55.452359], 'Seychelles'),
               'Praia': ('Praia (RAI - Nelson Mandela Intl.)', [14.9162811, -23.5095095], 'Cape Verde'),
               'Bangui': ("Bangui (BGF - Bangui M'Poko Intl.)", [4.3907153, 18.5509126], 'Central African Republic'),
               "N'Djamena": ("N'Djamena (NDJ - N'Djamena Intl.)", [12.1191543, 15.0502758], 'Chad'), 'Santiago': (
    'Santiago (SCL - Comodoro Arturo Merino Benitez Intl.)', [-33.4377756, -70.6504502], 'Chile'), 'Easter Island': (
    'Easter Island (IPC - Mataveri Intl.)', [-27.128500000000003, -109.33602969583333], 'Chile'),
               'Beijing': ('Beijing (PEK - Beijing Capital Intl.)', [39.906217, 116.3912757], 'China'),
               'Shanghai': ('Shanghai (PVG - Shanghai Pudong Intl.)', [31.2322758, 121.4692071], 'China'),
               'Hong Kong': ('Hong Kong (HKG - Hong Kong Intl.)', [22.2793278, 114.1628131], 'China'),
               'Guangzhou': ('Guangzhou (CAN - Guangzhou Baiyun Intl.)', [23.1301964, 113.2592945], 'China'),
               'Shenzhen': ("Shenzhen (SZX - Shenzhen Bao'an Intl.)", [22.5445741, 114.0545429], 'China'),
               'Quito': ('Quito (UIO - Mariscal Sucre Intl.)', [-0.2201641, -78.5123274], 'Ecuador'),
               'Guayaquil': ('Guayaquil (GYE - Jose Joaquin de Olmedo Intl.)', [-2.1900563, -79.8868741], 'Ecuador'),
               'Cairo': ('Cairo (CAI - Cairo Intl.)', [30.0443879, 31.2357257], 'Egypt'),
               'Alexandria': ('Alexandria (HBE - Borg El Arab Intl.)', [31.1991806, 29.8951716], 'Egypt'),
               'San Salvador': ('San Salvador (SAL - El Salvador Intl.)', [13.6989939, -89.1914249], 'El Salvador'),
               'Malabo': ('Malabo (SSG - Malabo Intl.)', [3.752831, 8.7800693], 'Equatorial Guinea'),
               'Bata': ('Bata (BSG - Bata Airport)', [1.82385155, 9.856166243652915], 'Equatorial Guinea'),
               'Asmara': ('Asmara (ASM - Asmara Intl.)', [15.3389667, 38.9326763], 'Eritrea'),
               'Tallinn': ('Tallinn (TLL - Lennart Meri Tallinn Airport)', [59.4372155, 24.7453688], 'Estonia'),
               'Addis Ababa': ('Addis Ababa (ADD - Bole Intl.)', [9.0107934, 38.7612525], 'Ethiopia'),
               'Nadi': ('Nadi (NAN - Nadi Intl.)', [-17.7992725, 177.4178549], 'Fiji'),
               'Suva': ('Suva (SUV - Nausori Intl.)', [-18.1415884, 178.4421662], 'Fiji'),
               'Helsinki': ('Helsinki (HEL - Helsinki Airport)', [60.1674881, 24.9427473], 'Finland'),
               'Tampere': ('Tampere (TMP - Tampere-Pirkkala Airport)', [61.4980214, 23.7603118], 'Finland'),
               'Paris': ('Paris (CDG - Charles de Gaulle Airport)', [48.8534951, 2.3483915], 'France'),
               'Nice': ('Nice (NCE - Nice Cote d Azur Airport)', [43.7009358, 7.2683912], 'France'),
               'Marseille': ('Marseille (MRS - Marseille Provence Airport)', [43.2961743, 5.3699525], 'France'),
               'Cayenne': ('Cayenne (CAY - Felix Eboue Airport)', [4.9371143, -52.3258307], 'French Guiana'),
               'Papeete': (
               'Papeete (PPT - Faa a International Airport)', [-17.5373835, -149.5659964], 'French Polynesia'),
               'Libreville': ("Libreville (LBV - Leon M'ba Intl.)", [0.4052012, 9.438551], 'Gabon'),
               'Port Gentil': ('Port Gentil (POG - Port Gentil)', [-0.7151966, 8.7787919], 'Gabon'),
               'Franceville': ('Franceville (MVB - Mvengue)', [-1.634363, 13.589513], 'Gabon'),
               'Banjul': ('Banjul (BJL - Banjul Intl.)', [13.4410165, -16.56275092072591], 'Gambia'),
               'Tbilisi': ('Tbilisi (TBS - Tbilisi Intl.)', [41.6934591, 44.8014495], 'Georgia'),
               'Kutaisi': ('Kutaisi (KUT - David the Builder Kutaisi Intl.)', [42.2716078, 42.7054475], 'Georgia'),
               'Batumi': ('Batumi (BUS - Batumi Intl.)', [41.6509502, 41.6360085], 'Georgia'), 'Berlin': (
    "Berlin {'Tegel': '(TXL - Berlin Tegel)', 'Schönefeld': '(SXF - Berlin Schönefeld)', 'Brandenburg': '(BER - Berlin Brandenburg)'}",
    [52.5170365, 13.3888599], 'Germany'),
               'Frankfurt': ('Frankfurt (FRA - Frankfurt Intl.)', [50.1106444, 8.6820917], 'Germany'),
               'Munich': ('Munich (MUC - Munich Intl.)', [48.1371079, 11.5753822], 'Germany'),
               'Düsseldorf': ('Düsseldorf (DUS - Düsseldorf Intl.)', [51.2254018, 6.7763137], 'Germany'),
               'Hamburg': ('Hamburg (HAM - Hamburg Airport)', [53.550341, 10.000654], 'Germany'),
               'Stuttgart': ('Stuttgart (STR - Stuttgart Airport)', [48.7784485, 9.1800132], 'Germany'),
               'Cologne': ("Cologne {'Bonn': '(CGN - Cologne Bonn Airport)'}", [50.938361, 6.959974], 'Germany'),
               'Nuremberg': ('Nuremberg (NUE - Nuremberg Airport)', [49.453872, 11.077298], 'Germany'),
               'Leipzig': ("Leipzig {'Halle': '(LEJ - Leipzig/Halle Airport)'}", [51.3406321, 12.3747329], 'Germany'),
               'Accra': ('Accra (ACC - Kotoka Intl.)', [5.5571096, -0.2012376], 'Ghana'),
               'Kumasi': ('Kumasi (KMS - Kumasi Airport)', [6.6985605, -1.6233086], 'Ghana'),
               'Tamale': ('Tamale (TML - Tamale Airport)', [9.4051992, -0.8423986], 'Ghana'),
               'Takoradi': ('Takoradi (TKD - Takoradi Airport)', [4.887401, -1.7519316], 'Ghana'),
               'Athens': ('Athens (ATH - Eleftherios Venizelos Intl.)', [37.9839412, 23.7283052], 'Greece'),
               'Thessaloniki': ('Thessaloniki (SKG - Thessaloniki Airport)', [40.6403167, 22.9352716], 'Greece'),
               'Heraklion': ('Heraklion (HER - Heraklion Intl.)', [35.33908, 25.1332843], 'Greece'),
               'Rhodes': ('Rhodes (RHO - Diagoras Airport)', [36.17262995, 27.919418145633188], 'Greece'),
               'Chania': ('Chania (CHQ - Chania International Airport)', [35.5120831, 24.0191544], 'Greece'),
               'Mykonos': ('Mykonos (JMK - Mykonos Airport)', [37.45139365, 25.39231486780794], 'Greece'),
               "St. George's": ("St. George's (GND - Maurice Bishop Intl.)", [12.0535331, -61.751805], 'Grenada'),
               'Guatemala City': (
               "Guatemala City {'La Aurora': '(GUA - La Aurora Intl.)', 'Mundo Maya': '(FRS - Mundo Maya International)'}",
               [14.6222328, -90.5185188], 'Guatemala'),
               'Flores': ('Flores (FRS - Mundo Maya International)', [16.9298524, -89.8914817], 'Guatemala'),
               'Conakry': ('Conakry (CKY - Conakry Intl.)', [9.5170602, -13.6998434], 'Guinea'),
               'Bissau': ('Bissau (OXB - Osvaldo Vieira Intl.)', [11.861324, -15.583055], 'Guinea-Bissau'),
               'Georgetown': ('Georgetown (GEO - Cheddi Jagan Intl.)', [6.8137426, -58.1624465], 'Guyana'),
               'Port-au-Prince': (
               'Port-au-Prince (PAP - Toussaint Louverture Intl.)', [18.547327, -72.3395928], 'Haiti'),
               'Cap-Haitien': ('Cap-Haitien (CAP - Cap-Haitien Intl.)', [19.7595236, -72.2008068], 'Haiti'),
               'Tegucigalpa': ('Tegucigalpa (TGU - Toncontín Intl.)', [14.1057433, -87.2040052], 'Honduras'),
               'San Pedro Sula': (
               'San Pedro Sula (SAP - Ramón Villeda Morales Intl.)', [15.5062156, -88.0248937], 'Honduras'),
               'Reykjavik': ('Reykjavik (RKV - Reykjavik Airport)', [64.145981, -21.9422367], 'Iceland'),
               'Keflavik': ('Keflavik (KEF - Keflavik International Airport)', [63.9997694, -22.5565373], 'Iceland'),
               'New Delhi': (
               'New Delhi (DEL - Indira Gandhi International Airport)', [28.6138954, 77.2090057], 'India'),
               'Mumbai': ('Mumbai (BOM - Chhatrapati Shivaji International Airport)', [19.0785451, 72.878176], 'India'),
               'Chennai': ('Chennai (MAA - Chennai International Airport)', [13.0836939, 80.270186], 'India'),
               'Kolkata': (
               'Kolkata (CCU - Netaji Subhas Chandra Bose International Airport)', [22.5726459, 88.3638953], 'India'),
               'Jakarta': (
               'Jakarta (CGK - Soekarno-Hatta International Airport)', [-6.1752489, 106.8270462], 'Indonesia'),
               'Bali': ('Bali (DPS - Ngurah Rai International Airport)', [-8.3304977, 115.0906401], 'Indonesia'),
               'Surabaya': ('Surabaya (SUB - Juanda International Airport)', [-7.2459717, 112.7378266], 'Indonesia'),
               'Medan': ('Medan (KNO - Kuala Namu International Airport)', [3.5896654, 98.6738261], 'Indonesia'),
               'Tehran': ('Tehran (IKA - Imam Khomeini International Airport)', [35.6892523, 51.3896004], 'Iran'),
               'Mashhad': ('Mashhad (MHD - Mashhad International Airport)', [36.2974945, 59.6059232], 'Iran'),
               'Shiraz': ('Shiraz (SYZ - Shiraz International Airport)', [29.6060218, 52.5378041], 'Iran'),
               'Isfahan': ('Isfahan (IFN - Isfahan International Airport)', [32.6707877, 51.6650002], 'Iran'),
               'Baghdad': ('Baghdad (BGW - Baghdad International Airport)', [33.3061701, 44.3872213], 'Iraq'),
               'Basra': ('Basra (BSR - Basra International Airport)', [30.4952371, 47.8090981], 'Iraq'),
               'Erbil': ('Erbil (EBL - Erbil International Airport)', [36.1911653, 44.0094294], 'Iraq'),
               'Dublin': ('Dublin (DUB - Dublin Airport)', [53.3498006, -6.2602964], 'Ireland'),
               'Cork': ('Cork (ORK - Cork Airport)', [51.897077, -8.4654674], 'Ireland'),
               'Shannon': ('Shannon (SNN - Shannon Airport)', [52.7093263, -8.876893685751469], 'Ireland'),
               'Knock': ('Knock (NOC - Ireland West Airport Knock)', [52.6284891, -9.3325659], 'Ireland'),
               'Tel Aviv': ('Tel Aviv (TLV - Ben Gurion Airport)', [32.0852997, 34.7818064], 'Israel'),
               'Eilat': ('Eilat (ETH - Eilat Airport)', [29.5569348, 34.9497949], 'Israel'),
               'Haifa': ('Haifa (HFA - Haifa Airport)', [32.8191218, 34.9983856], 'Israel'),
               'Rome': ('Rome (FCO - Leonardo da Vinci-Fiumicino Airport)', [41.8933203, 12.4829321], 'Italy'),
               'Milan': ('Milan (MXP - Milan Malpensa Airport)', [45.4641943, 9.1896346], 'Italy'),
               'Venice': ('Venice (VCE - Venice Marco Polo Airport)', [45.4371908, 12.3345898], 'Italy'),
               'Naples': ('Naples (NAP - Naples International Airport)', [40.8358846, 14.2487679], 'Italy'),
               'Montego Bay': (
               'Montego Bay (MBJ - Sangster International Airport)', [18.4724603, -77.9217357], 'Jamaica'),
               'Kingston': (
               'Kingston (KIN - Norman Manley International Airport)', [17.9712148, -76.7928128], 'Jamaica'),
               'Tokyo': ('Tokyo (NRT - Narita International Airport)', [35.6812665, 139.757653], 'Japan'), 'Osaka': (
    'Osaka (KIX - Kansai International Airport)', [34.661629000000005, 135.49992679245517], 'Japan'),
               'Nagoya': ('Nagoya (NGO - Chubu Centrair International Airport)', [35.1851045, 136.8998438], 'Japan'),
               'Fukuoka': ('Fukuoka (FUK - Fukuoka Airport)', [33.6251241, 130.6180016], 'Japan'),
               'Amman': ('Amman (AMM - Queen Alia International Airport)', [31.9515694, 35.9239625], 'Jordan'),
               'Aqaba': ('Aqaba (AQJ - King Hussein International Airport)', [29.5266483, 35.0075433], 'Jordan'),
               'Almaty': ('Almaty (ALA - Almaty Intl.)', [43.2363924, 76.9457275], 'Kazakhstan'),
               'Astana': ('Astana (TSE - Nursultan Nazarbayev Intl.)', [51.1282205, 71.4306682], 'Kazakhstan'),
               'Nairobi': ('Nairobi (NBO - Jomo Kenyatta Intl.)', [-1.2832533, 36.8172449], 'Kenya'),
               'Mombasa': ('Mombasa (MBA - Moi Intl.)', [-4.05052, 39.667169], 'Kenya'),
               'Tarawa': ('Tarawa (TRW - Bonriki Intl.)', [1.4845541999999998, 172.96896482000938], 'Kiribati'),
               'Seoul': ('Seoul (ICN - Incheon Intl.)', [40.7477981, -73.9872728], 'Korea, South'),
               'Busan': ('Busan (PUS - Gimhae Intl.)', [36.2861972, 126.8943083], 'Korea, South'),
               'Pristina': ('Pristina (PRN - Pristina Intl.)', [42.6638771, 21.1640849], 'Kosovo'),
               'Kuwait City': ('Kuwait City (KWI - Kuwait Intl.)', [29.3796532, 47.9734174], 'Kuwait'),
               'Bishkek': ('Bishkek (FRU - Manas Intl.)', [42.8777895, 74.6066926], 'Kyrgyzstan'),
               'Vientiane': ('Vientiane (VTE - Wattay Intl.)', [17.9640988, 102.6133707], 'Laos'),
               'Luang Prabang': ('Luang Prabang (LPQ - Luang Prabang Intl.)', [19.8887438, 102.135898], 'Laos'),
               'Riga': ('Riga (RIX - Riga Intl.)', [56.9493977, 24.1051846], 'Latvia'),
               'Beirut': ('Beirut (BEY - Beirut Rafic Hariri Intl.)', [33.88922645, 35.50255852895232], 'Lebanon'),
               'Maseru': ('Maseru (MSU - Moshoeshoe I Intl.)', [-29.5816942, 27.8243208], 'Lesotho'),
               'Monrovia': ('Monrovia (ROB - Roberts Intl.)', [6.328034, -10.797788], 'Liberia'),
               'Tripoli': ('Tripoli (TIP - Tripoli Intl.)', [32.896672, 13.1777923], 'Libya'),
               'Benghazi': ('Benghazi (BEN - Benina Intl.)', [32.1288331, 20.0817204], 'Libya'),
               'Vaduz': ('Vaduz (QVJ - Vaduz Heliport)', [47.1393131, 9.5225926], 'Liechtenstein'),
               'Vilnius': ('Vilnius (VNO - Vilnius Intl.)', [54.6870458, 25.2829111], 'Lithuania'), 'Luxembourg City': (
    'Luxembourg City (LUX - Luxembourg Findel Airport)', [49.6112768, 6.129799], 'Luxembourg'),
               'Windhoek': ('Windhoek (WDH - Hosea Kutako Intl.)', [-22.5776104, 17.0772739], 'Namibia'),
               'Yaren District': ('Yaren District (INU - Nauru Intl.)', [-0.5471014, 166.9164002], 'Nauru'),
               'Kathmandu': ('Kathmandu (KTM - Tribhuvan Intl.)', [27.708317, 85.3205817], 'Nepal'),
               'Amsterdam': ('Amsterdam (AMS - Amsterdam Schiphol)', [52.3730796, 4.8924534], 'Netherlands'),
               'Rotterdam': ('Rotterdam (RTM - Rotterdam The Hague Airport)', [51.9244424, 4.47775], 'Netherlands'),
               'Auckland': ('Auckland (AKL - Auckland Intl.)', [-36.852095, 174.7631803], 'New Zealand'),
               'Wellington': ('Wellington (WLG - Wellington Intl.)', [-41.2887953, 174.7772114], 'New Zealand'),
               'Managua': ('Managua (MGA - Augusto C. Sandino Intl.)', [12.1544035, -86.2737642], 'Nicaragua'),
               'Niamey': ('Niamey (NIM - Diori Hamani Intl.)', [13.524834, 2.109823], 'Niger'),
               'Abuja': ('Abuja (ABV - Nnamdi Azikiwe Intl.)', [9.0643305, 7.4892974], 'Nigeria'),
               'Lagos': ('Lagos (LOS - Murtala Muhammed Intl.)', [6.4550575, 3.3941795], 'Nigeria'),
               'Oslo': ('Oslo (OSL - Oslo Gardermoen)', [59.9133301, 10.7389701], 'Norway'),
               'Muscat': ('Muscat (MCT - Muscat Intl.)', [23.5882019, 58.3829448], 'Oman'),
               'Macao': ('Macao (MFM - Macau Intl.)', [22.1899448, 113.5380454], 'Macao'),
               'Skopje': ('Skopje (SKP - Skopje Intl.)', [41.9961816, 21.4319213], 'Macedonia'), 'Antananarivo': (
    'Antananarivo (TNR - Ivato Intl.)', [-18.779148749999997, 46.71217161656727], 'Madagascar'),
               'Nosy Be': ('Nosy Be (NOS - Fascene Airport)', [-13.311952999999999, 48.253398632406366], 'Madagascar'),
               'Lilongwe': ('Lilongwe (LLW - Kamuzu Intl.)', [-13.9875107, 33.768144], 'Malawi'),
               'Kuala Lumpur': ('Kuala Lumpur (KUL - Kuala Lumpur Intl.)', [3.1516964, 101.6942371], 'Malaysia'),
               'Kota Kinabalu': ('Kota Kinabalu (BKI - Kota Kinabalu Intl.)', [5.9780066, 116.0728988], 'Malaysia'),
               'Penang': ('Penang (PEN - Penang Intl.)', [5.4065013, 100.2559077], 'Malaysia'),
               'Malé': ('Malé (MLE - Velana Intl.)', [4.1779879, 73.5107387], 'Maldives'),
               'Bamako': ('Bamako (BKO - Bamako-Sénou Intl.)', [12.61326555, -7.984739136241295], 'Mali'),
               'Islamabad': ('Islamabad (ISB - Islamabad Intl.)', [33.6938118, 73.0651511], 'Pakistan'),
               'Karachi': ('Karachi (KHI - Jinnah Intl.)', [24.8546842, 67.0207055], 'Pakistan'),
               'Lahore': ('Lahore (LHE - Allama Iqbal Intl.)', [31.5656822, 74.3141829], 'Pakistan'),
               'Multan': ('Multan (MUX - Multan Intl.)', [30.197838, 71.4719683], 'Pakistan'),
               'Peshawar': ('Peshawar (PEW - Bacha Khan Intl.)', [34.0123846, 71.5787458], 'Pakistan'),
               'Quetta': ('Quetta (UET - Quetta Intl.)', [30.1957677, 67.0172447], 'Pakistan'),
               'Koror': ('Koror (ROR - Roman Tmetuchl Intl.)', [7.343275, 134.4766767], 'Palau'),
               'David': ('David (DAV - Enrique Malek Intl.)', [8.4949423, -82.48261591569641], 'Panama'),
               'Panama City': ('Panama City (PTY - Tocumen Intl.)', [8.9714493, -79.5341802], 'Panama'),
               'Port Moresby': ('Port Moresby (POM - Jacksons Intl.)', [-9.4743301, 147.1599504], 'Papua New Guinea'),
               'Asuncion': ('Asuncion (ASU - Silvio Pettirossi Intl.)', [-25.2800459, -57.6343814], 'Paraguay'),
               'Cusco': ('Cusco (CUZ - Alejandro Velasco Astete Intl.)', [-13.5170887, -71.9785356], 'Peru'),
               'Lima': ('Lima (LIM - Jorge Chavez Intl.)', [-12.0621065, -77.0365256], 'Peru'),
               'Cebu City': ('Cebu City (CEB - Mactan-Cebu Intl.)', [10.2931062, 123.9020773], 'Philippines'),
               'Manila': ('Manila (MNL - Ninoy Aquino Intl.)', [14.5948914, 120.9782618], 'Philippines'),
               'Krakow': ('Krakow (KRK - John Paul II Intl.)', [50.0619474, 19.9368564], 'Poland'),
               'Warsaw': ('Warsaw (WAW - Frederic Chopin Intl.)', [52.2319581, 21.0067249], 'Poland'),
               'Faro': ('Faro (FAO - Faro Intl.)', [37.0162727, -7.9351771], 'Portugal'),
               'Lisbon': ('Lisbon (LIS - Humberto Delgado Airport)', [38.7077507, -9.1365919], 'Portugal'),
               'Bucharest': ('Bucharest (OTP - Henri Coanda Intl.)', [44.4361414, 26.1027202], 'Romania'),
               'Cluj-Napoca': ('Cluj-Napoca (CLJ - Avram Iancu Cluj Intl.)', [46.769379, 23.5899542], 'Romania'),
               'Timisoara': ('Timisoara (TSR - Traian Vuia Intl.)', [45.7538355, 21.2257474], 'Romania'),
               'Moscow': ('Moscow (SVO - Sheremetyevo Intl.)', [55.7504461, 37.6174943], 'Russia'),
               'St. Petersburg': ('St. Petersburg (LED - Pulkovo Intl.)', [59.938732, 30.316229], 'Russia'),
               'Novosibirsk': ('Novosibirsk (OVB - Tolmachevo Intl.)', [55.0288307, 82.9226887], 'Russia'),
               'Kigali': ('Kigali (KGL - Kigali Intl.)', [-1.950851, 30.061507], 'Rwanda'), 'Basseterre': (
    'Basseterre (SKB - Robert L. Bradshaw Intl.)', [17.2960919, -62.722301], 'Saint Kitts and Nevis'), 'Castries': (
    'Castries (SLU - George F. L. Charles Airport)', [13.90904385, -60.97792414113452], 'Saint Lucia'), 'Kingstown': (
    'Kingstown (SVD - Argyle Intl.)', [13.1561864, -61.2279621], 'Saint Vincent and the Grenadines'),
               'Apia': ('Apia (APW - Faleolo Intl.)', [-13.8344639, -171.7649144], 'Samoa'),
               'San Marino': ('San Marino (RMI - Federico Fellini Intl.)', [43.9458623, 12.458306], 'San Marino'),
               'Sao Tome': ('Sao Tome (TMS - Sao Tome Intl.)', [0.3389242, 6.7313031], 'Sao Tome and Principe'),
               'Riyadh': ('Riyadh (RUH - King Khaled Intl.)', [24.638916, 46.7160104], 'Saudi Arabia'),
               'Jeddah': ('Jeddah (JED - King Abdulaziz Intl.)', [21.5810088, 39.1653612], 'Saudi Arabia'),
               'Dammam': ('Dammam (DMM - King Fahd Intl.)', [26.4367824, 50.1039991], 'Saudi Arabia'),
               'Dakar': ('Dakar (DKR - Blaise Diagne Intl.)', [14.693425, -17.447938], 'Senegal'),
               'Belgrade': ('Belgrade (BEG - Nikola Tesla Intl.)', [44.8178131, 20.4568974], 'Serbia'),
               'Freetown': ('Freetown (FNA - Lungi Intl.)', [8.479004, -13.26795], 'Sierra Leone'),
               'Singapore': ('Singapore (SIN - Changi Intl.)', [1.357107, 103.8194992], 'Singapore'),
               'Bratislava': ('Bratislava (BTS - M. R. Stefanik Airport)', [48.1516988, 17.1093063], 'Slovakia'),
               'Ljubljana': ('Ljubljana (LJU - Joze Pucnik Airport)', [46.0500268, 14.5069289], 'Slovenia'),
               'Honiara': ('Honiara (HIR - Honiara Intl.)', [-9.437797549999999, 159.9624174786047], 'Solomon Islands'),
               'Taipei': ('Taipei (TPE - Taiwan Taoyuan Intl.)', [25.0375198, 121.5636796], 'Taiwan'),
               'Kaohsiung': ('Kaohsiung (KHH - Kaohsiung Intl.)', [22.6203348, 120.3120375], 'Taiwan'),
               'Dushanbe': ('Dushanbe (DYU - Dushanbe Intl.)', [38.585694700000005, 68.7603746751885], 'Tajikistan'),
               'Dar es Salaam': ('Dar es Salaam (DAR - Julius Nyerere Intl.)', [-6.8160837, 39.2803583], 'Tanzania'),
               'Zanzibar City': (
               'Zanzibar City (ZNZ - Abeid Amani Karume Intl.)', [-6.1664908, 39.2074312], 'Tanzania'),
               'Bangkok': ('Bangkok (BKK - Suvarnabhumi Airport)', [13.7524938, 100.4935089], 'Thailand'),
               'Phuket': ('Phuket (HKT - Phuket Intl.)', [7.9366015, 98.3529292], 'Thailand'),
               'Dili': ('Dili (DIL - Presidente Nicolau Lobato Intl.)', [-8.5536809, 125.5784093], 'Timor-Leste'),
               'Lome': ('Lome (LFW - Gnassingbe Eyadema Intl.)', [6.130419, 1.215829], 'Togo'),
               "Nuku'alofa": ("Nuku'alofa (TBU - Fua'amotu Intl.)", [-21.1343401, -175.201808], 'Tonga'),
               'Port of Spain': (
               'Port of Spain (POS - Piarco Intl.)', [10.6572678, -61.5180173], 'Trinidad and Tobago'),
               'Tunis': ('Tunis (TUN - Carthage Intl.)', [33.8439408, 9.400138], 'Tunisia'),
               'Istanbul': ('Istanbul (IST - Istanbul Airport)', [41.0091982, 28.9662187], 'Turkey'),
               'Ankara': ('Ankara (ESB - Esenboga Intl.)', [39.9207886, 32.8540482], 'Turkey'),
               'Antalya': ('Antalya (AYT - Antalya Intl.)', [36.8872942, 30.7074549], 'Turkey'),
               'Ashgabat': ('Ashgabat (ASB - Ashgabat Intl.)', [37.9404648, 58.3823487], 'Turkmenistan'),
               'Funafuti': ('Funafuti (FUN - Funafuti Intl.)', [-8.5199633, 179.1982548], 'Tuvalu'),
               'Entebbe': ('Entebbe (EBB - Entebbe Intl.)', [0.0611715, 32.4698564], 'Uganda'),
               'Kyiv': ('Kyiv (KBP - Kyiv Boryspil Intl.)', [50.4500336, 30.5241361], 'Ukraine'),
               'Lviv': ('Lviv (LWO - Lviv Danylo Halytskyi Intl.)', [49.841952, 24.0315921], 'Ukraine'),
               'Dubai': ('Dubai (DXB - Dubai Intl.)', [25.074282349999997, 55.18853865430702], 'United Arab Emirates'),
               'Abu Dhabi': ('Abu Dhabi (AUH - Abu Dhabi Intl.)', [24.4538352, 54.3774014], 'United Arab Emirates'),
               'London': ('London (LHR - London Heathrow Airport)', [51.5073359, -0.12765], 'United Kingdom'),
               'Manchester': ('Manchester (MAN - Manchester Airport)', [53.4794892, -2.2451148], 'United Kingdom'),
               'New York': ('New York (JFK - John F. Kennedy Intl.)', [40.7127281, -74.0060152], 'United States'),
               'Los Angeles': ('Los Angeles (LAX - Los Angeles Intl.)', [34.0536909, -118.242766], 'United States'),
               'Chicago': ("Chicago (ORD - Chicago O'Hare Intl.)", [41.8755616, -87.6244212], 'United States'),
               'Montevideo': ('Montevideo (MVD - Carrasco Intl.)', [-34.9058916, -56.1913095], 'Uruguay'),
               'Tashkent': ('Tashkent (TAS - Tashkent Intl.)', [41.3123363, 69.2787079], 'Uzbekistan'),
               'Port Vila': ('Port Vila (VLI - Bauerfield Intl.)', [-17.7414972, 168.3150163], 'Vanuatu'),
               'Caracas': ('Caracas (CCS - Simon Bolivar Intl.)', [10.5060934, -66.9146008], 'Venezuela'),
               'Valencia': ('Valencia (VLN - Arturo Michelena Intl.)', [10.170026, -68.0003987], 'Venezuela'),
               'Maracaibo': ('Maracaibo (MAR - La Chinita Intl.)', [10.6498095, -71.6443596], 'Venezuela'),
               'Barquisimeto': ('Barquisimeto (BRM - Jacinto Lara Intl.)', [10.0774374, -69.3222293], 'Venezuela'),
               'Puerto Ordaz': ('Puerto Ordaz (PZO - Manuel Carlos Piar Intl.)', [8.2750351, -62.7558263], 'Venezuela'),
               'Porlamar': (
               'Porlamar (PMV - Del Caribe Intl. Gen. Santiago Marino)', [10.9635839, -63.8464509], 'Venezuela'),
               'Hanoi': ('Hanoi (HAN - Noi Bai Intl.)', [21.0294498, 105.8544441], 'Vietnam'),
               'Ho Chi Minh City': ('Ho Chi Minh City (SGN - Tan Son Nhat Intl.)', [10.7764772, 106.701938], 'Vietnam'),
               'Da Nang': ('Da Nang (DAD - Da Nang Intl.)', [16.068, 108.212], 'Vietnam'),
               'Nha Trang': ('Nha Trang (CXR - Cam Ranh Intl.)', [12.2431693, 109.1898675], 'Vietnam'),
               'Phu Quoc': ('Phu Quoc (PQC - Phu Quoc Intl.)', [10.2153093, 103.9880443], 'Vietnam'),
               'Futuna Island': ('Futuna Island (FUT)', [-14.276851, -178.14234997654432], 'Wallis and Futuna'),
               'Wallis Island': ('Wallis Island (WLS)', [-13.2846405, -176.20665679493294], 'Wallis and Futuna'),
               'Aden': ('Aden (ADE - Aden Intl)', [12.833333, 44.916667], 'Yemen'),
               'Sanaa': ('Sanaa (SAH - Sanaa Intl)', [15.3538569, 44.2058841], 'Yemen'),
               'Taiz': ('Taiz (TAI - Taiz Intl)', [13.4115414, 43.5570871], 'Yemen'),
               'Livingstone': ('Livingstone (LVI - Harry Mwanga Nkumbula Intl)', [-17.853135, 25.861429], 'Zambia'),
               'Lusaka': ('Lusaka (LUN - Kenneth Kaunda Intl)', [-15.4163395, 28.2818414], 'Zambia'),
               'Ndola': ('Ndola (NLA - Simon Mwansa Kapwepwe Intl)', [-12.9693056, 28.6365894], 'Zambia'),
               'Bulawayo': ('Bulawayo (BUQ - Joshua Mqabuko Nkomo Intl)', [-20.1053948, 28.5426856], 'Zimbabwe'),
               'Harare': ('Harare (HRE - Robert Gabriel Mugabe Intl)', [-17.831773, 31.045686], 'Zimbabwe'),
               'Victoria Falls': ('Victoria Falls (VFA - Victoria Falls Intl)', [-17.9229035, 25.8490239], 'Zimbabwe')}

Airports = {'Kabul': ('(KBL', 'Kabul (KBL - Hamid Karmic Intl.)', [34.5260109, 69.1776838], 'Afghanistan'),
            'Tirana': ('(TIA', 'Tirana (TIA - Tirana Intl.)', [41.330488599999995, 19.82556898393491], 'Albania'),
            'Algiers': ('(ALG', 'Algiers (ALG - Houari Boumediene Airport)', [36.7753606, 3.0601882], 'Algeria'),
            'Oran': ('(ORN', 'Oran (ORN - Oran Es Senia Airport)', [35.7044415, -0.6502981], 'Algeria'),
            'Andorra La Vella': ('(ALV', 'Andorra La Vella (ALV - Heliport)', [42.5069391, 1.5212467], 'Andorra'),
            'Luanda': ('(LAD', 'Luanda (LAD - Quatro de Fevereiro Intl.)', [-8.8272699, 13.2439512], 'Angola'),
            "St. John's": (
            '(ANU', "St. John's (ANU - V.C. Bird Intl.)", [17.1184569, -61.8448509], 'Antigua and Barbuda'),
            'Buenos Aires': (
            '(EZE', 'Buenos Aires (EZE - Ministro Pistarini Intl.)', [-34.6075682, -58.4370894], 'Argentina'),
            'Cordoba': (
            '(COR', 'Cordoba (COR - Ingeniero Aeronáutico Ambrosio L.V. Taravella Intl.)', [-31.4166867, -64.1834193],
            'Argentina'), 'Yerevan': ('(EVN', 'Yerevan (EVN - Zvartnots Intl.)', [40.1777112, 44.5126233], 'Armenia'),
            'Sydney': ('(SYD', 'Sydney (SYD - Sydney Kingsford Smith Intl.)', [-33.8698439, 151.2082848], 'Australia'),
            'Melbourne': (
            '(MEL', 'Melbourne (MEL - Melbourne Tullamarine Intl.)', [-37.8142176, 144.9631608], 'Australia'),
            'Manama': ('(BAH', 'Manama (BAH - Bahrain Intl.)', [26.2235041, 50.5822436], 'Bahrain'),
            'Dhaka': ('(DAC', 'Dhaka (DAC - Hazrat Shahjalal Intl.)', [23.7644025, 90.389015], 'Bangladesh'),
            'Bridgetown': ('(BGI', 'Bridgetown (BGI - Grantley Adams Intl.)', [13.0977832, -59.6184184], 'Barbados'),
            'Minsk': ('(MSQ', 'Minsk (MSQ - Minsk National Airport)', [53.9024716, 27.5618225], 'Belarus'),
            'Brussels': ('(BRU', 'Brussels (BRU - Brussels Airport)', [50.8465573, 4.351697], 'Belgium'),
            'Belize City': (
            '(BZE', 'Belize City (BZE - Philip S. W. Goldson Intl.)', [17.5000543, -88.2003115], 'Belize'),
            'Cotonou': ('(COO', 'Cotonou (COO - Cotonou Cadjehoun Airport)', [6.3676953, 2.4252507], 'Benin'),
            'Hamilton': ('(BDA', 'Hamilton (BDA - L.F. Wade Intl.)', [32.2956076, -64.7827048], 'Bermuda'),
            'Paro': ('(PBH', 'Paro (PBH - Paro Intl.)', [27.4646365, 89.3183409], 'Bhutan'),
            'La Paz': ('(LPB', 'La Paz (LPB - El Alto Intl.)', [-16.4955455, -68.1336229], 'Bolivia'),
            'Santa Cruz de la Sierra': (
            '(VVI', 'Santa Cruz de la Sierra (VVI - Viru Viru Intl.)', [-17.7834936, -63.1820853], 'Bolivia'),
            'Phnom Penh': ('(PNH', 'Phnom Penh (PNH - Phnom Penh Intl.)', [11.568271, 104.9224426], 'Cambodia'),
            'Siem Reap': ('(REP', 'Siem Reap (REP - Siem Reap Intl.)', [13.3617562, 103.8590321], 'Cambodia'),
            'Yaounde': ('(NSI', 'Yaounde (NSI - Yaounde Nsimalen Intl.)', [3.8689867, 11.5213344], 'Cameroon'),
            'Douala': ('(DLA', 'Douala (DLA - Douala Intl.)', [4.0429408, 9.706203], 'Cameroon'),
            'Toronto': ('(YYZ', 'Toronto (YYZ - Toronto Pearson Intl.)', [43.6534733, -79.383961], 'Canada'),
            'Vancouver': ('(YVR', 'Vancouver (YVR - Vancouver Intl.)', [49.2608724, -123.113952], 'Canada'),
            'Montreal': ('(YUL', 'Montreal (YUL - Montreal-Trudeau Intl.)', [45.5031824, -73.5698065], 'Canada'),
            'Calgary': ('(YYC', 'Calgary (YYC - Calgary Intl.)', [51.0460954, -114.065465], 'Canada'),
            'Edmonton': ('(YEG', 'Edmonton (YEG - Edmonton Intl.)', [53.5462055, -113.491241], 'Canada'),
            'Ottawa': ('(YOW', 'Ottawa (YOW - Ottawa Macdonald-Cartier Intl.)', [45.4208777, -75.6901106], 'Canada'),
            'Halifax': ('(YHZ', 'Halifax (YHZ - Halifax Stanfield Intl.)', [44.648618, -63.5859487], 'Canada'),
            'Quebec City': (
            '(YQB', 'Quebec City (YQB - Quebec City Jean Lesage Intl.)', [46.8137431, -71.2084061], 'Canada'),
            'Winnipeg': (
            '(YWG', 'Winnipeg (YWG - Winnipeg James Armstrong Richardson Intl.)', [49.8955367, -97.1384584], 'Canada'),
            'Victoria': ('(SEZ', 'Victoria (SEZ - Seychelles Intl.)', [-4.6232085, 55.452359], 'Seychelles'),
            'Praia': ('(RAI', 'Praia (RAI - Nelson Mandela Intl.)', [14.9162811, -23.5095095], 'Cape Verde'),
            'Bangui': (
            '(BGF', "Bangui (BGF - Bangui M'Poko Intl.)", [4.3907153, 18.5509126], 'Central African Republic'),
            "N'Djamena": ('(NDJ', "N'Djamena (NDJ - N'Djamena Intl.)", [12.1191543, 15.0502758], 'Chad'), 'Santiago': (
    '(SCL', 'Santiago (SCL - Comodoro Arturo Merino Benitez Intl.)', [-33.4377756, -70.6504502], 'Chile'),
            'Easter Island': (
            '(IPC', 'Easter Island (IPC - Mataveri Intl.)', [-27.128500000000003, -109.33602969583333], 'Chile'),
            'Beijing': ('(PEK', 'Beijing (PEK - Beijing Capital Intl.)', [39.906217, 116.3912757], 'China'),
            'Shanghai': ('(PVG', 'Shanghai (PVG - Shanghai Pudong Intl.)', [31.2322758, 121.4692071], 'China'),
            'Hong Kong': ('(HKG', 'Hong Kong (HKG - Hong Kong Intl.)', [22.2793278, 114.1628131], 'China'),
            'Guangzhou': ('(CAN', 'Guangzhou (CAN - Guangzhou Baiyun Intl.)', [23.1301964, 113.2592945], 'China'),
            'Shenzhen': ('(SZX', "Shenzhen (SZX - Shenzhen Bao'an Intl.)", [22.5445741, 114.0545429], 'China'),
            'Quito': ('(UIO', 'Quito (UIO - Mariscal Sucre Intl.)', [-0.2201641, -78.5123274], 'Ecuador'),
            'Guayaquil': (
            '(GYE', 'Guayaquil (GYE - Jose Joaquin de Olmedo Intl.)', [-2.1900563, -79.8868741], 'Ecuador'),
            'Cairo': ('(CAI', 'Cairo (CAI - Cairo Intl.)', [30.0443879, 31.2357257], 'Egypt'),
            'Alexandria': ('(HBE', 'Alexandria (HBE - Borg El Arab Intl.)', [31.1991806, 29.8951716], 'Egypt'),
            'San Salvador': (
            '(SAL', 'San Salvador (SAL - El Salvador Intl.)', [13.6989939, -89.1914249], 'El Salvador'),
            'Malabo': ('(SSG', 'Malabo (SSG - Malabo Intl.)', [3.752831, 8.7800693], 'Equatorial Guinea'),
            'Bata': ('(BSG', 'Bata (BSG - Bata Airport)', [1.82385155, 9.856166243652915], 'Equatorial Guinea'),
            'Asmara': ('(ASM', 'Asmara (ASM - Asmara Intl.)', [15.3389667, 38.9326763], 'Eritrea'),
            'Tallinn': ('(TLL', 'Tallinn (TLL - Lennart Meri Tallinn Airport)', [59.4372155, 24.7453688], 'Estonia'),
            'Addis Ababa': ('(ADD', 'Addis Ababa (ADD - Bole Intl.)', [9.0107934, 38.7612525], 'Ethiopia'),
            'Nadi': ('(NAN', 'Nadi (NAN - Nadi Intl.)', [-17.7992725, 177.4178549], 'Fiji'),
            'Suva': ('(SUV', 'Suva (SUV - Nausori Intl.)', [-18.1415884, 178.4421662], 'Fiji'),
            'Helsinki': ('(HEL', 'Helsinki (HEL - Helsinki Airport)', [60.1674881, 24.9427473], 'Finland'),
            'Tampere': ('(TMP', 'Tampere (TMP - Tampere-Pirkkala Airport)', [61.4980214, 23.7603118], 'Finland'),
            'Paris': ('(CDG', 'Paris (CDG - Charles de Gaulle Airport)', [48.8534951, 2.3483915], 'France'),
            'Nice': ('(NCE', 'Nice (NCE - Nice Cote d Azur Airport)', [43.7009358, 7.2683912], 'France'),
            'Marseille': ('(MRS', 'Marseille (MRS - Marseille Provence Airport)', [43.2961743, 5.3699525], 'France'),
            'Cayenne': ('(CAY', 'Cayenne (CAY - Felix Eboue Airport)', [4.9371143, -52.3258307], 'French Guiana'),
            'Papeete': (
            '(PPT', 'Papeete (PPT - Faa a International Airport)', [-17.5373835, -149.5659964], 'French Polynesia'),
            'Libreville': ('(LBV', "Libreville (LBV - Leon M'ba Intl.)", [0.4052012, 9.438551], 'Gabon'),
            'Port Gentil': ('(POG', 'Port Gentil (POG - Port Gentil)', [-0.7151966, 8.7787919], 'Gabon'),
            'Franceville': ('(MVB', 'Franceville (MVB - Mvengue)', [-1.634363, 13.589513], 'Gabon'),
            'Banjul': ('(BJL', 'Banjul (BJL - Banjul Intl.)', [13.4410165, -16.56275092072591], 'Gambia'),
            'Tbilisi': ('(TBS', 'Tbilisi (TBS - Tbilisi Intl.)', [41.6934591, 44.8014495], 'Georgia'),
            'Kutaisi': ('(KUT', 'Kutaisi (KUT - David the Builder Kutaisi Intl.)', [42.2716078, 42.7054475], 'Georgia'),
            'Batumi': ('(BUS', 'Batumi (BUS - Batumi Intl.)', [41.6509502, 41.6360085], 'Georgia'),
            'Frankfurt': ('(FRA', 'Frankfurt (FRA - Frankfurt Intl.)', [50.1106444, 8.6820917], 'Germany'),
            'Munich': ('(MUC', 'Munich (MUC - Munich Intl.)', [48.1371079, 11.5753822], 'Germany'),
            'Düsseldorf': ('(DUS', 'Düsseldorf (DUS - Düsseldorf Intl.)', [51.2254018, 6.7763137], 'Germany'),
            'Hamburg': ('(HAM', 'Hamburg (HAM - Hamburg Airport)', [53.550341, 10.000654], 'Germany'),
            'Stuttgart': ('(STR', 'Stuttgart (STR - Stuttgart Airport)', [48.7784485, 9.1800132], 'Germany'),
            'Nuremberg': ('(NUE', 'Nuremberg (NUE - Nuremberg Airport)', [49.453872, 11.077298], 'Germany'),
            'Accra': ('(ACC', 'Accra (ACC - Kotoka Intl.)', [5.5571096, -0.2012376], 'Ghana'),
            'Kumasi': ('(KMS', 'Kumasi (KMS - Kumasi Airport)', [6.6985605, -1.6233086], 'Ghana'),
            'Tamale': ('(TML', 'Tamale (TML - Tamale Airport)', [9.4051992, -0.8423986], 'Ghana'),
            'Takoradi': ('(TKD', 'Takoradi (TKD - Takoradi Airport)', [4.887401, -1.7519316], 'Ghana'),
            'Athens': ('(ATH', 'Athens (ATH - Eleftherios Venizelos Intl.)', [37.9839412, 23.7283052], 'Greece'),
            'Thessaloniki': ('(SKG', 'Thessaloniki (SKG - Thessaloniki Airport)', [40.6403167, 22.9352716], 'Greece'),
            'Heraklion': ('(HER', 'Heraklion (HER - Heraklion Intl.)', [35.33908, 25.1332843], 'Greece'),
            'Rhodes': ('(RHO', 'Rhodes (RHO - Diagoras Airport)', [36.17262995, 27.919418145633188], 'Greece'),
            'Chania': ('(CHQ', 'Chania (CHQ - Chania International Airport)', [35.5120831, 24.0191544], 'Greece'),
            'Mykonos': ('(JMK', 'Mykonos (JMK - Mykonos Airport)', [37.45139365, 25.39231486780794], 'Greece'),
            "St. George's": ('(GND', "St. George's (GND - Maurice Bishop Intl.)", [12.0535331, -61.751805], 'Grenada'),
            'Flores': ('(FRS', 'Flores (FRS - Mundo Maya International)', [16.9298524, -89.8914817], 'Guatemala'),
            'Conakry': ('(CKY', 'Conakry (CKY - Conakry Intl.)', [9.5170602, -13.6998434], 'Guinea'),
            'Bissau': ('(OXB', 'Bissau (OXB - Osvaldo Vieira Intl.)', [11.861324, -15.583055], 'Guinea-Bissau'),
            'Georgetown': ('(GEO', 'Georgetown (GEO - Cheddi Jagan Intl.)', [6.8137426, -58.1624465], 'Guyana'),
            'Port-au-Prince': (
            '(PAP', 'Port-au-Prince (PAP - Toussaint Louverture Intl.)', [18.547327, -72.3395928], 'Haiti'),
            'Cap-Haitien': ('(CAP', 'Cap-Haitien (CAP - Cap-Haitien Intl.)', [19.7595236, -72.2008068], 'Haiti'),
            'Tegucigalpa': ('(TGU', 'Tegucigalpa (TGU - Toncontín Intl.)', [14.1057433, -87.2040052], 'Honduras'),
            'San Pedro Sula': (
            '(SAP', 'San Pedro Sula (SAP - Ramón Villeda Morales Intl.)', [15.5062156, -88.0248937], 'Honduras'),
            'Reykjavik': ('(RKV', 'Reykjavik (RKV - Reykjavik Airport)', [64.145981, -21.9422367], 'Iceland'),
            'Keflavik': (
            '(KEF', 'Keflavik (KEF - Keflavik International Airport)', [63.9997694, -22.5565373], 'Iceland'),
            'New Delhi': (
            '(DEL', 'New Delhi (DEL - Indira Gandhi International Airport)', [28.6138954, 77.2090057], 'India'),
            'Mumbai': (
            '(BOM', 'Mumbai (BOM - Chhatrapati Shivaji International Airport)', [19.0785451, 72.878176], 'India'),
            'Chennai': ('(MAA', 'Chennai (MAA - Chennai International Airport)', [13.0836939, 80.270186], 'India'),
            'Kolkata': (
            '(CCU', 'Kolkata (CCU - Netaji Subhas Chandra Bose International Airport)', [22.5726459, 88.3638953],
            'India'), 'Jakarta': (
    '(CGK', 'Jakarta (CGK - Soekarno-Hatta International Airport)', [-6.1752489, 106.8270462], 'Indonesia'),
            'Bali': ('(DPS', 'Bali (DPS - Ngurah Rai International Airport)', [-8.3304977, 115.0906401], 'Indonesia'),
            'Surabaya': (
            '(SUB', 'Surabaya (SUB - Juanda International Airport)', [-7.2459717, 112.7378266], 'Indonesia'),
            'Medan': ('(KNO', 'Medan (KNO - Kuala Namu International Airport)', [3.5896654, 98.6738261], 'Indonesia'),
            'Tehran': ('(IKA', 'Tehran (IKA - Imam Khomeini International Airport)', [35.6892523, 51.3896004], 'Iran'),
            'Mashhad': ('(MHD', 'Mashhad (MHD - Mashhad International Airport)', [36.2974945, 59.6059232], 'Iran'),
            'Shiraz': ('(SYZ', 'Shiraz (SYZ - Shiraz International Airport)', [29.6060218, 52.5378041], 'Iran'),
            'Isfahan': ('(IFN', 'Isfahan (IFN - Isfahan International Airport)', [32.6707877, 51.6650002], 'Iran'),
            'Baghdad': ('(BGW', 'Baghdad (BGW - Baghdad International Airport)', [33.3061701, 44.3872213], 'Iraq'),
            'Basra': ('(BSR', 'Basra (BSR - Basra International Airport)', [30.4952371, 47.8090981], 'Iraq'),
            'Erbil': ('(EBL', 'Erbil (EBL - Erbil International Airport)', [36.1911653, 44.0094294], 'Iraq'),
            'Dublin': ('(DUB', 'Dublin (DUB - Dublin Airport)', [53.3498006, -6.2602964], 'Ireland'),
            'Cork': ('(ORK', 'Cork (ORK - Cork Airport)', [51.897077, -8.4654674], 'Ireland'),
            'Shannon': ('(SNN', 'Shannon (SNN - Shannon Airport)', [52.7093263, -8.876893685751469], 'Ireland'),
            'Knock': ('(NOC', 'Knock (NOC - Ireland West Airport Knock)', [52.6284891, -9.3325659], 'Ireland'),
            'Tel Aviv': ('(TLV', 'Tel Aviv (TLV - Ben Gurion Airport)', [32.0852997, 34.7818064], 'Israel'),
            'Eilat': ('(ETH', 'Eilat (ETH - Eilat Airport)', [29.5569348, 34.9497949], 'Israel'),
            'Haifa': ('(HFA', 'Haifa (HFA - Haifa Airport)', [32.8191218, 34.9983856], 'Israel'),
            'Rome': ('(FCO', 'Rome (FCO - Leonardo da Vinci-Fiumicino Airport)', [41.8933203, 12.4829321], 'Italy'),
            'Milan': ('(MXP', 'Milan (MXP - Milan Malpensa Airport)', [45.4641943, 9.1896346], 'Italy'),
            'Venice': ('(VCE', 'Venice (VCE - Venice Marco Polo Airport)', [45.4371908, 12.3345898], 'Italy'),
            'Naples': ('(NAP', 'Naples (NAP - Naples International Airport)', [40.8358846, 14.2487679], 'Italy'),
            'Montego Bay': (
            '(MBJ', 'Montego Bay (MBJ - Sangster International Airport)', [18.4724603, -77.9217357], 'Jamaica'),
            'Kingston': (
            '(KIN', 'Kingston (KIN - Norman Manley International Airport)', [17.9712148, -76.7928128], 'Jamaica'),
            'Tokyo': ('(NRT', 'Tokyo (NRT - Narita International Airport)', [35.6812665, 139.757653], 'Japan'),
            'Osaka': (
            '(KIX', 'Osaka (KIX - Kansai International Airport)', [34.661629000000005, 135.49992679245517], 'Japan'),
            'Nagoya': (
            '(NGO', 'Nagoya (NGO - Chubu Centrair International Airport)', [35.1851045, 136.8998438], 'Japan'),
            'Fukuoka': ('(FUK', 'Fukuoka (FUK - Fukuoka Airport)', [33.6251241, 130.6180016], 'Japan'),
            'Amman': ('(AMM', 'Amman (AMM - Queen Alia International Airport)', [31.9515694, 35.9239625], 'Jordan'),
            'Aqaba': ('(AQJ', 'Aqaba (AQJ - King Hussein International Airport)', [29.5266483, 35.0075433], 'Jordan'),
            'Almaty': ('(ALA', 'Almaty (ALA - Almaty Intl.)', [43.2363924, 76.9457275], 'Kazakhstan'),
            'Astana': ('(TSE', 'Astana (TSE - Nursultan Nazarbayev Intl.)', [51.1282205, 71.4306682], 'Kazakhstan'),
            'Nairobi': ('(NBO', 'Nairobi (NBO - Jomo Kenyatta Intl.)', [-1.2832533, 36.8172449], 'Kenya'),
            'Mombasa': ('(MBA', 'Mombasa (MBA - Moi Intl.)', [-4.05052, 39.667169], 'Kenya'),
            'Tarawa': ('(TRW', 'Tarawa (TRW - Bonriki Intl.)', [1.4845541999999998, 172.96896482000938], 'Kiribati'),
            'Seoul': ('(ICN', 'Seoul (ICN - Incheon Intl.)', [40.7477981, -73.9872728], 'Korea, South'),
            'Busan': ('(PUS', 'Busan (PUS - Gimhae Intl.)', [36.2861972, 126.8943083], 'Korea, South'),
            'Pristina': ('(PRN', 'Pristina (PRN - Pristina Intl.)', [42.6638771, 21.1640849], 'Kosovo'),
            'Kuwait City': ('(KWI', 'Kuwait City (KWI - Kuwait Intl.)', [29.3796532, 47.9734174], 'Kuwait'),
            'Bishkek': ('(FRU', 'Bishkek (FRU - Manas Intl.)', [42.8777895, 74.6066926], 'Kyrgyzstan'),
            'Vientiane': ('(VTE', 'Vientiane (VTE - Wattay Intl.)', [17.9640988, 102.6133707], 'Laos'),
            'Luang Prabang': ('(LPQ', 'Luang Prabang (LPQ - Luang Prabang Intl.)', [19.8887438, 102.135898], 'Laos'),
            'Riga': ('(RIX', 'Riga (RIX - Riga Intl.)', [56.9493977, 24.1051846], 'Latvia'),
            'Beirut': ('(BEY', 'Beirut (BEY - Beirut Rafic Hariri Intl.)', [33.88922645, 35.50255852895232], 'Lebanon'),
            'Maseru': ('(MSU', 'Maseru (MSU - Moshoeshoe I Intl.)', [-29.5816942, 27.8243208], 'Lesotho'),
            'Monrovia': ('(ROB', 'Monrovia (ROB - Roberts Intl.)', [6.328034, -10.797788], 'Liberia'),
            'Tripoli': ('(TIP', 'Tripoli (TIP - Tripoli Intl.)', [32.896672, 13.1777923], 'Libya'),
            'Benghazi': ('(BEN', 'Benghazi (BEN - Benina Intl.)', [32.1288331, 20.0817204], 'Libya'),
            'Vaduz': ('(QVJ', 'Vaduz (QVJ - Vaduz Heliport)', [47.1393131, 9.5225926], 'Liechtenstein'),
            'Vilnius': ('(VNO', 'Vilnius (VNO - Vilnius Intl.)', [54.6870458, 25.2829111], 'Lithuania'),
            'Luxembourg City': (
            '(LUX', 'Luxembourg City (LUX - Luxembourg Findel Airport)', [49.6112768, 6.129799], 'Luxembourg'),
            'Windhoek': ('(WDH', 'Windhoek (WDH - Hosea Kutako Intl.)', [-22.5776104, 17.0772739], 'Namibia'),
            'Yaren District': ('(INU', 'Yaren District (INU - Nauru Intl.)', [-0.5471014, 166.9164002], 'Nauru'),
            'Kathmandu': ('(KTM', 'Kathmandu (KTM - Tribhuvan Intl.)', [27.708317, 85.3205817], 'Nepal'),
            'Amsterdam': ('(AMS', 'Amsterdam (AMS - Amsterdam Schiphol)', [52.3730796, 4.8924534], 'Netherlands'),
            'Rotterdam': (
            '(RTM', 'Rotterdam (RTM - Rotterdam The Hague Airport)', [51.9244424, 4.47775], 'Netherlands'),
            'Auckland': ('(AKL', 'Auckland (AKL - Auckland Intl.)', [-36.852095, 174.7631803], 'New Zealand'),
            'Wellington': ('(WLG', 'Wellington (WLG - Wellington Intl.)', [-41.2887953, 174.7772114], 'New Zealand'),
            'Managua': ('(MGA', 'Managua (MGA - Augusto C. Sandino Intl.)', [12.1544035, -86.2737642], 'Nicaragua'),
            'Niamey': ('(NIM', 'Niamey (NIM - Diori Hamani Intl.)', [13.524834, 2.109823], 'Niger'),
            'Abuja': ('(ABV', 'Abuja (ABV - Nnamdi Azikiwe Intl.)', [9.0643305, 7.4892974], 'Nigeria'),
            'Lagos': ('(LOS', 'Lagos (LOS - Murtala Muhammed Intl.)', [6.4550575, 3.3941795], 'Nigeria'),
            'Oslo': ('(OSL', 'Oslo (OSL - Oslo Gardermoen)', [59.9133301, 10.7389701], 'Norway'),
            'Muscat': ('(MCT', 'Muscat (MCT - Muscat Intl.)', [23.5882019, 58.3829448], 'Oman'),
            'Macao': ('(MFM', 'Macao (MFM - Macau Intl.)', [22.1899448, 113.5380454], 'Macao'),
            'Skopje': ('(SKP', 'Skopje (SKP - Skopje Intl.)', [41.9961816, 21.4319213], 'Macedonia'), 'Antananarivo': (
    '(TNR', 'Antananarivo (TNR - Ivato Intl.)', [-18.779148749999997, 46.71217161656727], 'Madagascar'), 'Nosy Be': (
    '(NOS', 'Nosy Be (NOS - Fascene Airport)', [-13.311952999999999, 48.253398632406366], 'Madagascar'),
            'Lilongwe': ('(LLW', 'Lilongwe (LLW - Kamuzu Intl.)', [-13.9875107, 33.768144], 'Malawi'),
            'Kuala Lumpur': ('(KUL', 'Kuala Lumpur (KUL - Kuala Lumpur Intl.)', [3.1516964, 101.6942371], 'Malaysia'),
            'Kota Kinabalu': (
            '(BKI', 'Kota Kinabalu (BKI - Kota Kinabalu Intl.)', [5.9780066, 116.0728988], 'Malaysia'),
            'Penang': ('(PEN', 'Penang (PEN - Penang Intl.)', [5.4065013, 100.2559077], 'Malaysia'),
            'Malé': ('(MLE', 'Malé (MLE - Velana Intl.)', [4.1779879, 73.5107387], 'Maldives'),
            'Bamako': ('(BKO', 'Bamako (BKO - Bamako-Sénou Intl.)', [12.61326555, -7.984739136241295], 'Mali'),
            'Islamabad': ('(ISB', 'Islamabad (ISB - Islamabad Intl.)', [33.6938118, 73.0651511], 'Pakistan'),
            'Karachi': ('(KHI', 'Karachi (KHI - Jinnah Intl.)', [24.8546842, 67.0207055], 'Pakistan'),
            'Lahore': ('(LHE', 'Lahore (LHE - Allama Iqbal Intl.)', [31.5656822, 74.3141829], 'Pakistan'),
            'Multan': ('(MUX', 'Multan (MUX - Multan Intl.)', [30.197838, 71.4719683], 'Pakistan'),
            'Peshawar': ('(PEW', 'Peshawar (PEW - Bacha Khan Intl.)', [34.0123846, 71.5787458], 'Pakistan'),
            'Quetta': ('(UET', 'Quetta (UET - Quetta Intl.)', [30.1957677, 67.0172447], 'Pakistan'),
            'Koror': ('(ROR', 'Koror (ROR - Roman Tmetuchl Intl.)', [7.343275, 134.4766767], 'Palau'),
            'David': ('(DAV', 'David (DAV - Enrique Malek Intl.)', [8.4949423, -82.48261591569641], 'Panama'),
            'Panama City': ('(PTY', 'Panama City (PTY - Tocumen Intl.)', [8.9714493, -79.5341802], 'Panama'),
            'Port Moresby': (
            '(POM', 'Port Moresby (POM - Jacksons Intl.)', [-9.4743301, 147.1599504], 'Papua New Guinea'),
            'Asuncion': ('(ASU', 'Asuncion (ASU - Silvio Pettirossi Intl.)', [-25.2800459, -57.6343814], 'Paraguay'),
            'Cusco': ('(CUZ', 'Cusco (CUZ - Alejandro Velasco Astete Intl.)', [-13.5170887, -71.9785356], 'Peru'),
            'Lima': ('(LIM', 'Lima (LIM - Jorge Chavez Intl.)', [-12.0621065, -77.0365256], 'Peru'),
            'Cebu City': ('(CEB', 'Cebu City (CEB - Mactan-Cebu Intl.)', [10.2931062, 123.9020773], 'Philippines'),
            'Manila': ('(MNL', 'Manila (MNL - Ninoy Aquino Intl.)', [14.5948914, 120.9782618], 'Philippines'),
            'Krakow': ('(KRK', 'Krakow (KRK - John Paul II Intl.)', [50.0619474, 19.9368564], 'Poland'),
            'Warsaw': ('(WAW', 'Warsaw (WAW - Frederic Chopin Intl.)', [52.2319581, 21.0067249], 'Poland'),
            'Faro': ('(FAO', 'Faro (FAO - Faro Intl.)', [37.0162727, -7.9351771], 'Portugal'),
            'Lisbon': ('(LIS', 'Lisbon (LIS - Humberto Delgado Airport)', [38.7077507, -9.1365919], 'Portugal'),
            'Bucharest': ('(OTP', 'Bucharest (OTP - Henri Coanda Intl.)', [44.4361414, 26.1027202], 'Romania'),
            'Cluj-Napoca': ('(CLJ', 'Cluj-Napoca (CLJ - Avram Iancu Cluj Intl.)', [46.769379, 23.5899542], 'Romania'),
            'Timisoara': ('(TSR', 'Timisoara (TSR - Traian Vuia Intl.)', [45.7538355, 21.2257474], 'Romania'),
            'Moscow': ('(SVO', 'Moscow (SVO - Sheremetyevo Intl.)', [55.7504461, 37.6174943], 'Russia'),
            'St. Petersburg': ('(LED', 'St. Petersburg (LED - Pulkovo Intl.)', [59.938732, 30.316229], 'Russia'),
            'Novosibirsk': ('(OVB', 'Novosibirsk (OVB - Tolmachevo Intl.)', [55.0288307, 82.9226887], 'Russia'),
            'Kigali': ('(KGL', 'Kigali (KGL - Kigali Intl.)', [-1.950851, 30.061507], 'Rwanda'), 'Basseterre': (
    '(SKB', 'Basseterre (SKB - Robert L. Bradshaw Intl.)', [17.2960919, -62.722301], 'Saint Kitts and Nevis'),
            'Castries': (
            '(SLU', 'Castries (SLU - George F. L. Charles Airport)', [13.90904385, -60.97792414113452], 'Saint Lucia'),
            'Kingstown': (
            '(SVD', 'Kingstown (SVD - Argyle Intl.)', [13.1561864, -61.2279621], 'Saint Vincent and the Grenadines'),
            'Apia': ('(APW', 'Apia (APW - Faleolo Intl.)', [-13.8344639, -171.7649144], 'Samoa'),
            'San Marino': ('(RMI', 'San Marino (RMI - Federico Fellini Intl.)', [43.9458623, 12.458306], 'San Marino'),
            'Sao Tome': ('(TMS', 'Sao Tome (TMS - Sao Tome Intl.)', [0.3389242, 6.7313031], 'Sao Tome and Principe'),
            'Riyadh': ('(RUH', 'Riyadh (RUH - King Khaled Intl.)', [24.638916, 46.7160104], 'Saudi Arabia'),
            'Jeddah': ('(JED', 'Jeddah (JED - King Abdulaziz Intl.)', [21.5810088, 39.1653612], 'Saudi Arabia'),
            'Dammam': ('(DMM', 'Dammam (DMM - King Fahd Intl.)', [26.4367824, 50.1039991], 'Saudi Arabia'),
            'Dakar': ('(DKR', 'Dakar (DKR - Blaise Diagne Intl.)', [14.693425, -17.447938], 'Senegal'),
            'Belgrade': ('(BEG', 'Belgrade (BEG - Nikola Tesla Intl.)', [44.8178131, 20.4568974], 'Serbia'),
            'Freetown': ('(FNA', 'Freetown (FNA - Lungi Intl.)', [8.479004, -13.26795], 'Sierra Leone'),
            'Singapore': ('(SIN', 'Singapore (SIN - Changi Intl.)', [1.357107, 103.8194992], 'Singapore'),
            'Bratislava': ('(BTS', 'Bratislava (BTS - M. R. Stefanik Airport)', [48.1516988, 17.1093063], 'Slovakia'),
            'Ljubljana': ('(LJU', 'Ljubljana (LJU - Joze Pucnik Airport)', [46.0500268, 14.5069289], 'Slovenia'),
            'Honiara': (
            '(HIR', 'Honiara (HIR - Honiara Intl.)', [-9.437797549999999, 159.9624174786047], 'Solomon Islands'),
            'Taipei': ('(TPE', 'Taipei (TPE - Taiwan Taoyuan Intl.)', [25.0375198, 121.5636796], 'Taiwan'),
            'Kaohsiung': ('(KHH', 'Kaohsiung (KHH - Kaohsiung Intl.)', [22.6203348, 120.3120375], 'Taiwan'),
            'Dushanbe': (
            '(DYU', 'Dushanbe (DYU - Dushanbe Intl.)', [38.585694700000005, 68.7603746751885], 'Tajikistan'),
            'Dar es Salaam': (
            '(DAR', 'Dar es Salaam (DAR - Julius Nyerere Intl.)', [-6.8160837, 39.2803583], 'Tanzania'),
            'Zanzibar City': (
            '(ZNZ', 'Zanzibar City (ZNZ - Abeid Amani Karume Intl.)', [-6.1664908, 39.2074312], 'Tanzania'),
            'Bangkok': ('(BKK', 'Bangkok (BKK - Suvarnabhumi Airport)', [13.7524938, 100.4935089], 'Thailand'),
            'Phuket': ('(HKT', 'Phuket (HKT - Phuket Intl.)', [7.9366015, 98.3529292], 'Thailand'),
            'Dili': ('(DIL', 'Dili (DIL - Presidente Nicolau Lobato Intl.)', [-8.5536809, 125.5784093], 'Timor-Leste'),
            'Lome': ('(LFW', 'Lome (LFW - Gnassingbe Eyadema Intl.)', [6.130419, 1.215829], 'Togo'),
            "Nuku'alofa": ('(TBU', "Nuku'alofa (TBU - Fua'amotu Intl.)", [-21.1343401, -175.201808], 'Tonga'),
            'Port of Spain': (
            '(POS', 'Port of Spain (POS - Piarco Intl.)', [10.6572678, -61.5180173], 'Trinidad and Tobago'),
            'Tunis': ('(TUN', 'Tunis (TUN - Carthage Intl.)', [33.8439408, 9.400138], 'Tunisia'),
            'Istanbul': ('(IST', 'Istanbul (IST - Istanbul Airport)', [41.0091982, 28.9662187], 'Turkey'),
            'Ankara': ('(ESB', 'Ankara (ESB - Esenboga Intl.)', [39.9207886, 32.8540482], 'Turkey'),
            'Antalya': ('(AYT', 'Antalya (AYT - Antalya Intl.)', [36.8872942, 30.7074549], 'Turkey'),
            'Ashgabat': ('(ASB', 'Ashgabat (ASB - Ashgabat Intl.)', [37.9404648, 58.3823487], 'Turkmenistan'),
            'Funafuti': ('(FUN', 'Funafuti (FUN - Funafuti Intl.)', [-8.5199633, 179.1982548], 'Tuvalu'),
            'Entebbe': ('(EBB', 'Entebbe (EBB - Entebbe Intl.)', [0.0611715, 32.4698564], 'Uganda'),
            'Kyiv': ('(KBP', 'Kyiv (KBP - Kyiv Boryspil Intl.)', [50.4500336, 30.5241361], 'Ukraine'),
            'Lviv': ('(LWO', 'Lviv (LWO - Lviv Danylo Halytskyi Intl.)', [49.841952, 24.0315921], 'Ukraine'), 'Dubai': (
    '(DXB', 'Dubai (DXB - Dubai Intl.)', [25.074282349999997, 55.18853865430702], 'United Arab Emirates'),
            'Abu Dhabi': (
            '(AUH', 'Abu Dhabi (AUH - Abu Dhabi Intl.)', [24.4538352, 54.3774014], 'United Arab Emirates'),
            'London': ('(LHR', 'London (LHR - London Heathrow Airport)', [51.5073359, -0.12765], 'United Kingdom'),
            'Manchester': ('(MAN', 'Manchester (MAN - Manchester Airport)', [53.4794892, -2.2451148], 'United Kingdom'),
            'New York': ('(JFK', 'New York (JFK - John F. Kennedy Intl.)', [40.7127281, -74.0060152], 'United States'),
            'Los Angeles': (
            '(LAX', 'Los Angeles (LAX - Los Angeles Intl.)', [34.0536909, -118.242766], 'United States'),
            'Chicago': ('(ORD', "Chicago (ORD - Chicago O'Hare Intl.)", [41.8755616, -87.6244212], 'United States'),
            'Montevideo': ('(MVD', 'Montevideo (MVD - Carrasco Intl.)', [-34.9058916, -56.1913095], 'Uruguay'),
            'Tashkent': ('(TAS', 'Tashkent (TAS - Tashkent Intl.)', [41.3123363, 69.2787079], 'Uzbekistan'),
            'Port Vila': ('(VLI', 'Port Vila (VLI - Bauerfield Intl.)', [-17.7414972, 168.3150163], 'Vanuatu'),
            'Caracas': ('(CCS', 'Caracas (CCS - Simon Bolivar Intl.)', [10.5060934, -66.9146008], 'Venezuela'),
            'Valencia': ('(VLN', 'Valencia (VLN - Arturo Michelena Intl.)', [10.170026, -68.0003987], 'Venezuela'),
            'Maracaibo': ('(MAR', 'Maracaibo (MAR - La Chinita Intl.)', [10.6498095, -71.6443596], 'Venezuela'),
            'Barquisimeto': ('(BRM', 'Barquisimeto (BRM - Jacinto Lara Intl.)', [10.0774374, -69.3222293], 'Venezuela'),
            'Puerto Ordaz': (
            '(PZO', 'Puerto Ordaz (PZO - Manuel Carlos Piar Intl.)', [8.2750351, -62.7558263], 'Venezuela'),
            'Porlamar': (
            '(PMV', 'Porlamar (PMV - Del Caribe Intl. Gen. Santiago Marino)', [10.9635839, -63.8464509], 'Venezuela'),
            'Hanoi': ('(HAN', 'Hanoi (HAN - Noi Bai Intl.)', [21.0294498, 105.8544441], 'Vietnam'),
            'Ho Chi Minh City': (
            '(SGN', 'Ho Chi Minh City (SGN - Tan Son Nhat Intl.)', [10.7764772, 106.701938], 'Vietnam'),
            'Da Nang': ('(DAD', 'Da Nang (DAD - Da Nang Intl.)', [16.068, 108.212], 'Vietnam'),
            'Nha Trang': ('(CXR', 'Nha Trang (CXR - Cam Ranh Intl.)', [12.2431693, 109.1898675], 'Vietnam'),
            'Phu Quoc': ('(PQC', 'Phu Quoc (PQC - Phu Quoc Intl.)', [10.2153093, 103.9880443], 'Vietnam'),
            'Futuna Island': ('(FUT)', 'Futuna Island (FUT)', [-14.276851, -178.14234997654432], 'Wallis and Futuna'),
            'Wallis Island': ('(WLS)', 'Wallis Island (WLS)', [-13.2846405, -176.20665679493294], 'Wallis and Futuna'),
            'Aden': ('(ADE', 'Aden (ADE - Aden Intl)', [12.833333, 44.916667], 'Yemen'),
            'Sanaa': ('(SAH', 'Sanaa (SAH - Sanaa Intl)', [15.3538569, 44.2058841], 'Yemen'),
            'Taiz': ('(TAI', 'Taiz (TAI - Taiz Intl)', [13.4115414, 43.5570871], 'Yemen'), 'Livingstone': (
    '(LVI', 'Livingstone (LVI - Harry Mwanga Nkumbula Intl)', [-17.853135, 25.861429], 'Zambia'),
            'Lusaka': ('(LUN', 'Lusaka (LUN - Kenneth Kaunda Intl)', [-15.4163395, 28.2818414], 'Zambia'),
            'Ndola': ('(NLA', 'Ndola (NLA - Simon Mwansa Kapwepwe Intl)', [-12.9693056, 28.6365894], 'Zambia'),
            'Bulawayo': ('(BUQ', 'Bulawayo (BUQ - Joshua Mqabuko Nkomo Intl)', [-20.1053948, 28.5426856], 'Zimbabwe'),
            'Harare': ('(HRE', 'Harare (HRE - Robert Gabriel Mugabe Intl)', [-17.831773, 31.045686], 'Zimbabwe'),
            'Victoria Falls': (
            '(VFA', 'Victoria Falls (VFA - Victoria Falls Intl)', [-17.9229035, 25.8490239], 'Zimbabwe')}

temp = {}
for data in airports_raw_data.items():
    for childData in data[1].items():
        if childData[0] in airports_data.keys() and data[0]:
            try:
                fullName = airports_data[childData[0]][0]
                localCode = fullName.replace('()', '').split(' -')[0]
                location = airports_data[childData[0]][1]
                temp[childData[0]] = (localCode, childData[0] + " " + fullName, location, data[0])
            except Exception as e:
                pass
print(temp)







#########################################################
# Getting of Longitude and Latitude of airport locations
#########################################################


# geolocator = Nominatim(user_agent='airport_locator')
# result = {}
# for country, airports in airports_raw_data.items():
#     for city, name in airports.items():
#         location = geolocator.geocode(city + ', ' + country)
#         if location is not None:
#             latitude = location.latitude
#             longitude = location.longitude
#             data = f"{city} {name}"
#             result[city] = (data, [latitude, longitude], country)
# print(result)


#########################################################
# Getting Data for scraping
#########################################################

# temp = {'Kabul': ('Kabul (KBL - Hamid Karzai Intl.)', [34.5260109, 69.1776838], 'Afghanistan'),
#         'Victoria Falls': ('Victoria Falls (VFA - Victoria Falls Intl)', [-17.9229035, 25.8490239], 'Zimbabwe')
#         }
# # for data in temp.items():
# #     print(f"Name: {data[0]}\tCode: {data[1][0].split('(')[1].split(' -')[0]}")
#
# result = {}
# # from geopy.geocoders import Nominatim
# for country, airports in airports_raw_data.items():
#     for city, name in temp.items():
#         data = f"{city} {name}"
#         print(data)
#         data_code = data.split('(')[1].split(' -')[0]
#         print(data_code)
#         # result[city] = (name, data_code, data, second_data[city][1], country)
# print(result)
