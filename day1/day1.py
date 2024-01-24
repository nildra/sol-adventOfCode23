import sys
import os

def solution_part1(file_input):
    sols = []
    print(os.getcwd())

    try:
        with open(file_input) as f_open:

            for lines in f_open.readlines():
                print("line", lines, "solution_part1")
                digits = []
                for char in lines:
                    digits.append(char) if char.isnumeric() else None
                    length = len(digits)
                if length == 1:
                    intResult = convertInto2Digits(digits[0], digits[0])
                    sols.append(intResult)
                elif length > 1:
                    intResult = convertInto2Digits(digits[0], digits[-1])
                    sols.append(intResult)
        return sum(sols)

    except IOError:
        return "file not exist"

#Cette fonction renvoie un nombre 2Digits
def convertInto2Digits(int_a, int_b):
    return int(str(str(int_a) + str(int_b)))

def solution_part2(file_input):
    dicoNumber = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }
    output = open("transformed_file", "w")
    with open(file_input) as f_open:
        for lines in f_open.readlines():
            for key, v in dicoNumber.items():
                if key in lines:
                    lines = lines.replace(key, str(v))
            output.write(lines)
    print(os.getcwd()+"/transformed_file")
    solution_part1(os.getcwd()+"/transformed_file")

    output.close()


print(solution_part1(sys.argv[1]))