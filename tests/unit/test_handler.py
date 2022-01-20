import json

import pytest

from pay_money import app


def test_is_pay_money():
    assert app.is_pay_money(123) == [1,2,3] 


