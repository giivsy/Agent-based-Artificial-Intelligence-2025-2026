from cities import *

class StreetProblem:

    def __init__(self, initial_state, goal_state):

        self._initial_state = initial_state
        self._goal_state = goal_state

        self.map = {
            CORATO: [TRANI, BISCEGLIE, RUVO, ALTAMURA, ANDRIA],
            BARLETTA: [TRANI, ANDRIA, MINERVINO],
            ANDRIA: [CORATO, BARLETTA, MINERVINO],
            MINERVINO: [BARLETTA, ANDRIA, ALTAMURA],
            TRANI: [CORATO, BISCEGLIE, BARLETTA],
            BISCEGLIE: [TRANI, MOLFETTA, CORATO],
            MOLFETTA: [BISCEGLIE, RUVO, MODUGNO, BARI],
            RUVO: [CORATO, MOLFETTA, MODUGNO, ALTAMURA],
            ALTAMURA: [MINERVINO, CORATO, RUVO, MODUGNO, BARI],
            MODUGNO: [MOLFETTA, RUVO, ALTAMURA, BARI],
            BARI: [MOLFETTA, MODUGNO, ALTAMURA]
        }

    def actions(self, state):
        return self.map[state]

    def result(self, state, action):
        for street in streets: 
            c1, c2, _ = street
            if (c1 == state and action == c2) or (c2 == state and action == c1):
                return action
        raise ValueError('Action not possible')

    def explore(self, path):
        state = self._initial_state
        evolution = [('S',state)]
        is_solution = False
        for action in path:
            evolution.append(('A',action))
            state = self.result(state, action)
            evolution.append(('S',state))
        if state == self._goal_state:
            is_solution = True
        return evolution, is_solution

    def action_cost(self, state, action):
        for street in streets: 
            c1, c2, cost = street
            if (c1 == state and action == c2) or (c2 == state and action == c1):
                return cost
        raise ValueError('Action not allowed')


prob = StreetProblem(initial_state=CORATO, goal_state=RUVO)

actions = prob.actions(CORATO)
print(actions)