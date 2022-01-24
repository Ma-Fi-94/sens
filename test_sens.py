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


def test_sensitivities_distributions():
    def ab(x):
        return x[0]**2 / x[1]**3

    ds = [
        lambda: np.random.normal(10, 0.01), lambda: np.random.normal(10, 0.01)
    ]

    np.random.seed(0)

    r = sens.sensitivities_distributions(func=ab,
                                         input_distribs=ds,
                                         relative=True)
    assert approx_eq(np.array([np.mean(r[0]), np.mean(r[1])]),
                     np.array([2, -3]),
                     prec=.001)

    r = sens.sensitivities_distributions(func=ab,
                                         input_distribs=ds,
                                         relative=False)
    assert approx_eq(np.array([np.mean(r[0]), np.mean(r[1])]),
                     np.array([0.02, -0.03]),
                     prec=.001)
