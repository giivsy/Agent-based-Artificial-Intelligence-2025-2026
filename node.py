from problem import *

class Node:

    def __init__(self, state, action, parent, path_cost):
        self._state = state
        self._action = action
        self._parent = parent
        self._cost = path_cost

    def __repr__(self):
        return f"([NODE] State: {self._state}, Action: {self._action}, Parent: {self._parent._state}, Cost: {self._cost})"

    def path(self):
        if self._parent is None:
            return []
        parent_path = self._parent.path()
        parent_path.append(self._action)
        return parent_path

