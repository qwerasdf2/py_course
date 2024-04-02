def calculate(a, b, operator):
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b
    return int(result)


def main(input: str):
    values_list = input.split(' ')
    try:
        if len(values_list) == 3:
            first_value = int(values_list[0])
            second_value = int(values_list[2])
            operator = values_list[1]
        if (first_value >= 1 and second_value >= 1) and (first_value <= 10 and second_value <= 10):
            result = calculate(a=first_value, b=second_value, operator=operator)
            print('Result:', result, '\n')
        else:
            print('Values are out of range\nRange: 1 to 10\n')
    except:
        print('Invalid format\n')


print('Enter values:')
values_str = input()
main(input=values_str)