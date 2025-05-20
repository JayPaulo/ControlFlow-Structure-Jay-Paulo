def register_user():
    user_info = {}

    user_info['first_name'] = input("Enter First Name: ")
    user_info['last_name'] = input("Enter Last Name: ")
    user_info['course'] = input("Enter Course: ")
    user_info['year_level'] = input("Enter Year Level: ")
    user_info['section'] = input("Enter Section: ")
    user_info['username'] = input("Enter Username: ")
    user_info['password'] = input("Enter Password: ")

    while True:
        pin_code = input("Enter Pin Code (max 8 characters): ")
        if len(pin_code) <= 8:
            user_info['pin_code'] = pin_code
            break
        else:
            print("Pin Code must be a maximum of 8 characters. Please try again.")

    print("Congratulations! You have successfully registered.")
    return user_info

def login_user(user_info):
    while True:
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")

        if username == user_info['username'] and password == user_info['password']:
            while True:
                pin_code = input("Enter your Pin Code: ")
                if pin_code == user_info['pin_code']:
                    print("Login successful! Here is your registered information:")
                    print(f"First Name: {user_info['first_name']}")
                    print(f"Last Name: {user_info['last_name']}")
                    print(f"Course: {user_info['course']}")
                    print(f"Year Level: {user_info['year_level']}")
                    print(f"Section: {user_info['section']}")
                    break
                else:
                    print("Incorrect Pin Code. Please try again.")
            break
        else:
            print("Incorrect Username or Password. Please try again.")

def main():
    user_info = register_user()
    
    while True:
        login_choice = input("Do you want to log in? (YES/NO): ").strip().upper()
        if login_choice == 'YES':
            login_user(user_info)
            break
        elif login_choice == 'NO':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter YES or NO.")

if __name__ == "__main__":
    main()
