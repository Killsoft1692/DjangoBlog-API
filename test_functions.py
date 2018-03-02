import re


def handle_numbers(number1, number2, number3):
    out = []
    [out.append(value) for value in range(number1, number2+1) if value % number3 == 0]

    return len(out)


def handle_string(value):
    letters_count = len(re.findall(r'[a-zA-Z]', value))
    digits_count = len(re.findall(r'\d', value))

    return "Result:\n Letters: {}\n Digits: {}".format(letters_count, digits_count)


def handle_list_of_tuples(list_of_tuples):

    return sorted(list_of_tuples)


print(handle_numbers(1, 10, 2))
print(handle_string('Hello world! 123!'))
print(handle_list_of_tuples(
    [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98")
    ])
)

