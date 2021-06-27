"""
Module for easier transformation and tracking between different data structures
when using pandas, scikit-learn, NumPy, SciPy, and Vaex.
"""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TypeSelector(BaseEstimator, TransformerMixin):
    """Class for transforming and encoding pandas data"""
    def __init__(self, dtype):
        self.dtype = dtype

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        assert isinstance(X, pd.DataFrame)
        return X.select_dtypes(include=[self.dtype])


class Xfmr:
    """"""
    def __init__(self):
        pass
