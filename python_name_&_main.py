# what is __name__ & __main__ in python and why we need it

# what is the benefit of __name__ and __main__ when importing

# They are part of python execution/interpreter engine and set these variables before running any other code within a file/function/method

# Let's dive straight in as it's the easiest way to understand what is actually going on

# To see full functionality of __name__ and __main__ we will create 2 python files
# mod_1 and mod_2
#print(__name__)
# The output is __main__... why?
# when python runs a file it sets some variables in the background one of which is __name__ variable and this instance it is set to __main__

print("This is mode_1 ->" + __name__)