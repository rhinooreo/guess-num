import random

rnum = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = int(input('1~100 猜個數字： '))
	if num == rnum:
		print('您猜對了！')
		print('這是您猜的第', count, '次')
		break
	elif num > rnum:
		print('您猜得數字比答案大！')
	elif num < rnum:
		print('您猜的數字比答案小！')
	print('這是您猜的第', count, '次')