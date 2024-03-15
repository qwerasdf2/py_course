def calculate(a, b, operator):
    if (a>=1 and b>=1) and (a<=10 and b<=10):
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        return int(result)
    else:
        return 'Values are out of range\nRange: 1 to 10'

def main():
    while True:
        print('Enter values:')
        values_str = input()
        if values_str.isalnum() == False:
            values_list = values_str.split(' ')
            try:
                if len(values_list) == 3:
                    result = calculate(a=int(values_list[0]), b=int(values_list[2]), operator=values_list[1])
                    print('Result:', result, '\n')
                else:
                    print('Invalid format\n')
            except:
                print('Invalid format\n')
        else:
            print('String is not handling\n')


main()