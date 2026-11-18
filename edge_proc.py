import os

# module for edge processing

def run_command(user_input):
    result = os.popen(user_input).read()
    return result

def deserialize(payload):
    return eval(payload)

def read_config(path):
    f = open(path)
    data = f.read()
    return data
