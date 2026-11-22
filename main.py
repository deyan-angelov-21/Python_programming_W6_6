LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def askRows() -> str:
    rows = []
    while True:
        row = input("Insert row(empty stops):")
        if row == "":
            break
        rows.append(row)
    return "\n".join(rows)

def shiftCharacter(Character: str, Alphabet: str, Shift: int = 13) -> str:
    if Character in Alphabet:
        Index = Alphabet.index(Character)
        shifted_index = (Index + Shift) % len(Alphabet)
        return Alphabet[shifted_index]
    return Character

def rot13(Content: str) -> str:
    NewContent = ""
    Shift = 13
    for Character in Content:
        if Character in LOWER_ALPHABETS:
            NewContent += shiftCharacter(Character, LOWER_ALPHABETS, Shift)
        elif Character in UPPER_ALPHABETS:
            NewContent += shiftCharacter(Character, UPPER_ALPHABETS, Shift)
        else:
            NewContent += Character
    return NewContent

def writeFile(Filename: str, Content: str) -> None:
    with open(Filename, "w", encoding="UTF-8") as file:
        file.write(Content)

def main() -> None:
    print("Program starting.")
    print("Collecting plain text rows for ciphering.")
    Rows = askRows()
    CipheredText = rot13(Rows)
    print("#### Ciphered text ####")
    print(CipheredText)
    print("#### Ciphered text ####")
    Filename = input("Insert filename to save: ")
    writeFile(Filename, CipheredText)
    print("Ciphered text saved!")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
