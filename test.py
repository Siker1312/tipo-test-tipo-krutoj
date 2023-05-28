def find_duplicate_numbers(numbers):
    number_count = {}
    duplicates = []

    for number in numbers:
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1

    for number, count in number_count.items():
        if count > 1:
            duplicates.append(number)

    return ' '.join(str(number) for number in duplicates)

input_numbers = input("Введите список чисел: ").split()

result = find_duplicate_numbers(input_numbers)
print("Числа, которые встречаются более одного раза:", result)