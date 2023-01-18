import random

rnum = random.randint(1, 100)
while True:
	num = int(input('1~100 猜個數字： '))
	if num == rnum:
		print('您猜對了！')
		break
	else:
		if num > rnum:
			print('您猜得數字比答案大！')
		elif num < rnum:
			print('您猜的數字比答案小！')