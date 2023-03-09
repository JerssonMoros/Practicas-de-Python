#! This is a calculator in python
def addition(num1, num2):
    total = num1 + num2
    print(f'The adition of {num1} and {num2} is: {total}')

def subtraction(num1, num2):
    total = num1 - num2
    print(f'The subtraction of {num1} and {num2} is: {total}')

def multiplication(num1, num2):
    total = num1 * num2
    print(f'The multuplication of {num1} and {num2} is: {total}')

def division(num1, num2):
    try:
        total = num1 // num2
        cociente = num1 % num2
        print(f'The division of {num1} and {num2} is: {total} y sobran ')
    except:
        print('Hay un error con ')
def main():
    operator = input('Please, type the operation to perform: ')
    print(operator.upper())
    
    try:
        number1 = int(input('Please, type the firts number: '))
        number2 = int(input('Please, type the second number: '))
    except:
        print('Error, no se digito un numero')
        exit()
    if operator.lower() == 'suma':
        addition(number1, number2)
    if operator.lower() == 'resta':
        subtraction(number1, number2)
    if operator.lower() == 'multiplicacion':
        multiplication(number1, number2)
    if operator.lower() == 'division':
        division(number1, number2)


if __name__ == '__main__':
    main()