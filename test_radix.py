import random

def radix_sort(arr):
    if len(arr) < 2:
        return arr
    abs_min = abs(min(arr))
    arr = [i+abs_min for i in arr]
    max_length = False
    current_digit = 1
    while not max_length:
        max_length = True
        buckets = [[] for _ in range(10)]
        for  i in arr:
            quotient = i // current_digit
            buckets[quotient % 10].append( i )
            if max_length and quotient > 0:
                max_length = False
        a = 0
        for b in range(10):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        current_digit *= 10
    arr = [i - abs_min for i in arr]
    return arr


def test_empty_list():
    assert radix_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0, 100)
    assert radix_sort([rand_num]) == [rand_num]


def test_already_sorted():
    already_sorted = [i for i in range(100)]
    assert radix_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [i for i in reversed(range(100))]
    assert radix_sort(decrementing) == sorted(decrementing)


def test_random_positives():
    rand_nums = random.sample(range(1, 250), 100)
    assert radix_sort(rand_nums) == sorted(rand_nums)


def test_random_negatives():
    rand_nums = random.sample(range(-250, -1), 100)
    assert radix_sort(rand_nums) == sorted(rand_nums)


def test_random_numbers():
    rand_nums = random.sample(range(-250, 250), 100)
    assert radix_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(0, 24) for x in range(100)]
    assert radix_sort(rand_nums) == sorted(rand_nums)
