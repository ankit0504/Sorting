import random

def bubble_sort(given_list):
    for i in range(len(given_list)):
        for j in range(len(given_list) - i - 1):
            if given_list[j] > given_list[j + 1]:
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
    return given_list


def test_empty_list():
    assert bubble_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0, 100)
    assert bubble_sort([rand_num]) == [rand_num]


def test_already_sorted():
    already_sorted = [i for i in range(100)]
    assert bubble_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [i for i in reversed(range(100))]
    assert bubble_sort(decrementing) == sorted(decrementing)


def test_random_positives():
    rand_nums = random.sample(range(1, 250), 100)
    assert bubble_sort(rand_nums) == sorted(rand_nums)


def test_random_negatives():
    rand_nums = random.sample(range(-250, -1), 100)
    assert bubble_sort(rand_nums) == sorted(rand_nums)


def test_random_numbers():
    rand_nums = random.sample(range(-250, 250), 100)
    assert bubble_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(0, 24) for x in range(100)]
    assert bubble_sort(rand_nums) == sorted(rand_nums)
