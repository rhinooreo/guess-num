import random

start = int(input('請決定隨機數字範圍開始值： '))
end = int(input('請決定隨機數字範圍結束值： '))
rnum = random.randint(start, end)
count = 0
while True:
	count += 1
	num = int(input('猜個數字： '))
	if num == rnum:
		print('您猜對了！')
		print('這是您猜的第', count, '次')
		break
	elif num > rnum:
		print('您猜得數字比答案大！')
	elif num < rnum:
		print('您猜的數字比答案小！')
	print('這是您猜的第', count, '次')