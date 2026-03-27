from node import Node
from street_problem import *

root_node = Node(ANDRIA, None, None, 0)
node1 = Node(CORATO, GO_TO_CORATO, root_node, 5)
node2 = Node(RUVO, GO_TO_RUVO, node1, 10)

print(node2.path())
print(node1.path())
print(root_node.path())
