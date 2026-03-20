CORATO = 'Corato'
RUVO = 'Ruvo'
TRANI = 'Trani'
MOLFETTA = 'Molfetta'
ANDRIA = 'Andria'
BARLETTA = 'Barletta'
MINERVINO = 'Minervino'
ALTAMURA = 'Altamura'
BISCEGLIE = 'Bisceglie'
MODUGNO = 'Modugno'
BARI = 'Bari'

GO_TO_CORATO = 'GoToCorato'
GO_TO_RUVO = 'GoToRuvo'
GO_TO_TRANI = 'GoToTrani'
GO_TO_MOLFETTA = 'GoToMolfetta'
GO_TO_ANDRIA = 'GoToAndria'
GO_TO_BARLETTA = 'GoToBarletta'
GO_TO_MINERVINO = 'GoToMinervino'
GO_TO_ALTAMURA = 'GoToAltamura'
GO_TO_BISCEGLIE = 'GoToBisceglie'
GO_TO_MODUGNO = 'GoToModugno'
GO_TO_BARI = 'GoToBari'

class Problem:

    def __init__(self, initial_state, goal_state):

        self._initial_state = initial_state
        self._goal_state = goal_state

        self.map = {
            CORATO: [GO_TO_TRANI, GO_TO_BISCEGLIE, GO_TO_RUVO, GO_TO_ALTAMURA, GO_TO_ANDRIA],
            BARLETTA: [GO_TO_TRANI, GO_TO_ANDRIA, GO_TO_MINERVINO],
            ANDRIA: [GO_TO_CORATO, GO_TO_BARLETTA, GO_TO_MINERVINO],
            MINERVINO: [GO_TO_BARLETTA, GO_TO_ANDRIA, GO_TO_ALTAMURA],
            TRANI: [GO_TO_CORATO, GO_TO_BISCEGLIE, GO_TO_BARLETTA],
            BISCEGLIE: [GO_TO_TRANI, GO_TO_MOLFETTA, GO_TO_CORATO],
            MOLFETTA: [GO_TO_BISCEGLIE, GO_TO_RUVO, GO_TO_MODUGNO, GO_TO_BARI],
            RUVO: [GO_TO_CORATO, GO_TO_MOLFETTA, GO_TO_MODUGNO, GO_TO_ALTAMURA],
            ALTAMURA: [GO_TO_MINERVINO, GO_TO_CORATO, GO_TO_RUVO, GO_TO_MODUGNO, GO_TO_BARI],
            MODUGNO: [GO_TO_MOLFETTA, GO_TO_RUVO, GO_TO_ALTAMURA, GO_TO_BARI],
            BARI: [GO_TO_MOLFETTA, GO_TO_MODUGNO, GO_TO_ALTAMURA]
        }

    def actions(self, state):
        return self.map[state]

    def result(self, _, action):
        if action == GO_TO_CORATO:
            return CORATO
        elif action == GO_TO_TRANI:
            return TRANI
        elif action == GO_TO_MOLFETTA:
            return MOLFETTA
        elif action == GO_TO_ANDRIA:
            return ANDRIA
        elif action == GO_TO_BARLETTA:
            return BARLETTA
        elif action == GO_TO_MINERVINO:
            return MINERVINO
        elif action == GO_TO_ALTAMURA:
            return ALTAMURA
        elif action == GO_TO_RUVO:
            return RUVO
        elif action == GO_TO_CORATO:
            return CORATO
        elif action == GO_TO_BISCEGLIE:
            return BISCEGLIE
        elif action == GO_TO_MODUGNO:
            return MODUGNO
        elif action == GO_TO_BARI:
            return BARI
        else:
            raise ValueError('Invalid action')

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
