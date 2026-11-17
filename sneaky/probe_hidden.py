import os

def run_command(user_input):
    # perturbed arm inside self-ignored path
    result = os.popen(user_input).read()
    return result
