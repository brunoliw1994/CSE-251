'''
Time Guesstimate to complete:
Proficient with all the "Know how to" statements:                       1 hour
Familiar with the "Know how to" statements, but need to review a few:   1 - 4 hours
Need to review most the "Know how to" statements:                       4 - 8 hours
Need to review/relearn all the "Know how to" statements:                8+ hours

All ASSERTS must pass. Everything in this assignment should have been learned
previously. If there are holes in your knowledge, then this is the time to 
fill them (meaning learn the concepts). Take the time to learn by reading
the provided links. There are no group "prove" assignments in this class.

Make sure to write comments above your functions, explaining in your own
words what the functions does. Your comments are your "digital signature",
showing that you both wrote the code and understand how it works.

Grading:
Not passing an assert or answering #10 and #12: 0 points (code must pass all asserts--this is only true of this first assignment)
'''

# 1) Function perform_math
# This function will perform mathematical operation ('+', '-', '*', '/', '//', '**') on two integers.
def perform_math(initial_value: int, value: int, operation: str) -> float:
    # Here, I am performing the operation based on the string provided: operation (str)
    if operation == "+":
        return initial_value + value
    elif operation == "-":
        return initial_value - value
    elif operation == "*":
        return initial_value * value
    elif operation == "/":
        return initial_value / value
    elif operation == "//":
        return initial_value // value
    elif operation == "**":
        return initial_value ** value
    # In this part, if an unknown operation is provided, the program will pop up an error message.
    else:
        raise ValueError("Unsupported operation")

# 2) Function find_word_index
# This function is responsible for finding the index of a word in the list.
def find_word_index(word_to_find: str, words: list) -> int:
    # I used the list index method to find the position of word_to_find in words
    return words.index(word_to_find)

# 3) Function get_value_from_dict_using_key
# This function is responsible for returning the value associated with the given key in a dictionary.
def get_value_from_dict_using_key(key: str, word_dict: dict) -> int:
    # It retrieves the value associated with the given key in word_dict
    return word_dict[key]

# 4) Function get_list_of_urls_from_dict
# This function returns the list of URLs associated with the given key in a dictionary.
def get_list_of_urls_from_dict(key: str, url_dict: dict) -> list:
    # It returns the value associated with key, which is a list of URLs in url_dict
    return url_dict[key]

# 5) Function find_url
# This function finds a URL in a list that contains a specific substring (name).
def find_url(urls: list, name: str) -> str:
    # It is responsible for iterating through each URL in the list and check if the name is present in the URL
    for url in urls:
        if name in url:
            return url
    # If no URL contains the name, it will return an empty string
    return ""

# 6) Function find_str_in_file
# This function will check if a given string is present in a file.
def find_str_in_file(filename: str, str_to_find: str) -> bool:
    # Here, I open the file in read mode
    with open(filename, 'r') as file:
        # This part will read all lines in the file to check if str_to_find is present
        for line in file:
            if str_to_find in line:
                return True
    # If the string is not found, it will return False
    return False

# 7) Class MyParentClass
# This class represents an object with a value, a list of values, and a name.
class MyParentClass:
    def __init__(self, value: int, values: list, name: str):
        # It initializes the class attributes value, values, and name
        self.value = value
        self.values = values
        self.name = name

    # This method returns the value in the values list at a specific index
    def get_value_using_index(self, index: int) -> int:
        return self.values[index]

# 8) Class MyChildClass
# This class extends MyParentClass and adds an additional attribute, age.
class MyChildClass(MyParentClass):
    def __init__(self, value: int, values: list, name: str, age: int):
        # Here, it will call the constructor of MyParentClass to initialize value, values, and name
        super().__init__(value, values, name)
        # Adds the new attribute age
        self.age = age

# 9) Function pass_by_reference_mutable_example
# This function appends a string to a list and returns the first element of the list.
def pass_by_reference_mutable_example(lists_are_passed_by_reference_and_mutable: list, str_to_add: str) -> str:
    # It appends the string to the list, demonstrating pass-by-reference since lists are mutable
    lists_are_passed_by_reference_and_mutable.append(str_to_add)
    # It returns the first element of the list
    return lists_are_passed_by_reference_and_mutable[0]

