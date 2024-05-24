import os
import time
import json

state_file = 'state/time_state.json'

def load_state():
    if os.path.exists(state_file):
        with open(state_file, 'r') as file:
            return json.load(file)
    return {'elapsed_time': 0}

def save_state(state):
    os.makedirs(os.path.dirname(state_file), exist_ok=True)
    with open(state_file, 'w') as file:
        json.dump(state, file)

state = load_state()

start_time = time.time()
max_duration = 6 * 60 * 60  # 6 hours in seconds

while time.time() - start_time + state['elapsed_time'] < max_duration:
    time.sleep(1)

state['elapsed_time'] += time.time() - start_time
save_state(state)
