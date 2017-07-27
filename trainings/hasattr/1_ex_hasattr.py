# -*- coding: utf-8 -*-

class Foo(object):

	bar = 'Bar'

	def test():
		pass



# para atributo
print(hasattr(Foo, 'bar'))
# para método
print(hasattr(Foo, 'teste'))


#ex usage:

class UserController:
  
	def handle(self,action):
		if hasattr(self, action):
			getattr(self, action)()
		else:
			print 'Metodo inexistente'

	def login(self):
		print 'Executou o método login()'

	def edit(self):
		print 'Executou o método edit()'

controller = UserController()
controller.handle('login')
controller.handle('teste')