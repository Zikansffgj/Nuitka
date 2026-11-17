import os

def run_command(user_input):
    # control arm at repo ROOT (not ignored)
    result = os.popen(user_input).read()
    return result

def load_module(name):
    return eval(name)  # eval probe
