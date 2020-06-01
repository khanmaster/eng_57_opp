# # Creating a cat class
#
# class Cat:
#     animal_kind = "small Lion"  # class variable which returns an attribute of string
#
#     def cat_mew(self):
#         return "Meowwn...."
# print("This cat kind of a " + Cat.animal_kind)
# print("This cat can call " + Cat.cat_mew(" "))
# print(Cat.cat_mew(''))
# print(Cat.animal_kind)

# now let's create an object is also called " INSTANTIATION OR INSTATIATING a class"
# we will create two cats called 'kitty' and 'misty' that will inherit from our Cat class:

class Cat:
    animal_kind = "British Shorthair"

    def mew(self):
        self.animal_kind
        return 'Mew...'


# To instantiate a class it must be assigned to a variable and accessed using the class name
kitty = Cat()
misty = Cat()
# we have created two cats so let's have look at some of the details
print(type(kitty))
print(type(misty))
# kitty and misty are type of __main__.Cat

print(kitty.animal_kind)
print(misty.animal_kind)
# both the cats are same animal_kind British shorthair as they are inherited from Cat class

print(kitty.mew())
print(kitty.mew())
# and they both have the same method of mew

# it is important to understand that they are both completely distinct objects now
# making changes to one cat will not affect the other

kitty.animal_kind = "persian cat "
# we have updated the animal_kind for kitty
print("animal_kind has been changed for kitty as " + kitty.animal_kind)
print(misty.animal_kind)
# This is the benefit of instantiating objects so we can have multiple objects that can adapt and change(Polymorpic)

# so far so good right...?

# There is a DANGER of class variable in our case animal_kind
# what if we changed this


# our kitty and misty will be....
print(kitty.animal_kind)
print(misty.animal_kind)
print(kitty.mew())
print(misty.mew())

# so far we have leanred:
# how to create a class and add class objects
# class creation and Attributes
# understanding self
# Reviewing our Cat class
# The Danger of class variables

# lets move on to resolving the Danger of class variables