print("a. Hausa")
print("b. Igbo")
print("c. Yoruba")

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
