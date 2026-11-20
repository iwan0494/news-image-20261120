# Data for the 20 November 2026 world-news poster (round 2).
# Every item happened, or was first reported, on Friday 20 November 2026.
# Fields: num, head (headline), body (one short paragraph), src (source tag),
# region (region tag), place (map label), utc (verified UTC time, if any),
# art (lead illustration kind) / icon (card icon kind).

LEADS = [
    {
        "num": 1,
        "head": "COURT FINDS MYANMAR GUILTY OF GENOCIDE",
        "body": "The World Court rules 9-6 that Myanmar committed genocide "
                "against the Rohingya - a first for the court. 1.3 million "
                "remain displaced.",
        "src": "BBC / UN NEWS",
        "region": "EUROPE",
        "place": "The Hague",
        "art": "scales",
    },
    {
        "num": 2,
        "head": "TRUMP, XI AND PUTIN MEET IN SHENZHEN",
        "body": "First three-way summit lasts 70 minutes and ends with a "
                "four-point declaration - no breakthrough on Ukraine "
                "or Iran.",
        "src": "BBC / GUARDIAN",
        "region": "ASIA",
        "place": "Shenzhen",
        "art": "summit",
    },
    {
        "num": 3,
        "head": "CYCLONE AKVAN MAKES LANDFALL IN INDIA",
        "body": "Akvan crosses near Gopalpur at 02:00 UTC with 70-80 km/h "
                "winds; 300,000 evacuated, 423 rescue teams out.",
        "src": "IMD / HINDU BUSINESSLINE",
        "region": "ASIA",
        "place": "Gopalpur",
        "utc": "02:00",
        "art": "cyclone",
    },
]

CARDS = [
    {
        "num": 4,
        "head": "KYIV BARRAGE: ~100 MISSILES, 400 DRONES",
        "body": "Biggest combined strike on Kyiv: 3 Dnipro bridges hit, "
                "3 killed, 15 hurt.",
        "src": "REUTERS",
        "region": "EUROPE",
        "place": "Kyiv",
        "icon": "missile",
    },
    {
        "num": 5,
        "head": "COP31 DRAFT DROPS FOSSIL PHASE-OUT",
        "body": "Antalya draft cut 144 to 80 paragraphs; fossil phase-out "
                "and $120bn gone.",
        "src": "JAPAN TIMES",
        "region": "CLIMATE",
        "place": "Antalya",
        "icon": "draft",
    },
    {
        "num": 6,
        "head": "ASIA AI SELL-OFF: NIKKEI -4.8%",
        "body": "SoftBank -14.6%, KOSPI -5.2%, Taiex worst week since 1990.",
        "src": "REUTERS",
        "region": "ASIA",
        "place": "Tokyo",
        "icon": "down",
    },
    {
        "num": 7,
        "head": "ANTHROPIC DEBUT: +17% TO ~$97",
        "body": "Record $81.3bn IPO, valued near $1.5tn; opened $111.50 "
                "from $83.",
        "src": "BBC",
        "region": "NORTH AMERICA",
        "place": "New York",
        "icon": "up",
    },
    {
        "num": 8,
        "head": "HOUTHI MISSILE HITS RIYADH PIF TOWER",
        "body": "PIF tower hit in Riyadh financial district; 1 missile, "
                "5 drones stopped.",
        "src": "SKY NEWS",
        "region": "MIDDLE EAST",
        "place": "Riyadh",
        "icon": "tower",
    },
    {
        "num": 9,
        "head": "BERLIN SUMMIT; CRIMEA BRIDGE HIT",
        "body": "Allies weigh NATO-style guarantees; 3rd Crimea Bridge "
                "hit this week.",
        "src": "BBC",
        "region": "EUROPE",
        "place": "Berlin",
        "icon": "bridge",
    },
    {
        "num": 10,
        "head": "KENYA FREES LAST EBOLA PATIENT",
        "body": "Outbreak contained 37 days after first case; C. auris "
                "also found.",
        "src": "ALLAFRICA",
        "region": "AFRICA",
        "place": "Nairobi",
        "icon": "virus",
    },
    {
        "num": 11,
        "head": "IMF: WORLD DEBT NEARS 100% OF GDP",
        "body": "Highest since WWII, says Georgieva; states urged to "
                "prepare for AI.",
        "src": "MERCOPRESS",
        "region": "GLOBAL",
        "place": "Washington",
        "icon": "percent",
    },
    {
        "num": 12,
        "head": "FAA GROUND STOP STRANDS 1.5M FLYERS",
        "body": "Ground stop leaves 1.5 million travellers stuck at US "
                "airports.",
        "src": "WIRES",
        "region": "NORTH AMERICA",
        "place": "USA",
        "icon": "plane",
    },
    {
        "num": 13,
        "head": "GTA 6 LAUNCH TOPS $2.3 BILLION",
        "body": "Worldwide release after 13 years; biggest entertainment "
                "launch ever.",
        "src": "BBC",
        "region": "CULTURE",
        "place": "Edinburgh",
        "icon": "game",
    },
]

