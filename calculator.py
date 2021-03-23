"""Функция позволяющая проверять численные преобразования из строки.
       Args: symbol - строковое представление введенного числа.
       Return: success - Являлся ли символ числом.
               symbol - Символ преобразованный в число."""
def checker(data):
    if isinstance(data, str):
        try:
            return {'success': True,'symbol': int(data)}
        except:
            return {'success': False, 'error':'Знак не является числом, '}
    elif isinstance(data, list):
        try:
            if data[0] in ('+','-','*','/','**',):
                return {'success': True,'symbol': [data[0], int(data[1])]}
            else:
                return {'success': False, 'error': 'Действие не определено, '}
        except:
            return {'success': False, 'error': 'Несоответствие стилю написания [знак число], '}

def calculate(result, sign, digit):
    if sign == '+':
        return result + digit
    elif sign == '-':
        return result - digit
    elif sign == '*':
        return result * digit
    elif sign == '/':
        return result / digit
    elif sign == '**':
        return result ** digit


result = 0 # 0
enter = input()
result_enter = checker(enter)
while not result_enter.get('success'):
    enter = input('{}попробуйте еще раз: '.format(result_enter.get('error')))
    result_enter = checker(enter)
else: 
    result = result_enter.get('symbol')
while(1):
    enter = input().split(' ')
    if enter[0] == '=':
        break
    result_enter = checker(enter)
    while not result_enter.get('success'):
        enter = input('{}попробуйте еще раз: '.format(result_enter.get('error'))).split(' ')
        result_enter = checker(enter)
    result = calculate(result, result_enter.get('symbol')[0], result_enter.get('symbol')[1])
print('Ваш результат: {}'.format(result))
