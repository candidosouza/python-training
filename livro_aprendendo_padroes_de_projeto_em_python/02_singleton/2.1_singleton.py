# -*- coding: utf-8 -*-
# criacional,oo
# python2
# python3

class Singleton(object):

	# __new__ método especial de python para instanciar objetos
	def __new__(cls, *args, **kwargs):
		# hasattr método especial do python para saber se o objeto tem determinada propriedade
		if not hasattr(cls, '__instance'):
			cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

		return cls.__instance

s = Singleton()
print("Object created ", s)

# Se a instancia já existir é usado o mesmo objeto anteriormente criado
s1 = Singleton()
print("Object created ", s1)
