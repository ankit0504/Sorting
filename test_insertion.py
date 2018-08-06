import random

def insertion_sort(arr):
    for i in range (len(arr)):
        comp = i - 1
        while comp >= 0 and arr[i] < arr[comp]:
            arr[comp + 1] = arr[comp]
            comp -= 1
        arr[comp + 1] = arr[i]
    return arr


def test_empty_list():
    assert insertion_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0, 100)
    assert insertion_sort([rand_num]) == [rand_num]


def test_already_sorted():
    already_sorted = [i for i in range(100)]
    assert insertion_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [i for i in reversed(range(100))]
    assert insertion_sort(decrementing) == sorted(decrementing)


def test_random_positives():
    rand_nums = random.sample(range(1, 250), 100)
    assert insertion_sort(rand_nums) == sorted(rand_nums)


def test_random_negatives():
    rand_nums = random.sample(range(-250, -1), 100)
    assert insertion_sort(rand_nums) == sorted(rand_nums)


def test_random_numbers():
    rand_nums = random.sample(range(-250, 250), 100)
    assert insertion_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(0, 24) for x in range(100)]
    assert insertion_sort(rand_nums) == sorted(rand_nums)
