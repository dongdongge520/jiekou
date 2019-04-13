import os

def get_cwd():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print(get_cwd())