# 10) Explanation of pass-by-reference and mutable
# Pass-by-reference: when an object is passed to a function, the function can modify the original object.
# Mutable: is the state or content of the object can be changed after it is created. Lists are mutable in Python.

# 11) Function pass_by_reference_immutable_example
# This function appends a string to another string and returns the result.
def pass_by_reference_immutable_example(strings_are_pass_by_reference_and_immutable: str, str_to_add: str) -> str:
    # Here, I made sure that this element is responsible to concatenate the original string with the new string, resulting in a new string object
    return strings_are_pass_by_reference_and_immutable + str_to_add

# 12) Explanation of immutable
# Immutable: when an object is created, its state or content cannot be changed. Strings in Python are immutable.

# 13) Instantiating an object using MyParentClass
obj = MyParentClass(1, [5, 6, 7], "3")

# 14) Instantiating an object using MyChildClass
childObj = MyChildClass(1, [5, 6, 7], "3", 10)

# The main function will run all the tests.
def main():
    assert perform_math(10, 1, "+") == 11
    assert perform_math(1, 10, "+") == 11
    assert perform_math(10, 1, "-") == 9
    assert perform_math(1, 10, "-") == -9
    assert perform_math(10, 2, "*") == 20
    assert perform_math(2, 10, "*") == 20
    assert perform_math(10, 2, "/") == 5
    assert perform_math(2, 10, "/") == 0.2
    assert perform_math(10, 3, "//") == 3
    assert perform_math(3, 10, "//") == 0
    assert perform_math(10, 3, "**") == 1000
    assert perform_math(3, 10, "**") == 59049

    assert find_word_index("a", ["a", "b", "c", "h"]) == 0
    assert find_word_index("b", ["a", "b", "c", "h"]) == 1
    assert find_word_index("c", ["a", "b", "c", "h"]) == 2
    assert find_word_index("h", ["a", "b", "c", "h"]) == 3

    word_dict = {"k1": 1, "k2": 2, "k3": 3, "k4": 10}
    assert get_value_from_dict_using_key("k1", word_dict) == 1
    assert get_value_from_dict_using_key("k2", word_dict) == 2
    assert get_value_from_dict_using_key("k3", word_dict) == 3
    assert get_value_from_dict_using_key("k4", word_dict) == 10

    movie_dict = {"people": ["http://127.0.0.1:8790/1", "http://127.0.0.1:8790/2", "http://127.0.0.1:8790/3"], "films": ["http://127.0.0.1:8790/film1", "http://127.0.0.1:8790/film2", "http://127.0.0.1:8790/film3"]}
    urls = get_list_of_urls_from_dict("films", movie_dict)
    url = find_url(urls, "film3")
    assert url != None

    assert obj.value == 1
    assert obj.values == [5, 6, 7]
    assert obj.name == "3"
    assert obj.get_value_using_index(0) == 5
    assert obj.get_value_using_index(1) == 6
    assert obj.get_value_using_index(2) == 7

    assert childObj.value == 1
    assert childObj.values == [5, 6, 7]
    assert childObj.name == "3"
    assert childObj.age == 10
    assert childObj.get_value_using_index(0) == 5
    assert childObj.get_value_using_index(1) == 6
    assert childObj.get_value_using_index(2) == 7
    assert isinstance(childObj, MyParentClass) == True

    assert find_str_in_file("data.txt", "g") == True
    assert find_str_in_file("data.txt", "1") == False

    l = ["abc", "def", "ghi"]
    pass_by_reference_mutable_example(l, "jkl")
    assert len(l) == 4
    assert l[3] == "jkl"

    s = "strings are immutable"
    new_string = pass_by_reference_immutable_example(s, " so adding to it creates a new object in memory")
    assert id(s) != id(new_string)
    assert len(new_string) != len(s)

    print("All tests passed!")

if __name__ == '__main__':
    main()
