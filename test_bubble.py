import random

def bubble_sort(given_list):
    for i in range(len(given_list)):
        for j in range(len(given_list)-i-1):
            if given_list[j] > given_list[j+1]:
                given_list[j], given_list[j+1] = given_list[j+1], given_list[j]
    return given_list


def test_already_sorted():
    already_sorted = [0,1,2,3,4,5,6,7,8,9]
    assert bubble_sort(already_sorted) == sorted(already_sorted)


def test_decrementing():
    decrementing = [9,8,7,6,5,4,3,2,1,0]
    assert bubble_sort(decrementing) == sorted(decrementing)


def test_random_numbers():
    rand_nums = random.sample(range(100), 10)
    assert bubble_sort(rand_nums) == sorted(rand_nums)


def test_empty_list():
    assert bubble_sort([]) == []


def test_one_element_list():
    rand_num = random.randint(0,100)
    assert bubble_sort([rand_num]) == [rand_num]


def test_random_negatives():
    rand_nums = random.sample(range(-100,-1), 5)
    assert bubble_sort(rand_nums) == sorted(rand_nums)


def test_has_duplicates():
    rand_nums = [random.randint(1,5) for x in range(1, 10)]
    assert bubble_sort(rand_nums) == sorted(rand_nums)
