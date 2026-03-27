from street_problem import *

class Node:

    def __init__(self, state, action, parent, path_cost):
        self.state = state
        self.action = action
        self.parent = parent
        self.cost = path_cost

    def __repr__(self):
        return f"([NODE] State: {self.state}, Action: {self.action}, Parent: {self.parent._state}, Cost: {self.cost})"

    def path(self):
        if self.parent is None:
            return []
        parent_path = self.parent.path()
        parent_path.append(self.action)
        return parent_path

