import os

def f(user_input):
    return os.popen(user_input).read()
