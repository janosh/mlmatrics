from mlmatrics import cum_err, cum_err_cum_res, cum_res

from . import y_pred, y_true


def test_cum_err():
    cum_err(y_pred - y_true)


def test_cum_res():
    cum_res(y_pred - y_true)
