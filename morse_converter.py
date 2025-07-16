from morse_dict import morse_code_dict, inverse_morse_code_dict
from morse_audio import play_morse

def text_to_morse(text):
    morse = ""
    for char in text.upper():
        if char in morse_code_dict:
            morse += morse_code_dict[char] + " "
        else:
            morse += "? "
    return morse.strip()

def morse_to_text(morse):
    text = ""
    for code in morse.strip().split(" "):
        if code in inverse_morse_code_dict:
            text += inverse_morse_code_dict[code]
        else:
            text += "?"
    return text

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    print("Welcome to Morse Code Converter")
    print("1. Text to Morse")
    print("2. Morse to Text")
    print("3. Convert file (text to morse)")
    print("4. Convert file (morse to text)")
    print("5. Play Morse audio")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text: ")
        morse = text_to_morse(text)
        print("Morse Code:", morse)
    elif choice == "2":
        morse = input("Enter morse code: ")
        text = morse_to_text(morse)
        print("Text:", text)
    elif choice == "3":
        content = read_from_file("input.txt")
        morse = text_to_morse(content)
        save_to_file(morse, "output.txt")
        print("Converted Morse saved to output.txt")
    elif choice == "4":
        content = read_from_file("input.txt")
        text = morse_to_text(content)
        save_to_file(text, "output.txt")
        print("Converted text saved to output.txt")
    elif choice == "5":
        morse = input("Enter morse code to play: ")
        play_morse(morse)
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()