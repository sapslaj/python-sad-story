#!/usr/bin/python
from __future__ import print_function
import time
from contextlib import contextmanager

@contextmanager
def beat(length):
    yield
    time.sleep(length)

with beat(2):
    print("apolgy for bad english")

with beat(3):
    print("where were u wen club penguin die")

with beat(4):
    print("i was at house eating dorito when phone ring")

with beat(2):
    print('"club penguin is kil"')

with beat(2):
    print('"no"')
