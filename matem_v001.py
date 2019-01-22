import random
import os
import datetime

#print('Привет! Как тебя зовут?')
name = input('Привет! Как тебя зовут? ')
print('\nПривет ' + name +'! Давай позанимаемся математикой.')
gotov = input('\nГотов?! (да/нет): ')
while gotov == 'да':
	d = 0
	rezult = 0
	x = 0
	col = 3
	y = 0
	z = 0
	for i in range(col):
		znak = [1, 2, 1, 2, 2, 1, 1, 2]
		for y in znak:
			if y == 1:
				now = datetime.datetime.now()
				now1 = now
				a = random.randint(0, 25)
				b = random.randint(0, 25)
				z += 1
				c = a + b
				while x != c:
					print(a,'+',b,'= ', end ='')
					x = int(input())
					if x == c:
						print('Верно, молодец!\n')
					else:
						print('Ошибка!!! Попробуй еще раз!')
						d += 1
		
			if y == 2:
				now = datetime.datetime.now()
				now1 = now
				a = random.randint(0, 25)
				b = random.randint(0, 25)
				z += 1
				if a < b:
					a,b = b,a
				c = a - b
				while x != c:
					print(a,'-',b,'= ', end ='')
					x = int(input())
					if x == c:
						print('Верно, молодец!\n')
					else:
						print('Ошибка!!! Попробуй еще раз!')
						d += 1  

	if d == 0:
		rezult = 5
	elif d == 1:
		rezult = 4
	elif d == 2:
		rezult = 3
	else:
		rezult = 2

	print()
	print(name+', ты решил', z,'заданий.')
	print('Количество допущенных ошибок:', d)
	print('Твоя оценка:', rezult)
	if rezult == 5:
		print('МОЛОДЕЦ!!! Можешь 5 минут отдохнуть!')
	else:
		print('Следующий раз будь внимательней!')   
	print('')

	new_line = str(rezult)
	col_str = str(z)
	now = datetime.datetime.now()
	f = open('journal', 'a')
	f.write((now1.strftime("%d-%m-%Y %H:%M ")) + '-> ' + (now.strftime("%H:%M ")) + name + '; Оценка: ' + new_line + '.\n')
	f.close

	gotov = input('Еще порешаем?! (да/нет): ')  

		
input("\nНажми Enter для выхода из программы!")