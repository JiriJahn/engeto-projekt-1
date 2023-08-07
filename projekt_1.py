"""
projekt_1.py: První projekt do Engeto Online Python Akademie
author: Jiri Jahn
email: jiri.jahn@email.cz
discord: jirkaj. 
"""
#Definice registrovanych uzivatelu#

REGISTERED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

#Definice textu pro analyzu#

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#Prihlaseni#

def login():
    username = input("username: ")
    password = input("password: ")
    return username, password

def is_registered_user(username, password):
    return username in REGISTERED_USERS and REGISTERED_USERS[username] == password

#Analyza definovaneho textu#

def analyze_text(text):
    words = text.split()
    word_lengths = [len(word.strip(".,!?")) for word in words]
    word_stats = {
        "word_count": len(words),
        "titlecase_count": sum(1 for word in words if word.istitle()),
        "uppercase_count": sum(1 for word in words if word.isupper()),
        "lowercase_count": sum(1 for word in words if word.islower()),
        "numeric_count": sum(1 for word in words if word.isdigit()),
        "numeric_sum": sum(int(word) for word in words if word.isdigit())
    }
    return word_stats, word_lengths

#Definice tabulky#

def table(word_lengths):
    length_counts = {length: word_lengths.count(length) for length in set(word_lengths)}
    sorted_counts = sorted(length_counts.items())
    print("LEN|    OCCURENCES    |NR.")
    print("----------------------------------------")
    for length, count in sorted_counts:
        print(f"{length:3d}|{'*' * count:18}|{count:2d}")

#Zobrazení výsledku#

def main():
    print("$ python projekt1.py")
    username, password = login()
    if is_registered_user(username, password):
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
    

    if username in REGISTERED_USERS and REGISTERED_USERS[username] == password:
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        print("----------------------------------------")
        try:
            selected_text_idx = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
            if 0 <= selected_text_idx < len(TEXTS):
                selected_text = TEXTS[selected_text_idx]
                word_stats, word_lengths = analyze_text(selected_text)
                print("----------------------------------------")
                print(f"There are {word_stats['word_count']} words in the selected text.")
                print(f"There are {word_stats['titlecase_count']} titlecase words.")
                print(f"There are {word_stats['uppercase_count']} uppercase words.")
                print(f"There are {word_stats['lowercase_count']} lowercase words.")
                print(f"There are {word_stats['numeric_count']} numeric strings.")
                print(f"The sum of all the numbers {word_stats['numeric_sum']}")
                print("----------------------------------------")
                table(word_lengths)
            else:
                print("Invalid selection. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
    else:
        print("Unregistered user, terminating the program..")

if __name__ == "__main__":
    main()
