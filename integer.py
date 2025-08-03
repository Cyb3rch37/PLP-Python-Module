#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
def get_integer_list():
    integer_list = []
    while True:
        user_input = input("Enter an integer (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            integer_list.append(number)
        except ValueError:
            print("Please enter a valid integer.")
    
    return integer_list
def sum_of_integers(integer_list):
    return sum(integer_list)
if __name__ == "__main__":
    integers = get_integer_list()
    total = sum_of_integers(integers)
    print(f"The sum of the integers is: {total}")