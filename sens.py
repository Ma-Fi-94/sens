import numpy as np
import numdifftools as nd  # type: ignore

from typing import Callable, List


def sensitivities(func: Callable,
                  inputs: List[float],
                  relative: bool = False) -> np.ndarray:
    '''Calculate first-order absolute or relative sensitivities at specific point in parameter space.'''

    grad = np.array(nd.Gradient(func)(inputs))

    if relative:
        y0 = func(inputs)
        grad *= np.array(inputs) / y0

    return grad


def sensitivities2(func: Callable,
                  inputs: List[float],
                  relative: bool = False) -> np.ndarray:
    '''Calculate second-order absolute or relative sensitivities at specific point in parameter space.'''
    
    hessian = np.array(nd.Hessian(func)(inputs))

    if relative:
        y0 = func(inputs)
        xixj = np.array([[xi*xj for xi in inputs] for xj in inputs])
        # TODO: Check the literature on this
        hessian *= xixj / y0

    return hessian

  
def sensitivities_distributions(func: Callable,
                                input_distribs: List[Callable],
                                N: int = 100,
                                relative: bool = False) -> np.ndarray:
    '''Calculate first-order absolute or relative sensitivities at multiple points
    in parameter space based on input distributions to sample from.'''

    results = []
    for _ in range(N):
        inputs = [d() for d in input_distribs]
        sens = sensitivities(func=func, inputs=inputs, relative=relative)
        results.append(sens)

    return np.array(results).T

  
def sensitivities2_distributions(func: Callable,
                                input_distribs: List[Callable],
                                N: int = 100,
                                relative: bool = False) -> np.ndarray:

    pass # TBD!
