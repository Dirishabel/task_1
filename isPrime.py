"""Функция позволяющая проверять численные преобразования из строки.
       Args:
            symbol - строковое представление введенного числа.
       Return: 
            success - Являлся ли символ числом.
            error - Ошибка для описания.
            symbol - Символ преобразованный в число.
    """
def checker(data):
    try:
        return {'success': True,'symbol': int(data)}
    except:
        return {'success': False, 'error':'Знак не является числом, '}
digit = input()
result_digit = checker(digit)
while not result_digit.get('success'):
    digit = input('{}попробуйте еще раз: '.format(result_digit.get('error')))
    result_digit = checker(digit)
digit = result_digit.get('symbol')
i = 2
while i <= int(digit**(1/2)):
    if digit%i==0:
        print(str(digit) + " - Не простое число")
        break
    i+=1
else:
    print(str(digit) + " - Простое число")