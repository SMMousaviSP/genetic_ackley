from genetic_ackley import chromosome


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


def test_from_gen_list_chromosome():
    gen_list = [0, 0, 0, 0]
    c = get_from_gen_list_chromosome(gen_list)
    assert str(c) == "0000"
    assert c[0] == 0
    c[0] = 1
    assert c[0] == 1
    assert c[0:2] == [1, 0]


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
