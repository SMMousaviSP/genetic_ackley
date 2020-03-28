from models import chromosome


def get_random_chromosome(size):
    return chromosome.Chromosome.random(size)


def get_from_gen_list_chromosome(gen_list):
    return chromosome.Chromosome.from_gen_list(gen_list)


def test_random_chromosom_size():
    c = get_random_chromosome(9)
    assert len(str(c)) == 10
    assert c.size == 10
    c = get_random_chromosome(10)
    assert len(str(c)) == 10
    assert c.size == 10
    assert c.fitness >= 1


def test_from_gen_list_chromosome():
    gen_list = [0, 0, 0, 0]
    c = get_from_gen_list_chromosome(gen_list)
    assert str(c) == "0000"
    assert c[0] == 0
    c[0] = 1
    assert c[0] == 1
    assert c[0:2] == [1, 0]
    assert c.fitness >= 1


def test_phenotype_get_x_and_y():
    gen_list = [1, 1, 0, 0]
    c = get_from_gen_list_chromosome(gen_list)
    assert c.get_x() == 5
    assert c.get_y() == -5


def test_general_crossover():
    c = get_from_gen_list_chromosome([1 for x in range(4)])
    d = get_from_gen_list_chromosome([0 for x in range(4)])

    first_child, second_child = c.general_crossover(d, [0, 2, 4])
    assert str(first_child) == "1100"
    assert str(second_child) == "0011"

    first_child, second_child = c.general_crossover(d, [0, 1, 2, 3, 4])
    assert str(first_child) == "1010"
    assert str(second_child) == "0101"


def test_single_point_crossover():
    c = get_from_gen_list_chromosome([1, 1, 1, 1])
    d = get_from_gen_list_chromosome([0, 0, 0, 0])
    first_child, second_child = c.single_point_crossover(d)

    flag = True
    count = 0
    for i, j in zip(first_child, second_child):
        if i == 1 and j == 0 and flag:
            count += 1
        elif i == 0 and j == 1:
            flag = False
            count += 1
    assert count == 4


def test_n_point_crossover():
    c = get_from_gen_list_chromosome([1 for _ in range(50)])
    d = get_from_gen_list_chromosome([0 for _ in range(50)])
    first_child, second_child = c.single_point_crossover(d)

    sum_children = [x + y for x, y in zip(first_child, second_child)]
    for i in sum_children:
        assert i == 1


def test_universal_crossover():
    c = get_from_gen_list_chromosome([1 for _ in range(50)])
    d = get_from_gen_list_chromosome([0 for _ in range(50)])
    first_child, second_child = c.uniform_crossover(d)

    sum_children = [x + y for x, y in zip(first_child, second_child)]
    for i in sum_children:
        assert i == 1


def test_calculate_ackley_function():
    c = get_random_chromosome(10)
    c.get_x = lambda: 0
    c.get_y = lambda: 0
    assert c.calculate_ackley_function() == 0


def test_calculate_fitness():
    c = get_random_chromosome(10)
    c.get_x = lambda: 0
    c.get_y = lambda: 0
    assert c.calculate_fitness() == 21
