import random

def selection_sort(num_list):
    for i in range(len(num_list)):
        to_swap = i
        for j in range (i + 1, len(num_list)):
            if num_list[to_swap] > num_list[j]:
                to_swap = j
        num_list[i], num_list[to_swap] = num_list[to_swap], num_list[i]
    return num_list


def test_empty_list():
    assert selection_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0, 100)
    assert selection_sort([rand_num]) == [rand_num]


def test_already_sorted():
    already_sorted = [i for i in range(100)]
    assert selection_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [i for i in reversed(range(100))]
    assert selection_sort(decrementing) == sorted(decrementing)


def test_random_positives():
    rand_nums = random.sample(range(1, 250), 100)
    assert selection_sort(rand_nums) == sorted(rand_nums)


def test_random_negatives():
    rand_nums = random.sample(range(-250, -1), 100)
    assert selection_sort(rand_nums) == sorted(rand_nums)


def test_random_numbers():
    rand_nums = random.sample(range(-250, 250), 100)
    assert selection_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(0, 24) for x in range(100)]
    assert selection_sort(rand_nums) == sorted(rand_nums)
