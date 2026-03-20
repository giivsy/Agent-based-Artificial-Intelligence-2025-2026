from problem import *

def test_actions():
    problem = Problem(ANDRIA, CORATO)
    assert problem.actions(ANDRIA) == [GO_TO_CORATO, GO_TO_BARLETTA, GO_TO_MINERVINO]
    assert problem.actions(BARLETTA) == [GO_TO_TRANI, GO_TO_ANDRIA, GO_TO_MINERVINO]
    assert problem.actions(MOLFETTA) == [GO_TO_BISCEGLIE, GO_TO_RUVO, GO_TO_MODUGNO, GO_TO_BARI]
    print('Test passed!')

test_actions()