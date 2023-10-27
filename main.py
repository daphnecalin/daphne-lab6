# Daphne Calin

def encoder(pw):
    encoded_pw = ""
    for digit in pw:
        encoded_pw += str(int(digit) + 3)
    return encoded_pw


# Paola Bechalani

def decoder(password):
    pw_return = ""
    value = 0
    for i in range(len(password)):
        value = int(password[i]) - 3
        pw_return += str(value)
    return pw_return


def main():
    choice = ""
    password_data = ""
    while choice != "3":
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            try:
                password_data = encoder(password)
            except:
                print("Invalid password")
            finally:
                print("Your password has been encoded and stored!")
        elif choice == "2":
            try:
                print(
                    f"The encoded password is {password_data}, and the original password is {decoder(password_data)}.")  # needs decoder function to be implemented
            except:
                print("Invalid input, must be numbers only")


if __name__ == "__main__":
    main()
