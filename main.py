import random

def is_valid(number,n):
    return number >= 1 and number <= n


    
schet = 0
play = 'да'
print('Добро пожаловать в числовую угадайку')
while play.lower() == 'да':
    n = 0
    print('До какого числа игаем?')
    nnn = int(input())
    num = random.randint(1, nnn)
    while n != num:
        print('Введите число')
        n = int(input())
        if is_valid(n, nnn) is True:
            if n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                schet += 1
            elif n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                schet += 1
            else:
                print('Вы угадали, поздравляем!', 'Вы справились за', schet, 'попыток')
        else:
            print('Ошибка!')
            print('Введите число от 1 до', nnn)
    print('Хотите сыграть еще?')
    play = input()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')    