from classes import Dog, Bulldog, RussellTerrier

snoopy = Dog("Snoopy", 12)
bob = Dog("Bob", 5)
tody = Dog("Tody", 7)

ted = Bulldog("Ted", 3)

#Mostra que as instancias sao diferentes
print(snoopy == bob)
#Mostra o tipo do objeto d1
print(type(snoopy))

#Acessando os atributos das instancias.
print("{} is {} years old and {} is {} years old.".format(snoopy.name, snoopy.age, bob.name, bob.age))

if snoopy.specie == "mammal":
	print("{0} is {1}".format(snoopy.name, snoopy.specie))


print(snoopy.description())
print(snoopy.speak("Gruff gruff"))
print(ted.description())
print(ted.run("fast"))

#verifica se uma classe e uma instancia de outra.
print(isinstance(ted, Dog))
print(isinstance(snoopy, Bulldog))
print(isinstance(ted, RussellTerrier))