BRIEFS = [
    (14, "Italy fines Meta \u20ac805M",
     "over Android photo access.", "WIRES", "EUROPE"),
    (15, "European youth plan strike",
     "25+ countries protest living costs, militarisation.", "STRAITS TIMES", "EUROPE"),
    (16, "Italy nationwide strike",
     "over wages and the cost of living.", "WIRES", "EUROPE"),
    (17, "US Senate passes energy bill 62-33",
     "data centres pay for grid.", "REUTERS", "NORTH AMERICA"),
    (18, "Bukele registers for third term",
     "six-year term; limits scrapped 2025.", "AL JAZEERA", "LATIN AMERICA"),
    (19, "Africa wants $120bn a year to adapt",
     "need $305bn by 2035; got $28-32bn in 2024.", "UNEP", "AFRICA"),
    (20, "Vatican lifts 25m Christmas tree",
     "into place in St Peter's Square.", "WIRES", "EUROPE"),
    (21, "Hormuz tanker attacks intensify",
     "tanker burns after mine; US war cost $48.3bn.", "CBS", "MIDDLE EAST"),
    (22, "Israel crosses Yellow Line in Gaza",
     "first truce breach; baby dies of cold in floods.", "BBC", "MIDDLE EAST"),
    (23, "California probes Nvidia",
     "subpoena on chips to China; CEO Huang resigns.", "BBC", "NORTH AMERICA"),
    (24, "UK-EU youth mobility deal",
     "100,000 young people a year to travel, work, study.", "BBC", "EUROPE"),
    (25, "Drone strike kills 10 in Sudan",
     "Amnesty urges probe of 9 RSF attacks.", "ALLAFRICA", "AFRICA"),
    (26, "Haiti raid kills 34 gang suspects",
     "Martissant corridor retaken.", "AL JAZEERA", "LATIN AMERICA"),
    (27, "Migrant boat capsizes off Senegal",
     "50-100 aboard; dozens missing, 4 bodies found.", "BBC", "AFRICA"),
    (28, "US-Venezuela military deal signed",
     "Hegseth in Caracas; 'threat' now 'partner'.", "BBC", "LATIN AMERICA"),
    (29, "Brazil recognises Raoni ancestral land",
     "Lula protects Kayapo territory.", "AL JAZEERA", "LATIN AMERICA"),
    (30, "White House fires cyber director",
     "Cairncross out; Davies steps in.", "FRANCE 24", "NORTH AMERICA"),
    (31, "UN chief race stalls after 8 votes",
     "Security Council split; UN may go leaderless.", "GUARDIAN", "GLOBAL"),
    (32, "Bangladesh unrest before Hasina return",
     "protests, arson; passport refused.", "GUARDIAN", "ASIA"),
    (33, "Iraq orders militia out of Jurf al-Nasr",
     "militia given until Friday to leave.", "EURONEWS", "MIDDLE EAST"),
    (34, "Voyager 1 reaches one light-day",
     "over 26bn km out, 49 years after launch.", "NASA", "SPACE"),
    (35, "BepiColombo reaches Mercury orbit",
     "second mission ever to orbit the planet.", "GUARDIAN", "SPACE"),
    (36, "Fiji, Tonga declare El Nino disasters",
     "drought crisis; Cook Islands emergency.", "RFI", "OCEANIA"),
]

STATS = [
    ("9-6", "ICJ GENOCIDE VOTE"),
    ("+17%", "ANTHROPIC DEBUT"),
    ("-4.8%", "NIKKEI"),
    ("100+400", "MISSILES + DRONES, KYIV"),
    ("300K", "EVACUATED, AKVAN"),
    ("$2.3BN", "GTA 6 SALES"),
]

RAIL = [
    (2.0, "02:00", "AKVAN LANDFALL"),
    (3.32, "03:19", "SENATE VOTE"),
    (6.0, "06:00", "NIKKEI CLOSE"),
    (21.0, "21:00", "ANTHROPIC CLOSE"),
]

# Map dots: (story num, x, y) inside a 620 x 96 map strip.
MAP_DOTS = [
    (1, 298, 26), (2, 520, 52), (3, 468, 58), (4, 330, 30),
    (5, 352, 46), (6, 560, 42), (7, 108, 38), (8, 382, 54),
    (9, 308, 22), (10, 362, 60), (11, 102, 44), (12, 62, 42),
    (13, 288, 16),
]

MAP_PLACES = [
    (1, "The Hague"), (2, "Shenzhen"), (3, "Gopalpur"), (4, "Kyiv"),
    (5, "Antalya"), (6, "Tokyo"), (7, "New York"), (8, "Riyadh"),
    (9, "Berlin"), (10, "Nairobi"), (11, "Washington"), (12, "USA"),
    (13, "Edinburgh"),
]
