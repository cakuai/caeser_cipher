import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo.logo)


def caeser(direction, text, shift):
    final_text = ""
    if direction == "encode":
        for letter in text:
            if letter not in alphabet:
                final_text += letter
            else:
                position = alphabet.index(letter)
                new_pos = position+shift
                if new_pos > 25:
                    new_pos -= 26
                final_text += alphabet[new_pos]
        print(f"The encoded text is {final_text}")

    elif direction == "decode":
        for letter in text:
            if letter not in alphabet:
                final_text += letter
            else:
                position = alphabet.index(letter)
                new_pos = position-shift
                final_text += alphabet[new_pos]
        print(f"The decoded text is {final_text}")


end_of_trial = False
while not end_of_trial:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caeser(direction, text, shift)
    end = input("Do you want to give another try? please enter Y or N\n").lower()
    if end == "y":
        continue
    else:
        print("Thank you for trying.")
        end_of_trial = True
