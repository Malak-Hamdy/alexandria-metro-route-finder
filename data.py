graph = {
    "aboqir": ["elmaamora"],
    "elmaamora": ["aboqir", "elmontazah"],
    "elmontazah": ["elmaamora", "elmandara"],
    "elmandara": ["elmontazah", "elasafra"],
    "elasafra": ["elmandara", "sidibeshr"],
    "sidibeshr": ["elasafra", "victoria", "loran"],
    "victoria": ["loran", "sidibeshr"],
    "loran": ["sidibeshr", "victoria", "sanstefano", "clocksquare"],
    "sanstefano": ["loran", "glem"],

    "glem": ["sanstefano", "stanly"],
    "stanly": ["glem", "roushdi"],
    "roushdi": ["stanly", "sidigaber"],
    "sidigaber": ["roushdi", "smouha", "sporting"],
    "sporting": ["sidigaber", "kilopatra"],
    "kilopatra": ["sporting", "campshizar"],
    "campshizar": ["kilopatra", "elibrahimia"],
    "elibrahimia": ["campshizar", "elshatby"],
    "elshatby": ["elibrahimia", "elazarita"],
    "elazarita": ["elshatby", "mahatetelramel"],

    "clocksquare": ["loran", "abosuliman", "elsiof"],
    "abosuliman": ["clocksquare", "smouha"],
    "smouha": ["abosuliman", "sidigaber"],

    "elsiof": ["clocksquare", "falaky", "elawayid"],
    "falaky": ["elsiof", "ezbetmohsen"],
    "ezbetmohsen": ["falaky"],
    "elawayid": ["elsiof", "abis"],
    "abis": ["elawayid", "eldaary"],
    "eldaary": ["abis", "moharambek"],
    "moharambek": ["eldaary", "elhadra"],
    "elhadra": ["moharambek", "karmouz"],
    "karmouz": ["elhadra", "elmanshia"],
    "elmanshia": ["karmouz", "mahatetelramel"],
    "mahatetelramel": ["elmanshia", "bahary", "elazarita"],
    "bahary": ["mahatetelramel"]

}

positions = {
    "aboqir": (1317, 15),
    "elmaamora": (1227, 15),
    "elmontazah": (1103, 15),
    "elmandara": (977, 15),
    "elasafra": (857, 15),
    "sidibeshr": (737, 15),
    "victoria": (737, 77),
    "loran": (584, 77),
    "sanstefano": (355, 77),

    "glem": (128, 77),

    "stanly": (128, 140),

    "roushdi": (128, 205),

    "sidigaber": (128, 275),

    "sporting": (128, 345),
    "kilopatra": (128, 415),
    "campshizar": (128, 490),

    "elibrahimia": (128, 575),
    "elshatby": (128, 663),
    "elazarita": (230, 663),
    "mahatetelramel": (332, 663),
    "bahary": (332, 576),
    "elmanshia": (435, 663),
    "karmouz": (534, 663),
    "elhadra": (653, 663),
    "moharambek": (803, 663),
    "eldaary": (975, 663),
    "abis": (1213, 663),
    "elawayid": (1211, 140),
    "elsiof": (900, 140),

    "falaky": (900, 285),
    "ezbetmohsen": (900, 440),

    "clocksquare": (584, 145),
    "abosuliman": (584, 205),
    "smouha": (584, 275),

}
