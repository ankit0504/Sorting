import random

def insertion_sort(given_list):
    for i in range (len(given_list)):
        prev = i - 1
        while prev >= 0 and given_list[i] < given_list[prev]:
            given_list[prev + 1] = given_list[prev]
            prev -= 1
        given_list[prev + 1] = given_list[i]
    return given_list


def test_empty_list():
    assert insertion_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0,100)
    assert insertion_sort([rand_num]) == [rand_num]


def test_already_sorted():
    already_sorted = [0,1,2,3,4,5,6,7,8,9]
    assert insertion_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [9,8,7,6,5,4,3,2,1,0]
    assert insertion_sort(decrementing) == sorted(decrementing)


def test_random_positives():
    rand_nums = random.sample(range(1, 100), 5)
    assert insertion_sort(rand_nums) == sorted(rand_nums)


def test_random_negatives():
    rand_nums = random.sample(range(-100,-1), 5)
    assert insertion_sort(rand_nums) == sorted(rand_nums)


def test_random_numbers():
    rand_nums = random.sample(range(-100, 100), 10)
    assert insertion_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(1,5) for x in range(1, 10)]
    assert insertion_sort(rand_nums) == sorted(rand_nums)
