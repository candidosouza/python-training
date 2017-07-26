# -*- coding: utf-8 -*-
# python3

# iterar por algum motivo sem usar for


# with open('/etc/passwd') as f:
# 	try:
# 		while True:
# 			line = next(f)
# 			print(line, end='')
# 	except StopIteration:
# 		pass

# with open('/etc/passwd') as f:
# 	while True:
# 		line = next(f, None)
# 		if line is None:
# 			break
# 		print(line, end='')

# ex:
# items = [1, 2, 3, 4]
#obtem o iterador
# it = iter(items)	# chama items.__iter__()
#executa o iterador
# next(it)			# chama items.__next__()


items = [1, 2, 3, 4]
it = iter(items)
try:
	while True:
		line = next(it)
		print(line, end='')
except StopIteration:
	pass

