from node import Node
from street_problem import *

root_node = Node(ANDRIA, None, None, 0)
node1 = Node(CORATO, GO_TO_CORATO, root_node, 5)
node2 = Node(RUVO, GO_TO_RUVO, node1, 10)

path = node2.path()
print(path)

prob = Problem(ANDRIA, CORATO)
exploration, result = prob.explore(path)
print('Exploration:', exploration)
if result:
    print('The is a solution!')
else:
    print('The is not a solution!')

prob = Problem(ANDRIA, RUVO)
exploration, result = prob.explore(path)
print('Exploration:', exploration)
if result:
    print('The is a solution!')
else:
    print('The is not a solution!')
