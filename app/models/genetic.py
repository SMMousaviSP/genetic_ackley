"""
Genetic algorithm implementation for Ackley function.
"""

from genetic_ackley.app.models.chromosome import Chromosome


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
        """ Initialize an instance of genetic class.
        :param chromosome_size: Size of each binary chromosome.
        :type chromosome_size: int
        :param population_size: Size of each generation population
        :type population_size: int
        :param generation_count: Number of generations
        :type generation_count: int
        :param crossover_method: Crossover method for binary chromosome, could
        be "n_point" (a number instead of n), "single_point" or "uniform",
        defaults to "3_point"
        :type crossover_method: str, optional
        :param parent_selection_method: Parent selection method, could be "rws"
        (Roulette Wheal Selection), "sus" (Stochastic Universal Sampling), "ts"
        (Tournament Selection) or "rb" (Rank-based Selection), defaults to "ts"
        :type parent_selection_method: str, optional
        :param survival_selection_method: TODO, defaults to "rws"
        :type survival_selection_method: str, optional
        """
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.generation_count = generation_count
        self.crossover_method = crossover_method
        self.parent_selection_method = parent_selection_method
        self.survival_selection_method = survival_selection_method

    def initialize_population(self):
        self.current_generation = [
            Chromosome.random(self.chromosome_size)
            for _ in range(self.population_size)
        ]
