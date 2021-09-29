# -*- encoding: utf-8 -*-
from my_test.run import Run

def test_run():
    r = Run()
    assert r.return_true()
    assert 1 != 1
