# # # we will look at methods in python
# # # python Magic
# # # understanding private and getters and setters
# #
# # # Let's dive into Pythonic magic
# #
# # class Method_examples:
# #     this_can_be_accessed_easily = "Hey, here I am easily found"
# #
# # method = Method_examples()
# # print(method.this_can_be_accessed_easily)
# #
# # # Let's make a change to our variable
# # method.this_can_be_accessed_easily = "I have changed"
# # print(method.this_can_be_accessed_easily)
#
# # The pythonic magic saves us a lot of time but this relates to a class variable and is accessible everywhere as we know
# # # Let's move onto the __init__ method as we should use for created data with our objects
# #
# # class Method_init_example:
# #     def __init__(self):
# #         self.this_can_be_accessed_easily = "Hey, here I am easily found"
# #
# # method_init = Method_init_example()
# # print(method_init.this_can_be_accessed_easily)
# #
# # method_init.this_can_be_accessed_easily = "I have changed "
# # print(method_init.this_can_be_accessed_easily)
# #
# # # again nothing should change here but if python didn't deliver all the above magic
#
# # 3rd iteration
# class Method_example:
#     def __init__(self):
#         self.this_can_be_accessed_easily = "Hey here I am "
#
#     # getter method
#     def get_this_can_be_accssed_easily(self):
#         return self.this_can_be_accessed_easily
#
#     # setter method
#     def set_this_can_be_accessed_easily(self, value_to_be_set):
#         self.this_can_be_accessed_easily = value_to_be_set
#
#
# method_getter_setter = Method_example()
#
# print(method_getter_setter.get_this_can_be_accssed_easily())
#
# method_getter_setter.set_this_can_be_accessed_easily("I have changed")
# print(method_getter_setter.get_this_can_be_accssed_easily())
#
# 4th iteration
# Let's take our previous code and add _ to our variable in self:
class Method_example:
    def __init__(self):
        # here we will add self._this_can_be_accessed_easily and run
        self._this_can_be_accessed_easily = "Hey here I am "

    # getter method
    def get_this_can_be_accssed_easily(self):
        # Let'd add _ here as well
        return self._this_can_be_accessed_easily

    # setter method
    def set_this_can_be_accessed_easily(self, value_to_be_set):
        # Let'd add _ here as well
        self._this_can_be_accessed_easily = value_to_be_set
# by adding an _ with our variables we are telling python to essentially, not generate the getter & setters automatically


method_getter_setter = Method_example()

print(method_getter_setter.get_this_can_be_accssed_easily())

method_getter_setter.set_this_can_be_accessed_easily("I have changed")
print(method_getter_setter.get_this_can_be_accssed_easily())
#The same can be done for our methods and we'll do that in our 5th iterations


# 5th iteration
# we will do the same with our methods now but will add double __ :
