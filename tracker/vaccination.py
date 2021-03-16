import pandas as pd 

con = pd.DataFrame({
    "Country": {
        "0": "Afghanistan",
        "1": "Albania",
        "2": "Algeria",
        "3": "Angola",
        "4": "Antigua and Barbuda",
        "5": "Argentina",
        "6": "Armenia",
        "7": "Australia",
        "8": "Austria",
        "9": "Azerbaijan",
        "10": "Bahrain",
        "11": "Bangladesh",
        "12": "Barbados",
        "13": "Belarus",
        "14": "Belgium",
        "15": "Belize",
        "16": "Benin",
        "17": "Bermuda",
        "18": "Bhutan",
        "19": "Bolivia",
        "20": "Bosnia and Herzegovina",
        "21": "Botswana",
        "22": "Brazil",
        "23": "Brunei",
        "24": "Bulgaria",
        "25": "Burkina Faso",
        "26": "Burundi",
        "27": "Cambodia",
        "28": "Cameroon",
        "29": "Canada",
        "30": "Cape Verde",
        "31": "Cayman Islands",
        "32": "Central African Republic",
        "33": "Chad",
        "34": "Chile",
        "35": "China",
        "36": "Colombia",
        "37": "Comoros",
        "38": "Costa Rica",
        "39": "Croatia",
        "40": "Cuba",
        "41": "Cyprus",
        "42": "Denmark",
        "43": "Djibouti",
        "44": "Dominica",
        "45": "Dominican Republic",
        "46": "Ecuador",
        "47": "Egypt",
        "48": "El Salvador",
        "49": "Equatorial Guinea",
        "50": "Eritrea",
        "51": "Estonia",
        "52": "Ethiopia",
        "53": "Fiji",
        "54": "Finland",
        "55": "France",
        "56": "Gabon",
        "57": "Georgia",
        "58": "Germany",
        "59": "Ghana",
        "60": "Gibraltar",
        "61": "Greece",
        "62": "Greenland",
        "63": "Grenada",
        "64": "Guatemala",
        "65": "Guernsey",
        "66": "Guinea",
        "67": "Guinea-Bissau",
        "68": "Guyana",
        "69": "Haiti",
        "70": "Honduras",
        "71": "Hong Kong",
        "72": "Hungary",
        "73": "Iceland",
        "74": "India",
        "75": "Indonesia",
        "76": "Iran",
        "77": "Iraq",
        "78": "Ireland",
        "79": "Isle of Man",
        "80": "Israel",
        "81": "Italy",
        "82": "Jamaica",
        "83": "Japan",
        "84": "Jersey",
        "85": "Jordan",
        "86": "Kazakhstan",
        "87": "Kenya",
        "88": "Kuwait",
        "89": "Kyrgyzstan",
        "90": "Laos",
        "91": "Latvia",
        "92": "Lebanon",
        "93": "Lesotho",
        "94": "Liberia",
        "95": "Libya",
        "96": "Liechtenstein",
        "97": "Lithuania",
        "98": "Luxembourg",
        "99": "Madagascar",
        "100": "Malawi",
        "101": "Malaysia",
        "102": "Maldives",
        "103": "Mali",
        "104": "Malta",
        "105": "Marshall Islands",
        "106": "Mauritania",
        "107": "Mauritius",
        "108": "Mexico",
        "109": "Moldova",
        "110": "Monaco",
        "111": "Mongolia",
        "112": "Morocco",
        "113": "Mozambique",
        "114": "Namibia",
        "115": "Nepal",
        "116": "Netherlands",
        "117": "New Zealand",
        "118": "Nicaragua",
        "119": "Niger",
        "120": "Nigeria",
        "121": "Norway",
        "122": "Oman",
        "123": "Pakistan",
        "124": "Panama",
        "125": "Papua New Guinea",
        "126": "Paraguay",
        "127": "Peru",
        "128": "Philippines",
        "129": "Poland",
        "130": "Portugal",
        "131": "Qatar",
        "132": "Romania",
        "133": "Russia",
        "134": "Rwanda",
        "135": "Saint Helena",
        "136": "Saint Kitts and Nevis",
        "137": "Saint Lucia",
        "138": "Saint Vincent and the Grenadines",
        "139": "Samoa",
        "140": "San Marino",
        "141": "Saudi Arabia",
        "142": "Senegal",
        "143": "Serbia",
        "144": "Seychelles",
        "145": "Sierra Leone",
        "146": "Singapore",
        "147": "Slovakia",
        "148": "Slovenia",
        "149": "Solomon Islands",
        "150": "Somalia",
        "151": "South Africa",
        "152": "South Korea",
        "153": "South Sudan",
        "154": "Spain",
        "155": "Sri Lanka",
        "156": "Sudan",
        "157": "Suriname",
        "158": "Sweden",
        "159": "Switzerland",
        "160": "Syria",
        "161": "Taiwan",
        "162": "Tajikistan",
        "163": "Tanzania",
        "164": "Thailand",
        "165": "Togo",
        "166": "Trinidad and Tobago",
        "167": "Tunisia",
        "168": "Turkey",
        "169": "Uganda",
        "170": "Ukraine",
        "171": "United Arab Emirates",
        "172": "United Kingdom",
        "173": "United States",
        "174": "Uruguay",
        "175": "Uzbekistan",
        "176": "Vanuatu",
        "177": "Venezuela",
        "178": "Vietnam",
        "179": "Yemen",
        "180": "Zambia",
        "181": "Zimbabwe"
    },
    "capital": {
        "0": "Kabul",
        "1": "Tirana",
        "2": "Algiers",
        "3": "Luanda",
        "4": "Saint John's",
        "5": "Buenos Aires",
        "6": "Yerevan",
        "7": "Canberra",
        "8": "Vienna",
        "9": "Baku",
        "10": "Manama",
        "11": "Dhaka",
        "12": "Bridgetown",
        "13": "Minsk",
        "14": "Brussels",
        "15": "Belmopan",
        "16": "Porto-Novo",
        "17": "Hamilton",
        "18": "Thimphu",
        "19": "Sucre",
        "20": "Sarajevo",
        "21": "Gaborone",
        "22": "Bras\u00edlia",
        "23": "Bandar Seri Begawan",
        "24": "Sofia",
        "25": "Ouagadougou",
        "26": "Bujumbura",
        "27": "Phnom Penh",
        "28": "Yaound\u00e9",
        "29": "Ottawa",
        "30": "Praia",
        "31": "George Town",
        "32": "Bangui",
        "33": "N'Djamena",
        "34": "Santiago",
        "35": "Beijing",
        "36": "Bogot\u00e1",
        "37": "Moroni",
        "38": "San Jos\u00e9",
        "39": "Zagreb",
        "40": "Havana",
        "41": "Nicosia",
        "42": "Copenhagen",
        "43": "Djibouti",
        "44": "Roseau",
        "45": "Santo Domingo",
        "46": "Quito",
        "47": "Cairo",
        "48": "San Salvador",
        "49": "Malabo",
        "50": "Asmara",
        "51": "Tallinn",
        "52": "Addis Ababa",
        "53": "Suva",
        "54": "Helsinki",
        "55": "Paris",
        "56": "Libreville",
        "57": "Tbilisi",
        "58": "Berlin",
        "59": "Accra",
        "60": "Gibraltar",
        "61": "Athens",
        "62": "Nuuk",
        "63": "St. George's",
        "64": "Guatemala City",
        "65": "St. Peter Port",
        "66": "Conakry",
        "67": "Bissau",
        "68": "Georgetown",
        "69": "Port-au-Prince",
        "70": "Tegucigalpa",
        "71": "City of Victoria",
        "72": "Budapest",
        "73": "Reykjavik",
        "74": "New Delhi",
        "75": "Jakarta",
        "76": "Tehran",
        "77": "Baghdad",
        "78": "Dublin",
        "79": "Douglas",
        "80": "Jerusalem",
        "81": "Rome",
        "82": "Kingston",
        "83": "Tokyo",
        "84": "Saint Helier",
        "85": "Amman",
        "86": "Astana",
        "87": "Nairobi",
        "88": "Kuwait City",
        "89": "Bishkek",
        "90": "Vientiane",
        "91": "Riga",
        "92": "Beirut",
        "93": "Maseru",
        "94": "Monrovia",
        "95": "Tripoli",
        "96": "Vaduz",
        "97": "Vilnius",
        "98": "Luxembourg",
        "99": "Antananarivo",
        "100": "Lilongwe",
        "101": "Kuala Lumpur",
        "102": "Mal\u00e9",
        "103": "Bamako",
        "104": "Valletta",
        "105": "Majuro",
        "106": "Nouakchott",
        "107": "Port Louis",
        "108": "Mexico City",
        "109": "Chi\u0219in\u0103u",
        "110": "Monaco",
        "111": "Ulan Bator",
        "112": "Rabat",
        "113": "Maputo",
        "114": "Windhoek",
        "115": "Kathmandu",
        "116": "Amsterdam",
        "117": "Wellington",
        "118": "Managua",
        "119": "Niamey",
        "120": "Abuja",
        "121": "Oslo",
        "122": "Muscat",
        "123": "Islamabad",
        "124": "Panama City",
        "125": "Port Moresby",
        "126": "Asunci\u00f3n",
        "127": "Lima",
        "128": "Manila",
        "129": "Warsaw",
        "130": "Lisbon",
        "131": "Doha",
        "132": "Bucharest",
        "133": "Moscow",
        "134": "Kigali",
        "135": "Jamestown",
        "136": "Basseterre",
        "137": "Castries",
        "138": "Kingstown",
        "139": "Apia",
        "140": "City of San Marino",
        "141": "Riyadh",
        "142": "Dakar",
        "143": "Belgrade",
        "144": "Victoria",
        "145": "Freetown",
        "146": "Singapore",
        "147": "Bratislava",
        "148": "Ljubljana",
        "149": "Honiara",
        "150": "Mogadishu",
        "151": "Pretoria",
        "152": "Seoul",
        "153": "Juba",
        "154": "Madrid",
        "155": "Colombo",
        "156": "Khartoum",
        "157": "Paramaribo",
        "158": "Stockholm",
        "159": "Bern",
        "160": "Damascus",
        "161": "Taipei",
        "162": "Dushanbe",
        "163": "Dodoma",
        "164": "Bangkok",
        "165": "Lom\u00e9",
        "166": "Port of Spain",
        "167": "Tunis",
        "168": "Ankara",
        "169": "Kampala",
        "170": "Kiev",
        "171": "Abu Dhabi",
        "172": "London",
        "173": "Washington D.C.",
        "174": "Montevideo",
        "175": "Tashkent",
        "176": "Port Vila",
        "177": "Caracas",
        "178": "Hanoi",
        "179": "Sana'a",
        "180": "Lusaka",
        "181": "Harare"
    },
    "lat_lon": {
        "0": [
            "34.5260109",
            "69.1776838"
        ],
        "1": [
            "41.3305141",
            "19.825562857582966"
        ],
        "2": [
            "28.0000272",
            "2.9999825"
        ],
        "3": [
            "-8.8272699",
            "13.2439512"
        ],
        "4": [
            "17.1184569",
            "-61.8448509"
        ],
        "5": [
            "-34.6075682",
            "-58.4370894"
        ],
        "6": [
            "40.1776121",
            "44.5125849"
        ],
        "7": [
            "-35.2975906",
            "149.1012676"
        ],
        "8": [
            "48.2083537",
            "16.3725042"
        ],
        "9": [
            "40.3754434",
            "49.8326748"
        ],
        "10": [
            "26.2235041",
            "50.5822436"
        ],
        "11": [
            "23.810651",
            "90.4126466"
        ],
        "12": [
            "13.0977832",
            "-59.6184184"
        ],
        "13": [
            "53.902334",
            "27.5618791"
        ],
        "14": [
            "50.8465573",
            "4.351697"
        ],
        "15": [
            "17.250199",
            "-88.770018"
        ],
        "16": [
            "6.4990718",
            "2.6253361"
        ],
        "17": [
            "43.2560802",
            "-79.8728583"
        ],
        "18": [
            "27.4713546",
            "89.6336729"
        ],
        "19": [
            "-19.0477251",
            "-65.2594306"
        ],
        "20": [
            "43.8519774",
            "18.3866868"
        ],
        "21": [
            "-24.6581357",
            "25.9088474"
        ],
        "22": [
            "-10.3333333",
            "-53.2"
        ],
        "23": [
            "4.8895453",
            "114.9417574"
        ],
        "24": [
            "-15.2538402",
            "48.2562163"
        ],
        "25": [
            "12.3681873",
            "-1.5270944"
        ],
        "26": [
            "-3.3638125",
            "29.3675028"
        ],
        "27": [
            "11.568271",
            "104.9224426"
        ],
        "28": [
            "3.8689867",
            "11.5213344"
        ],
        "29": [
            "45.421106",
            "-75.690308"
        ],
        "30": [
            "14.9160169",
            "-23.5096132"
        ],
        "31": [
            "5.4145681",
            "100.3298035"
        ],
        "32": [
            "4.3907153",
            "18.5509126"
        ],
        "33": [
            "12.1191543",
            "15.0502758"
        ],
        "34": [
            "9.8694792",
            "-83.7980749"
        ],
        "35": [
            "39.9065084",
            "116.3912391"
        ],
        "36": [
            "4.6533326",
            "-74.083652"
        ],
        "37": [
            "-11.6931255",
            "43.2543044"
        ],
        "38": [
            "9.9325427",
            "-84.0795782"
        ],
        "39": [
            "45.8131847",
            "15.9771774"
        ],
        "40": [
            "23.135305",
            "-82.3589631"
        ],
        "41": [
            "35.1739302",
            "33.364726"
        ],
        "42": [
            "55.6867243",
            "12.5700724"
        ],
        "43": [
            "11.8145966",
            "42.8453061"
        ],
        "44": [
            "48.7710371",
            "-95.7697882"
        ],
        "45": [
            "18.4801972",
            "-69.942111"
        ],
        "46": [
            "-0.2201641",
            "-78.5123274"
        ],
        "47": [
            "30.0443879",
            "31.2357257"
        ],
        "48": [
            "13.6989939",
            "-89.1914249"
        ],
        "49": [
            "3.752828",
            "8.780061"
        ],
        "50": [
            "15.3389667",
            "38.9326763"
        ],
        "51": [
            "59.4372155",
            "24.7453688"
        ],
        "52": [
            "9.0107934",
            "38.7612525"
        ],
        "53": [
            "-18.1415884",
            "178.4421662"
        ],
        "54": [
            "60.1674881",
            "24.9427473"
        ],
        "55": [
            "48.8566969",
            "2.3514616"
        ],
        "56": [
            "0.390002",
            "9.454001"
        ],
        "57": [
            "41.6934591",
            "44.8014495"
        ],
        "58": [
            "52.5170365",
            "13.3888599"
        ],
        "59": [
            "5.5600141",
            "-0.2057437"
        ],
        "60": [
            "36.140807",
            "-5.3541295"
        ],
        "61": [
            "37.9839412",
            "23.7283052"
        ],
        "62": [
            "64.175029",
            "-51.7355386"
        ],
        "63": [
            "48.6581382",
            "6.9280988"
        ],
        "64": [
            "14.6222328",
            "-90.5185188"
        ],
        "65": [
            "49.4568142",
            "-2.5389979"
        ],
        "66": [
            "9.5170602",
            "-13.6998434"
        ],
        "67": [
            "11.861324",
            "-15.583055"
        ],
        "68": [
            "6.8137426",
            "-58.1624465"
        ],
        "69": [
            "18.547327",
            "-72.3395928"
        ],
        "70": [
            "14.1056861",
            "-87.204676"
        ],
        "71": [
            "-37.8142176",
            "144.9631608"
        ],
        "72": [
            "47.48138955",
            "19.14607278448202"
        ],
        "73": [
            "64.145981",
            "-21.9422367"
        ],
        "74": [
            "28.6138954",
            "77.2090057"
        ],
        "75": [
            "-6.1753942",
            "106.827183"
        ],
        "76": [
            "35.6892523",
            "51.3896004"
        ],
        "77": [
            "33.3024309",
            "44.3787992"
        ],
        "78": [
            "53.3497645",
            "-6.2602732"
        ],
        "79": [
            "39.7628415",
            "-88.2170516"
        ],
        "80": [
            "31.79592425",
            "35.21198075969497"
        ],
        "81": [
            "41.8933203",
            "12.4829321"
        ],
        "82": [
            "17.9712148",
            "-76.7928128"
        ],
        "83": [
            "35.6828387",
            "139.7594549"
        ],
        "84": [
            "47.3843871",
            "4.6833254"
        ],
        "85": [
            "31.9515694",
            "35.9239625"
        ],
        "86": [
            "51.1282205",
            "71.4306682"
        ],
        "87": [
            "-1.3031689499999999",
            "36.826061224105075"
        ],
        "88": [
            "29.3797091",
            "47.9735629"
        ],
        "89": [
            "42.8765615",
            "74.6070079"
        ],
        "90": [
            "17.9640988",
            "102.6133707"
        ],
        "91": [
            "56.9493977",
            "24.1051846"
        ],
        "92": [
            "33.8959203",
            "35.47843"
        ],
        "93": [
            "-29.310054",
            "27.478222"
        ],
        "94": [
            "6.328034",
            "-10.797788"
        ],
        "95": [
            "32.896672",
            "13.1777923"
        ],
        "96": [
            "47.1392862",
            "9.5227962"
        ],
        "97": [
            "54.6870458",
            "25.2829111"
        ],
        "98": [
            "49.8158683",
            "6.1296751"
        ],
        "99": [
            "-18.9100122",
            "47.5255809"
        ],
        "100": [
            "-13.9875107",
            "33.768144"
        ],
        "101": [
            "3.1516964",
            "101.6942371"
        ],
        "102": [
            "16.3700359",
            "-2.2900239"
        ],
        "103": [
            "12.61326555",
            "-7.984739136241295"
        ],
        "104": [
            "35.8989818",
            "14.5136759"
        ],
        "105": [
            "7.0909924",
            "171.3816354"
        ],
        "106": [
            "18.0792379",
            "-15.9780071"
        ],
        "107": [
            "-20.1637281",
            "57.5045331"
        ],
        "108": [
            "19.4326296",
            "-99.1331785"
        ],
        "109": [
            "47.0245117",
            "28.8322923"
        ],
        "110": [
            "43.73844905",
            "7.424224092532953"
        ],
        "111": [
            "47.9184676",
            "106.9177016"
        ],
        "112": [
            "33.9667424",
            "-6.842641008106102"
        ],
        "113": [
            "-25.966213",
            "32.56745"
        ],
        "114": [
            "-22.5743922",
            "17.0790688"
        ],
        "115": [
            "27.708317",
            "85.3205817"
        ],
        "116": [
            "52.3727598",
            "4.8936041"
        ],
        "117": [
            "-41.2887953",
            "174.7772114"
        ],
        "118": [
            "12.1459907",
            "-86.2746665"
        ],
        "119": [
            "13.524834",
            "2.109823"
        ],
        "120": [
            "9.0643305",
            "7.4892974"
        ],
        "121": [
            "59.9133301",
            "10.7389701"
        ],
        "122": [
            "23.5882019",
            "58.3829448"
        ],
        "123": [
            "33.6938118",
            "73.0651511"
        ],
        "124": [
            "30.1600827",
            "-85.6545729"
        ],
        "125": [
            "-9.4743301",
            "147.1599504"
        ],
        "126": [
            "-25.2800459",
            "-57.6343814"
        ],
        "127": [
            "-12.0621065",
            "-77.0365256"
        ],
        "128": [
            "14.5907332",
            "120.9809674"
        ],
        "129": [
            "52.2319581",
            "21.0067249"
        ],
        "130": [
            "38.7077507",
            "-9.1365919"
        ],
        "131": [
            "25.2856329",
            "51.5264162"
        ],
        "132": [
            "44.4361414",
            "26.1027202"
        ],
        "133": [
            "55.7504461",
            "37.6174943"
        ],
        "134": [
            "-1.950851",
            "30.061507"
        ],
        "135": [
            "37.2104434",
            "-76.7738928"
        ],
        "136": [
            "17.2960919",
            "-62.722301"
        ],
        "137": [
            "13.952589249999999",
            "-60.98782353129866"
        ],
        "138": [
            "13.1561864",
            "-61.2279621"
        ],
        "139": [
            "-13.8343691",
            "-171.7692793"
        ],
        "140": [
            "43.9363996",
            "12.4466991"
        ],
        "141": [
            "24.638916",
            "46.7160104"
        ],
        "142": [
            "14.693425",
            "-17.447938"
        ],
        "143": [
            "44.8178131",
            "20.4568974"
        ],
        "144": [
            "-36.5986096",
            "144.6780052"
        ],
        "145": [
            "8.479004",
            "-13.26795"
        ],
        "146": [
            "1.357107",
            "103.8194992"
        ],
        "147": [
            "48.1516988",
            "17.1093063"
        ],
        "148": [
            "46.0499803",
            "14.5068602"
        ],
        "149": [
            "-9.437797549999999",
            "159.9624174786047"
        ],
        "150": [
            "2.0349312",
            "45.3419183"
        ],
        "151": [
            "-25.7459374",
            "28.1879444"
        ],
        "152": [
            "37.5666791",
            "126.9782914"
        ],
        "153": [
            "4.8472017",
            "31.5951655"
        ],
        "154": [
            "40.4167047",
            "-3.7035825"
        ],
        "155": [
            "6.9349969",
            "79.8538463"
        ],
        "156": [
            "15.593325",
            "32.53565"
        ],
        "157": [
            "5.8216091",
            "-55.1770432"
        ],
        "158": [
            "59.3251172",
            "18.0710935"
        ],
        "159": [
            "46.9482713",
            "7.4514512"
        ],
        "160": [
            "33.5130695",
            "36.3095814"
        ],
        "161": [
            "25.0375198",
            "121.5636796"
        ],
        "162": [
            "38.5762709",
            "68.7863573"
        ],
        "163": [
            "-6.3372817",
            "35.73717712327764"
        ],
        "164": [
            "13.7544238",
            "100.4930399"
        ],
        "165": [
            "6.130419",
            "1.215829"
        ],
        "166": [
            "10.6572678",
            "-61.5180173"
        ],
        "167": [
            "33.8439408",
            "9.400138"
        ],
        "168": [
            "39.9207486",
            "32.8540093"
        ],
        "169": [
            "0.3177137",
            "32.5813539"
        ],
        "170": [
            "50.4500336",
            "30.5241361"
        ],
        "171": [
            "24.4538352",
            "54.3774014"
        ],
        "172": [
            "51.5073219",
            "-0.1276474"
        ],
        "173": [
            "38.8949924",
            "-77.0365581"
        ],
        "174": [
            "-34.9058916",
            "-56.1913095"
        ],
        "175": [
            "41.3123363",
            "69.2787079"
        ],
        "176": [
            "-17.7414972",
            "168.3150163"
        ],
        "177": [
            "10.506098",
            "-66.9146017"
        ],
        "178": [
            "21.0294498",
            "105.8544441"
        ],
        "179": [
            "15.3538569",
            "44.2058841"
        ],
        "180": [
            "-15.4164488",
            "28.2821535"
        ],
        "181": [
            "-17.831773",
            "31.045686"
        ]
    }
})



