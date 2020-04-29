from models.genetic import Genetic
from models.chromosome import Chromosome


def test_genetic():
    g = Genetic(10, 10, 10)
    assert len(g.current_generation) == 10
    assert isinstance(g.current_generation[0], Chromosome)
    assert g.current_generation[0].size == 10


def test_roulette_wheal_selection():
    chromosome_list = [Chromosome.random(10) for _ in range(5)]
    for _ in range(20):
        chromosome = Genetic.roulette_wheal_selection(chromosome_list)
        assert isinstance(chromosome, Chromosome)


def test_selection():
    chromosome_list = [Chromosome.random(10) for _ in range(10)]
    selected_chromosome_list = Genetic.selection(chromosome_list, 10, "rws")
    assert len(selected_chromosome_list) == 10
    for chromosome in selected_chromosome_list:
        assert isinstance(chromosome, Chromosome)
