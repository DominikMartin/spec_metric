# Authors: Dominik Martin <martin@kit.edu>
#          Philipp Spitzer <office@ksri.kit.edu>
#          Niklas Kühl <kuehl@kit.edu>

import numpy as np


def spec(y_true, y_pred, a1=0.75, a2=0.25):
    """Stock-keeping-oriented Prediction Error Costs (SPEC)
    Read more in the :ref:`https://arxiv.org/abs/2004.10537`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        Ground truth (correct) target values.
    y_pred : array-like of shape (n_samples,)
        Estimated target values.
    a1 : opportunity costs weighting parameter
        a1 ∈ [0, ∞]. Default value is 0.75.
    a2 : stock-keeping costs weighting parameter
        a2 ∈ [0, ∞]. Default value is 0.25.

    Returns
    -------
    loss : float
        SPEC output is non-negative floating point. The best value is 0.0.

    Examples
    --------
    >>> from spec_metric import spec
    >>> y_true = [0, 0, 5, 6, 0, 5, 0, 0, 0, 8, 0, 0, 6, 0]
    >>> y_pred = [0, 0, 5, 6, 0, 5, 0, 0, 8, 0, 0, 0, 6, 0]
    >>> spec(y_true, y_pred)
    0.1428...
    >>> spec(y_true, y_pred, a1=0.1, a2=0.9)
    0.5142...
    """
    assert len(y_true) > 0 and len(y_pred) > 0
    assert len(y_true) == len(y_pred)

    sum_n = 0
    for t in range(1, len(y_true) + 1):
        sum_t = 0
        for i in range(1, t + 1):
            delta1 = np.sum([y_k for y_k in y_true[:i]]) - np.sum([f_j for f_j in y_pred[:t]])
            delta2 = np.sum([f_k for f_k in y_pred[:i]]) - np.sum([y_j for y_j in y_true[:t]])

            sum_t = sum_t + np.max([0, a1 * np.min([y_true[i - 1], delta1]), a2 * np.min([y_pred[i - 1], delta2])]) * (
                        t - i + 1)
        sum_n = sum_n + sum_t
    return sum_n / len(y_true)
