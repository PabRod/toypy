from tools import *
import pytest


# @pytest.mark.parametrize('x_deg', [0, 30, 45, 60, 90])

@pytest.mark.parametrize("input, exp_output", [
    (0, 0),
    (30, 1/2),
    (45, np.sqrt(2)/2),
    (60, np.sqrt(3)/2),
    (90, 1),
    (180, 0),
    (270, -1)
])
def test_sindeg(input, exp_output):
    tol = 1e-6
    f = sindeg(input)
    assert(f == pytest.approx(exp_output, tol)), \
        'sindeg is not behaving as expected'
