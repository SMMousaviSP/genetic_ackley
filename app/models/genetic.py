"""
Genetic algorithm implementation for Ackley function.
"""

import random

from models.chromosome import Chromosome


class Genetic:
    """ Genetic algorithm for Ackley function.

    """

    def __init__(self, chromosome_size, population_size, generation_count):
        """ Initialize an instance of genetic class.
        :param chromosome_size: Size of each binary chromosome.
        :type chromosome_size: int
        :param population_size: Size of each generation population
        :type population_size: int
        :param generation_count: Number of generations
        :type generation_count: int
        """
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.generation_count = generation_count
        self.current_generation = self.initialize_population()
        self.next_generation = list()

    def initialize_population(self):
        """ Initialize random population.

        :return: List of random chromosome
        :rtype: list
        """
        return [
            Chromosome.random(self.chromosome_size)
            for _ in range(self.population_size)
        ]

    def run(
            self, crossover_method="3_point",
            parent_selection_method="rws",
            survival_selection_method="rws"
    ):
        """ Run genetic algorithm for ackley function in given methods.

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

    def parent_selection(self, parent_selection_method):
        """ Parent selection based on selection method.

        :param parent_selection_method: Parent selection method (rws, sus, ts,
        rb)
        :type parent_selection_method: str
        :return: List of chromosomes, to be the parents of the next generation
        :rtype: list
        """
        return Genetic.selection(
            self.current_generation,
            self.population_size,
            parent_selection_method
        )

    def go_to_the_future(self):
        """ Change current generation to the next generation.

        :return: NoneType
        :rtype: NoneType
        """
        self.current_generation = self.next_generation
        self.next_generation = list()

    @staticmethod
    def survival_selection(chromosome_list, survival_selection_method):
        """ Survival selection based on selection method.

        :param chromosome_list: Chromosome list to select from
        :type chromosome_list: list
        :param survival_selection_method: Survival selection method (rws, sus,
        ts, rb)
        :type survival_selection_method: str
        :return: List of chromosomes, to be the survivals of the next
        generation
        :rtype: list
        """
        return Genetic.selection(
            chromosome_list,
            2,
            survival_selection_method
        )

    @staticmethod
    def selection(chromosome_list, size, selection_method):
        """ Select chromosomes based on selection method.

        :param chromosome_list: Chromosome list to select from
        :type chromosome_list: list
        :param size: Size of chromosomes that should be selected
        :type size: int
        :param selection_method: Selection method (rws, sus, ts, rb)
        :type selection_method: str
        :return: List of selected chromosomes
        :rtype: list
        """
        if selection_method == "rws":
            return [
                Genetic.roulette_wheal_selection(chromosome_list)
                for _ in range(size)
            ]
        # TODO: Add sus, ts and rb selection
        return False

    @staticmethod
    def fitness_sum(chromosome_list):
        """ Add up all the chromosomes fitness in current generation.

        :return: Sum of all chromosomes fitness in current generation
        :rtype: float
        """
        summation = 0
        for chromosome in chromosome_list:
            summation += chromosome.fitness
        return summation

    @staticmethod
    def roulette_wheal_selection(chromosome_list):
        """ Select a chromosome based on roulette wheal selection (rws)

        :param chromosome_list: List of chromosome
        :type chromosome_list: list
        :return: Selected chromosome based on roulette wheal selection
        :rtype: Chromosome
        """
        fitness_sum = Genetic.fitness_sum(chromosome_list)
        random_float = random.uniform(0, fitness_sum)
        for chromosome in chromosome_list:
            random_float -= chromosome.fitness
            if random_float <= 0:
                return chromosome
        return chromosome_list[-1]
