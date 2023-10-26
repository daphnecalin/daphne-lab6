def encoder(pw):
    encoded_pw = ""
    for digit in pw:
        encoded_pw += str(int(digit) + 3)
    return encoded_pw


def main():
    choice = ""
    while choice != "q":
        print("1: Encode password")
        print("2: Decode password")
        print("q: Quit")
        choice = input("Select an option: ")

        if choice == "1":
            password = input("Enter a password to encode: ")
            try: 
                print(encoder(password))
            except:
                print("Invalid password, must be numbers only")
        elif choice == "2":
            password = input("Enter a password to decode: ")
            try:
                print(decoder(password)) # needs decoder function to be implemented
            except:
                print("Invalid input, must be numbers only")
        elif choice == "q":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()