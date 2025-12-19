igala = {
    'hello': 'aloo',
    'food': 'onyi',
    'water': 'omi',
    'thank you': 'oche',
    'school': 'sukulu',
    'book': 'buku',
    'love': 'ohuma',
    'friend': 'omako',
    'family': 'ogijo',
    'money': 'owo',
    'car': 'moto',
    'road': 'ogba',
    'city': 'otu',
    'work': 'ogba',
    'time': 'ojo',
    'day': 'ojo',
    'night': 'odu',
    'sun': 'ene',
    'moon': 'ole',
    'child': 'oma'
}

def translate_to_igala():
    word = input('Enter an English word: ').lower()
    if word in igala:
        print(f"Igala: {igala[word]}")
    else:
        print("The word is not in the dictionary. Try another.")

def main():
    print("Language Translator")
    print("1. Igala")
    print("2. Exit")
    while True:
        choice = input('Choose an option: ')
        if choice == '1':
            translate_to_igala()
        elif choice == '2':
            print("Oche!")
            break
        else:
            print('Invalid option')

if __name__ == "__main__":
    main()