covid = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
covid_vac = covid.loc[: , ['location','total_cases', 'new_cases',  'total_deaths', 'new_deaths', 'total_vaccinations', 'new_vaccinations']]
t = covid_vac.groupby("location").max()
t = pd.merge(t, con , left_on=t.index ,right_on =con.Country ).fillna(0)
cleared_covid_dataset = pd.DataFrame({
    "Country" :                 t.Country,
    "lat_lon" :                 t.lat_lon, 
    "total_cases" :             t.total_cases,
    "new_cases" :               t.new_cases,
    "total_deaths" :            t.total_deaths,
    "new_deaths" :              t.new_deaths,	
    "total_vaccinations":       t.total_vaccinations,
    "new_vaccinations" :        t.new_vaccinations
})

class vaccinations_info() :
    def __init__(self,index, Country, lat_lon, total_cases, new_cases, total_deaths, new_deaths,  total_vaccinations, new_vaccinations):
      self.index = index+1
      self.Country = Country
      self.lat_lon = lat_lon
      self.total_cases = total_cases
      self.new_cases = new_cases 
      self.total_deaths = total_deaths
      self.new_deaths = new_deaths 
      self.total_vaccinations = total_vaccinations
      self.new_vaccinations = new_vaccinations
    


def sort_values_by(sort_index=1) :
    if sort_index == 0 : 
        sort_index =  cleared_covid_dataset.columns[sort_index]
        temp = cleared_covid_dataset.sort_values(sort_index,).reset_index(drop=True)
    else :
        sort_index =  cleared_covid_dataset.columns[sort_index+1]
        temp = cleared_covid_dataset.sort_values(sort_index, ascending=False).reset_index(drop=True)
    
    result = []
    # print(sort_index)
    for ind in range(len(temp)) :
        result.append(vaccinations_info(temp.index[ind], temp.Country[ind], temp.lat_lon[ind], temp.total_cases[ind], temp.new_cases[ind], temp.total_deaths[ind], temp.new_deaths[ind] , temp.total_vaccinations[ind], temp.new_vaccinations[ind]))
    return {
    "info" : result
    }