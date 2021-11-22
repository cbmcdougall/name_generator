alphabet = "abcdefghijklmnopqrstuvwxyz"
months = [
    "january", "february", "march", 
    "april", "may", "june", 
    "july", "august", "september", 
    "october", "november", "december"
]
first_names = [
    "Waddles", "Snowball", "Icy", 
    "Arctic", "Frosty", "Snowy", 
    "Hoppy", "Feathers", "Fuzzy", 
    "Blizzy", "Puffy", "Fuzzbutt", 
    "Beaker", "Buddy", "Bluesy", 
    "Hopkins", "King", "Fluffers", 
    "Honky", "Duke", "Roly", 
    "Pop Pop", "Waddlebutt", "Snowface", 
    "Fishbeak", "Flappy"
]
last_names = [
    "Fluffpants", "MC Waddle", "Winterton", 
    "Kipperley", "Frostbuns", "O'Macaroni", 
    "Hopperton", "Fluffball", "Von Flump", 
    "Hopsalot", "Fishbuns", "Fuzztum"
]

def get_penguin_name(name, birth_month):
    try:
        first = first_names[alphabet.find(name[0])]
        last = last_names[months.index(birth_month)]
        penguin_name = first + " " + last
        return penguin_name
    except:
        print("\nWhoops! Error in generating penguin name\n")