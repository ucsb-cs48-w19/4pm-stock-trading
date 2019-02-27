import pytest

from stocks import getChart


def test_getChart():
   assert len(getChart("MSFT")) == pytest.approx(254)

