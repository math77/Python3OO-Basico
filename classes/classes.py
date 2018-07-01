class Dog:

	#Class Attribute
	specie = 'mammal'

	def __init__(self, name, age):
		self.name = name
		self.age = age

	#metodo de instancia
	def description(self):
		return "{} is {} years old".format(self.name, self.age)

	#metodo de instancia	
	def speak(self, sound):
		return "{} says {}".format(self.name, sound)


class RussellTerrier(Dog):
	def run(self, speed):
		return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
	def run (self, speed):
		return "{} runs {}".format(self.name, speed)