exit_status = {
    'a': 0,
    'o': 0,
    'u': 0,
    'i': 0,
    'e': 0,
    'y': 0,
}
work_string = input('Введите строку: ')
for letter in work_string:
    if letter in exit_status.keys():
        exit_status[letter] +=1
for letter_exit in exit_status.keys():
    print('{0} {1}'.format(letter_exit, exit_status[letter_exit]), end=', ')