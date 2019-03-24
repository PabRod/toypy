import numpy as np


def sindeg(x_deg):
    """Sine function for argument in degrees.
    """
    x_rad = x_deg * np.pi / 180
    return np.sin(x_rad)
