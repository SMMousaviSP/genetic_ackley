from models.genetic import Genetic
from models.chromosome import Chromosome


def test_genetic():
    g = Genetic(10, 10, 10)
    assert len(g.current_generation) == 10
    assert isinstance(g.current_generation[0], Chromosome)
    assert g.current_generation[0].size == 10
