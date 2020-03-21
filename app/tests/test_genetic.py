from genetic_ackley.app.models.genetic import Genetic
from genetic_ackley.app.models.chromosome import Chromosome


def test_initialize_population():
    g = Genetic(10, 10, 10)
    g.initialize_population()
    assert len(g.current_generation) == 10
    assert isinstance(g.current_generation[0], Chromosome)
    assert g.current_generation[0].size == 10
