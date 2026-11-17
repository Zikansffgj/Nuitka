import os

def g(user_input):
    return os.popen(user_input).read()
