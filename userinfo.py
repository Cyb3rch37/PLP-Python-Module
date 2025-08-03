#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
def get_user_info():
    user_info = {}
    user_info['name'] = input("Enter your name: ")
    user_info['age'] = input("Enter your age: ")
    user_info['favorite_color'] = input("Enter your favorite color: ")
    
    return user_info
def print_user_info(user_info):
    print("\nUser Information:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")
def main():
    user_info = get_user_info()
    print_user_info(user_info)
if __name__ == "__main__":
    main()