# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

chetv = int(input('введите номер четверти (от 1 до 4): '))

if chetv == 1: 
    print('X > 0 and Y > 0')
elif chetv == 2:
    print('X > 0 and Y < 0')
elif chetv == 3:
    print('X < 0 and Y < 0')
elif chetv == 4:
    print('X < 0 and Y > 0')