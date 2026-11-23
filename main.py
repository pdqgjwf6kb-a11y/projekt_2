import random

def generuj_tajne_cislo() -> str:
    """Generuje náhodné 4-místné číslo, kde první číslice je od 1 do 9 a ostatní jsou od 0 do 9. Všechny číslice jsou unikátní."""
    while True:
        random_digit_1 = str(random.randint(1, 9))
        random_digit_2 = str(random.randint(0, 9))
        random_digit_3 = str(random.randint(0, 9))
        random_digit_4 = str(random.randint(0, 9))

        if (
            random_digit_1 != random_digit_2
            and random_digit_1 != random_digit_3
            and random_digit_1 != random_digit_4
            and random_digit_2 != random_digit_3
            and random_digit_2 != random_digit_4
            and random_digit_3 != random_digit_4):

            random_number = random_digit_1 + random_digit_2 + random_digit_3 + random_digit_4
            return random_number

def porovnej_cisla(random_number: str, input_number: str) -> tuple:
    """Porovnává tajné číslo s číslem zadaným uživatelem a vrací počet bulls a cows."""
    bulls = 0
    cows = 0

    for i in range(4):
        if input_number[i] == random_number[i]:
            bulls += 1
        elif input_number[i] in random_number:
            cows += 1

    return bulls, cows

def zkontroluj_vstup(input_number: str) -> str:
    """Kontroluje, zda je vstupní číslo platné (4-místné, unikátní číslice, první číslice není 0)."""
    if len(input_number) != 4:
        return "Neplatný vstup. Zadejte 4-místné číslo."
    if not input_number.isdigit():
        return "Neplatný vstup. Zadejte pouze číslice."
    if input_number[0] == '0':
        return "Neplatný vstup. První číslice nesmí být 0."
    if len(set(input_number)) != 4:
        return "Neplatný vstup. Číslice musí být unikátní."
    return ""

def main():
    """Hlavní funkce hry."""
    print("Hi there!\n"
    "-----------------------------------------------\n"
    "I've generated a random 4 digit number for you.\n"
    "Let's play a bulls and cows game.\n"
    "-----------------------------------------------\n"
    "Enter a number:\n"
    "-----------------------------------------------")
    random_number = generuj_tajne_cislo()

    while True:
        input_number = input("Zadejte číslo: ")

        error_message = zkontroluj_vstup(input_number)

        if error_message:
            print(error_message)
            continue

        bulls, cows = porovnej_cisla(random_number, input_number)

        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"

        print(f"{bulls} {bull_text}, {cows} {cow_text}")

        if bulls == 4:
            print("Gratulujeme! Uhodli jste číslo!")
            break
        
if __name__ == "__main__":
    main()


