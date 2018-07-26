import random

def selection_sort(num_list):
    if len(num_list) < 2:
        return num_list
    for i in range(len(num_list)):
        swapped = i
        for j in range (i+1, len(num_list)):
            if num_list[swapped] > num_list[j]:
                swapped = j
        num_list[i], num_list[swapped] = num_list[swapped], num_list[i]
    return num_list


def test_already_sorted():
    already_sorted = [0,1,2,3,4,5,6,7,8,9]
    assert selection_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [9,8,7,6,5,4,3,2,1,0]
    assert selection_sort(decrementing) == sorted(decrementing)


def test_random_numbers():
    rand_nums = random.sample(range(100), 10)
    assert selection_sort(rand_nums) == sorted(rand_nums)


def test_empty_list():
    assert selection_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0,100)
    assert selection_sort([rand_num]) == [rand_num]


def test_random_negatives():
    rand_nums = random.sample(range(-100,-1), 5)
    assert selection_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(1,5) for x in range(1, 10)]
    assert selection_sort(rand_nums) == sorted(rand_nums)
