from tools import *
import pytest


@pytest.mark.parametrize('x_deg', [0, 30, 45, 60, 90])
def test_sindeg(x_deg):
    f = sindeg(x_deg)
    assert(np.abs(f) <= 1), \
        'sindeg should be bounded between -1 and 1'
