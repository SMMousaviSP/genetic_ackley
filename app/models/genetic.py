"""
Genetic algorithm implementation for Ackley function.
"""


class Genetic:
    """ Genetic algorithm for Ackley function.

    """

    def __init__(
            self,
            chromosome_size,
            population_size,
            generation_count,
            crossover_method="3_point",
            parent_selection_method="rws",
            survival_selection_method="rws"
    ):
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.generation_count = generation_count
        self.crossover_method = crossover_method
        self.parent_selection_method = parent_selection_method
        self.survival_selection_method = survival_selection_method
