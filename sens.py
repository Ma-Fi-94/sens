import numpy as np
import numdifftools as nd  # type: ignore

from typing import Callable, List


def sensitivities(func: Callable,
                  inputs: List[float],
                  relative: bool = False) -> np.ndarray:

    grad = nd.Gradient(func)(inputs)

    if relative:
        y0 = func(inputs)
        grad = np.array(grad)
        grad *= np.array(inputs) / y0

    return grad


def sensitivities_distributions(func: Callable,
                                input_distribs: List[Callable],
                                N: int = 100,
                                relative: bool = False) -> np.ndarray:

    results = []
    for _ in range(N):
        inputs = [d() for d in input_distribs]
        sens = sensitivities(func=func, inputs=inputs, relative=relative)
        results.append(sens)

    return np.array(results).T
