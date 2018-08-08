from time import sleep
from threading import Timer
import random

# TAKEN FROM ROSETTACODE.ORG

def sleep_sort(values):
    sleep_sort.result = []
    def add1(x):
        sleep_sort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleep_sort.result

def test_random_positives():
    rand_nums = random.sample(range(1, 4), 2)
    assert sleep_sort(rand_nums) == sorted(rand_nums)
