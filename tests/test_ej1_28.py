import pytest
from scr.p1_7.ej1_28 import main

@pytest.mark.parametrize(
    "input1, input2",
    [
    (1,1),
    (0,0),
    (100,100),
    (-15,-15),
    (-3,-3),
    (9,9)
    ]
)

def test_main_iguales(input1, input2):
    main()
    assert input1 == input2
def test_main_diferentes(input1, input2):
    main()
    assert input1 != input2
    assert abs(input1 - input2) > 0 