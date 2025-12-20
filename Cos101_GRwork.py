print("a. Hausa")
print("b. Igbo")
print("c. Yoruba")
print("d. fulani")
choice = input("What language do you want to translate to? (a, b, c): ")

# Hausa dictionary
hausa_dictionary = {
    "hello": "sannu",
    "good morning": "ina kwana",
    "how are you": "yaya kake",
    "thank you": "nagode",
    "goodbye": "sai an jima",
    "child": "yaro",
    "friend": "aboki",
    "love": "so",
    "peace": "zaman lafiya",
    "food": "abinci",
    "water": "ruwa",
    "house": "gida",
    "family": "iyali",
    "school": "makaranta",
    "book": "littafi",
    "car": "mota",
    "money": "kudi",
    "work": "aiki",
    "happy": "farin ciki",
    "sad": "bakin ciki",
    "laugh": "dariya"
}

if choice == "a":
    print("\nWelcome to the Hausa translation program")
    print("Type an English word to translate to Hausa")
    print("Type 'exit' to quit\n")

    while True:
        word = input("Enter an English word: ").lower()

        if word == "exit":
            print("Goodbye! Sai an jima")
            break

        if word in hausa_dictionary:
            print("The Hausa translation is:", hausa_dictionary[word])
            break
        else:
            print("Sorry, the word is not in the dictionary.")

else:
    print("Sorry, only Hausa translation is available for now.")
    # Simple English to Igbo Dictionary

igbo_dictionary = {
    "hello": "ndewo",
    "food": "nri",
    "water": "mmiri",
    "house": "ulo",
    "child": "nwa",
    "man": "nwoke",
    "woman": "nwanyi",
    "love": "ihunanya",
    "come": "bia",
    "go": "gaa",
    "good": "oma",
    "bad": "ojoo",
    "sun": "anyanwu",
    "rain": "mmiri ozuzo",
    "school": "ulo akwukwo",
    "book": "akwukwo",
    "money": "ego",
    "friend": "enyi",
    "mother": "nne",
    "father": "nna"
}

print("Welcome to the English → Igbo Dictionary")
print("Type an English word to translate it into Igbo.")
print("Type 'exit' to quit.\n")

while True:
    word = input("Enter an English word: ").lower()

    if word == "exit":
        print("Goodbye! Ka omesia.")
        break

    if word in igbo_dictionary:
        print(f"Igbo translation: {igbo_dictionary[word]}\n")
    else:
        print("Sorry, that word is not in the dictionary.\n")

