from node import Node
from street_problem import *

root_node = Node(ANDRIA, None, None, 0)
node1 = Node(CORATO, GO_TO_CORATO, root_node, 5)
node2 = Node(RUVO, GO_TO_RUVO, node1, 10)

path = []
node = node2
while True:
    if node is None:
        break
    path.append(node._action)
    node = node._parent

print(path)
# with [:-1] we remove the last element of the list, which is None, and with [::-1] we reverse the list
path = path[:-1][::-1]
print(path)

