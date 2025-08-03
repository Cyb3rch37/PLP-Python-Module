#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
def get_integer_set(prompt):
    integer_set = set()
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            integer_set.add(number)
        except ValueError:
            print("Please enter a valid integer.")
    
    return integer_set
def common_elements(set1, set2):
    return set1.intersection(set2)
if __name__ == "__main__":
    print("Enter integers for the first set (type 'done' to finish):")
    set1 = get_integer_set("Enter an integer: ")
    
    print("Enter integers for the second set (type 'done' to finish):")
    set2 = get_integer_set("Enter an integer: ")
    
    common_set = common_elements(set1, set2)
    print(f"The common elements in both sets are: {common_set}")