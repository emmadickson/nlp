""" Constants used throughout the application """

# Stop Words
ENGLISH_STOP_WORDS = ["MR"]

# Language Rules
grammar_rules = {"VB": ["NNP"],
                 "NNP": ["NNP", "VBZ", "JJ", "VB"],
                 "CC": ["RB", "JJ"],
                 "RB": ["VBZ", "NNS"],
                 "VBZ": ["IN"],
                 "VBG": ["DT", "NN", "IN"],
                 "JJ": ["CC", "NN"],
                 "PRP": ["VBD", "VBZ"],
                 "VBD": ["JJ"],
                 "TO": ["DT"],
                 "DT": ["VBG", "NN", "JJ"],
                 "IN": ["NN", "DT"],
                 "NNS": ["VBP", "VBD"],
                 "VBP": ["DT"],
                 "PRP$": ["JJ", "NNS"],
                 "NN": ["VBZ", "NN", "NNS"]
                 }
starting_pos = ["VB", "VBG", "PRP", "RB", "DT", "NN"]