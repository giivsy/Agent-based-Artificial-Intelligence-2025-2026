from node import Node
from problem import *
import random

ACTION_COST = 1

prob = Problem(ANDRIA, BARI)
root_node = Node(ANDRIA, None, None, 0)

node = root_node
for _ in range(5):
    action = random.choice(prob.actions(node._state))
    new_state = prob.result(node._state, action)
    node = Node(new_state, action, node, node._cost + ACTION_COST)

path = node.path()
print(path)

exploration, result = prob.explore(path)
if result:
    print('Solution found!')

for step_type, step in exploration:
    if step_type == 'S':
        print(f'|{step}|', end='')
    elif step_type == 'A':
        print(f'--{step}-->', end='')
