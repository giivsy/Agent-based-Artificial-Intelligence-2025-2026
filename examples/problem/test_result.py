from street_problem import *

def test_result():
    problem = Problem(ANDRIA, CORATO)
    state = CORATO
    actions = problem.actions(state)
    for action in actions:
        print(action, ' -> ', problem.result(state, action))
    print('Test passed!')

test_result()