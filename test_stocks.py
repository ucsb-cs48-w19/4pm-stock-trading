import pytest

from stocks import getChart
from stocklist import save_stock_tickers


def test_getChart():
   assert len(getChart("MSFT")) == pytest.approx(254, 10)
   
def test_save_stock_tickers():
   names = []
   tickers = []
   save_stock_tickers(names,tickers)
   assert len(names) == len(tickers)

