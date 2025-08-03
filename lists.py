#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
def filter_odd_length_words(words):
    return [word for word in words if len(word) % 2 != 0]
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "fig", "grape"]
    odd_length_words = filter_odd_length_words(words)
    print(f"Words with an odd number of characters: {odd_length_words}")