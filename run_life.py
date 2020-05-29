# import classes and initilise objects and run methods

from dog_class import *
# import classes here and intialize objs and run methods
# this speration will maintain you code more organized following speration of concerns

from dog_class import *

# Initialize a Dog object -
max_dog_instance = Dog()
ringo_dog_instance = Dog('Ringo')

print(max_dog_instance)

print(max_dog_instance.name)
print(ringo_dog_instance.name)

# # Call the method .bark() on object
#
# print(max_dog_instance.eat('BONE'))
# print(max_dog_instance.bark())
# print(max_dog_instance.fetch())
# print(max_dog_instance.potty())
# print(max_dog_instance.bark())
# print(max_dog_instance.sleep())
#
# print('walk the dog home')
#
# print(max_dog_instance.sleep())
# print(max_dog_instance.sleep())
# print(max_dog_instance.bark("Creepy Stranger!!"))