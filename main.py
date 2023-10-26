def encoder(pw):
    encoded_pw = ""
    for digit in pw:
        encoded_pw += str(int(digit) + 3)
    return encoded_pw


def main():
    choice = ""
    while choice != "3":
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        password_data = ""
        if choice == "1":
            password = input("Please enter your password to encode: ")
            try: 
                password_data = encoder(password)
            except:
                print("Invalid password, must be numbers only")
            finally:
                print("Your password has been encoded and stored!")
        elif choice == "2":
            try:
                print(f"The encoded password is {password_data}, and the original password is {password}") # needs decoder function to be implemented
            except:
                print("Invalid input, must be numbers only")

if __name__ == "__main__":
    main()