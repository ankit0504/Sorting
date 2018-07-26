import random

def counting_sort(given_list):
    if len(given_list) < 2:
        return given_list
    minimum = min(given_list)
    maximum = max(given_list)
    num_instances = [0 for i in range(minimum, maximum+1)]
    returnable = [0 for i in range(len(given_list))]
    for num in given_list:
        num_instances[num - minimum] += 1
    for i in range(1, len(num_instances)):
        num_instances[i] += num_instances[i - 1]
    for i in reversed(given_list):
        returnable[num_instances[i - minimum] - 1] = i
        num_instances[i - minimum] -= 1
    return returnable


def test_already_sorted():
    already_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert counting_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert counting_sort(decrementing) == sorted(decrementing)


def test_empty_list():
    assert counting_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0, 100)
    assert counting_sort([rand_num]) == [rand_num]


def test_random_positives():
    rand_nums = random.sample(range(1, 100), 5)
    assert counting_sort(rand_nums) == sorted(rand_nums)


def test_random_negatives():
    rand_nums = random.sample(range(-100, -1), 5)
    assert counting_sort(rand_nums) == sorted(rand_nums)


def test_random_numbers():
    rand_nums = random.sample(range(-100, 100), 10)
    assert counting_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(1, 5) for x in range(1, 10)]
    assert counting_sort(rand_nums) == sorted(rand_nums)
