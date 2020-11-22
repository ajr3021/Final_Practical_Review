
from node_stack import *


def alliteration(string):
    words = string.split()
    letter = words[0][0].lower()
    letter_count = 0
    
    for word in words:
        if word[0].lower() == letter:
            letter_count += 1
    
    return (letter_count / len(words)) >= .5


def pokemon_output(filename, generation_number):
    try:
        with open(filename) as the_file:
            with open("output.txt", 'w') as output:
                next(the_file)
                counter = 0
                GENERATION_INDEX = 11
                for line in the_file:
                    tokens = line.strip().split(',')
                    if int(tokens[GENERATION_INDEX]) == generation_number:
                        counter += 1
                        output.write(line)
    except FileNotFoundError:
        return 'FileNotFound'
    return counter


def find_pokemon_name(filename, number):
    try:
        with open(filename) as the_file:
            next(the_file)
            NUMBER_INDEX = 0
            NAME_INDEX = 1
            for line in the_file:
                tokens = line.strip().split(',')
                if int(tokens[NUMBER_INDEX]) == number:
                    return tokens[NAME_INDEX]
    except FileNotFoundError:
        return 'FileNotFound'

def find_primes(limit):
    primes_list = []
    for i in range(2, limit):
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(i)
    return primes_list


def letter_count(filename):
    try:
        with open(filename) as the_file:
            letter_list = [0 for _ in range(26)]
            for line in the_file:
                word_list = line.strip().split()
                for word in word_list:
                    for letter in word:
                        if ord(letter) >= 97 and ord(letter) <= 122:
                            letter_list[ord(letter) - ord('a')] += 1
            return letter_list
    except FileNotFoundError:
        print("The file was not found")



def reverse_string_recursive(string):
    if string == '':
        return ''
    else:
        return string[-1] + reverse_string_recursive(string[:-1])


def gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 == num2:
        return num1
    elif num1 > num2:
        return gcd(num1 - num2, num2)
    return gcd(num1, num2 - num1)

def test_add(capsys, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n2\n"))
    expected = 3
    actual = add()
    captured = capsys.readouterr()
    assert expected == actual
    assert captured.out == "Enter first number: Enter second number: "


def subset(set1, set2):
    for value in set1:
        if not value in set2:
            return False
    return True


def alphabetical_length(filename):
    try:
        with open(filename) as the_file:
            word_dict = dict()
            for line in the_file:
                words = line.strip().split()
                for word in words:
                    length = len(word)
                    if length in word_dict:
                        if word.lower() > word_dict[length].lower():
                            word_dict[length] = word
                    else:
                         word_dict[length] = word
            return word_dict
    except FileNotFoundError:
        print("Could not find the file")


class Question:
    __slots__ = ['__type', '__options', '__answer']

    def __init__(self, type, options, answer):
        self.__type = type
        self.__options = options
        self.__answer = answer
    
    def choose_answer(self):
        answer = input("Enter a letter: ")
        return answer.lower() == self.__answer.get_letter()

    def __str__(self):
        for option in self.__options:
            print(option)

class Option:
    __slots__ = ['__letter', '__text']

    def __init__(self, letter, text):
        self.__letter = letter.lower()
        self.__text = text

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__letter == other.__letter and self.__text == other.__letter

    def __str__(self):
        return f'{self.__letter}: {self.__text}'


    def get_letter(self):
        return self.__letter

    def get_text(self):
        return self.__text


def validate_parenthesis(string):
    stack = Stack()
    for char in string:
        if char == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()
        elif char == '(':
            stack.push(char)
    return stack.is_empty()