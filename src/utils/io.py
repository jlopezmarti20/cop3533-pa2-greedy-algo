import os
def read_input(filename: str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, '..', '..', 'data', filename)
    with open(filepath, 'r') as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))
    return k, requests