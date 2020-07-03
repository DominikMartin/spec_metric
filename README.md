 # Stock-keeping-oriented Prediction Error Costs (SPEC)
Python package to evaluate forecasts of lumpy or intermittent demand time series with Stock-keeping-oriented Prediction Error Costs (SPEC).

Please note our [publication](https://arxiv.org/abs/2004.10537) for details.

### Installation
This package requires numpy.
```
pip install git+https://github.com/DominikMartin/spec_metric.git
```

### Usage
```python
>>> from spec_metric import spec

>>> y_true = [0, 0, 5, 6, 0, 5, 0, 0, 0, 8, 0, 0, 6, 0]
>>> y_pred = [0, 0, 5, 6, 0, 5, 0, 0, 8, 0, 0, 0, 6, 0]

>>> spec(y_true, y_pred)
0.1428...

>>> spec(y_true, y_pred, a1=0.1, a2=0.9)
0.5142...
```

### Citation
If you use SPEC in a scientific publication, we would appreciate citations:

Martin, D.; Spitzer, P.; Kühl, N. (2020). A New Metric for Lumpy and Intermittent Demand Forecasts: Stock-keeping-oriented Prediction Error Costs. In Proceedings of the 53rd Annual Hawaii International Conference on System Sciences (HICSS-53), Grand Wailea, Maui, HI, January 7-10, 2020.
