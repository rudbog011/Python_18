def print_query(question, answer):
    count_right_answer = 0
    for i in range(len(question)):
        print('№', i + 1, ') ', question[i], sep='')
        user_answer = int(input())
        right_answer = answer[i]
        if user_answer == right_answer:
            count_right_answer += 1
    return count_right_answer

def My_Tester():
    print('Добрый день. Введите своё имя:')
    name_user = input()
    question = [
        'Сколько будет два плюс два умноженное на два?',
        'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?',
        'На двух руках 10 пальцев. Сколько пальцев на 5 руках?',
        'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
        'Пять свечей горело, две потухло. Сколько свечей осталось?'
    ]
    answer = [6, 9, 25, 60, 2]
    result = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']
    
    count_right_answer = print_query(question, answer)
    
    print(name_user, ', Ваш результат: ', result[count_right_answer], sep='')
    
    print('Хотите пройти My-Tester заново? (Да/Нет)')
    answer_user = input()
    
    if answer_user == 'Да':
        My_Tester()
    else:
        print('До новых встреч!')
My_Tester()