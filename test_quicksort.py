import random

def quicksort(given_list):
    if not given_list:
        return (given_list)
    less = []
    piv_list = []
    greater = []
    piv_el = given_list[random.randint(0, len(given_list) - 1)]
    for i in given_list:
        if i < piv_el: less.append(i)
        elif i == piv_el: piv_list.append(i)
        else: greater.append(i)
    less = quicksort(less)
    greater = quicksort(greater)
    return less + piv_list + greater


def test_empty_list():
    assert quicksort([]) == []


def test_one_element_list():
    rand_num = random.randint(0, 100)
    assert quicksort([rand_num]) == [rand_num]


def test_already_sorted():
    already_sorted = [i for i in range(100)]
    assert quicksort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [i for i in reversed(range(100))]
    assert quicksort(decrementing) == sorted(decrementing)


def test_random_positives():
    rand_nums = random.sample(range(1, 250), 100)
    assert quicksort(rand_nums) == sorted(rand_nums)


def test_random_negatives():
    rand_nums = random.sample(range(-250, -1), 100)
    assert quicksort(rand_nums) == sorted(rand_nums)


def test_random_numbers():
    rand_nums = random.sample(range(-250, 250), 100)
    assert quicksort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(0, 24) for x in range(100)]
    assert quicksort(rand_nums) == sorted(rand_nums)
