#jump7
num = range(1,101)
for i in num:
	if i%7 == 0 or i%10 == 7 or int(i/10) == 7:
		continue
	print(i) 

