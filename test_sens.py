import sens
import numpy as np
import pytest


def approx_eq(a, b, prec=1e-6):
    return np.all(np.abs(a - b) < prec)


def test_sensitivities():
    def ab(x):
        return x[0]**2 / x[1]**3

    assert approx_eq(
        sens.sensitivities(func=ab, inputs=[10, 10], relative=True),
        np.array([2, -3]))

    assert approx_eq(
        sens.sensitivities(func=ab, inputs=[10, 10], relative=False),
        np.array([0.02, -0.03]))
