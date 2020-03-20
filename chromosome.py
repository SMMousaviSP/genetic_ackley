"""
Genetic algorithm for Ackley function.

Author S.Mohammad Mousavi <smmousavisp@gmail.com>

Copyright under MIT License, you can find the license file in the main
directory of this project.
"""

import random


class Chromosome():
    """ Representation of a chromosome in both phenotype and genotype.

    """
    def __init__(self, genotype, minimum=-5, maximum=5):
        self.size = len(genotype)
        self.minimum = minimum
        self.maximum = maximum
        self.genotype = genotype

    @classmethod
    def random(cls, size, minimum=-5, maximum=5):
        """ Create a random chromosome instance.

        :param size: Size of chromosome
        :type size: int
        :param minimum: Minimum value in phenotype, defaults to -5
        :type minimum: int, optional
        :param maximum: Maximum value in phenotype, defaults to 5
        :type maximum: int, optional
        :return: An instance of chromosome class
        :rtype: Chromosome
        """
        if size % 2 == 1:
            print("size can't be odd, increasing by 1 automatically")
            size += 1
        genotype = []
        for _ in range(size):
            genotype.append(bool(random.getrandbits(1)))
        return cls(genotype, minimum, maximum)

    @classmethod
    def from_gen_list(cls, gen_list, minimum=-5, maximum=5):
        """ Create a chromosome based on a gen_list.

        :param gen_list: A list which the chromosome should be created from
        :type gen_list: list
        :param minimum: Minimum value in phenotype, defaults to -5
        :type minimum: int, optional
        :param maximum: Maximum value in phenotype, defaults to 5
        :type maximum: int, optional
        :return: An instance of chromosome class
        :rtype: Chromosome
        """
        genotype = [bool(int(x)) for x in gen_list]
        return cls(genotype, minimum, maximum)

    def __str__(self):
        return ''.join(['1' if x else '0' for x in self.genotype])

    def __repr__(self):
        return ''.join(['1' if x else '0' for x in self.genotype])

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [1 if x else 0 for x in self.genotype[key]]
        return 1 if self.genotype[key] else 0

    def __setitem__(self, key, value):
        self.genotype[key] = bool(int(value))

    def __calculate_phenotype_value(self, gen_list):
        raw_value = 0
        for i, gen in enumerate(gen_list):
            raw_value += gen * (2 ** i)
        return (
            raw_value *
            ((self.maximum - self.minimum) / ((2 ** len(gen_list)) - 1))
            + self.minimum
        )

    def __get_random_split_point_list(self, count):
        """ Generate random unique split points.

        :param count: Number of split points needed.
        :type count: int
        :return: Sorted list of random split points
        :rtype: list
        """
        split_point_list = random.sample(range(1, self.size), count)
        split_point_list.sort()
        split_point_list.insert(0, 0)
        split_point_list.append(self.size)
        return split_point_list

    def general_crossover(self, second_parent, split_point_list):
        """ Crossover with two parent chromosome and produce two children.

        :param second_parent: Second parent
        :type second_parent: Chromosome
        :param split_point_list: A list with random split points
        :type split_point_list: list
        :return: A tuple containing two children
        :rtype: tuple
        """
        first_parent = self
        first_child = []
        second_child = []
        for i, (start, end) in enumerate(
                zip(split_point_list[:-1], split_point_list[1:])
        ):
            if i % 2 == 0:
                first_child[start:end] = first_parent[start:end]
                second_child[start:end] = second_parent[start:end]
            else:
                first_child[start:end] = second_parent[start:end]
                second_child[start:end] = first_parent[start:end]
        return (
            self.from_gen_list(first_child), self.from_gen_list(second_child)
        )

    def single_point_crossover(self, second_parent):
        """ Single point crossover.

        :param second_parent: Second parent
        :type second_parent: Chromosome
        :return: A tuple containing two children
        :rtype: tuple
        """
        split_point_list = self.__get_random_split_point_list(1)
        return self.general_crossover(second_parent, split_point_list)

    def get_x(self):
        """ Get value of x in phenotype space.

        :return: Value of x
        :rtype: float
        """
        return self.__calculate_phenotype_value(self[:int(self.size/2)])

    def get_y(self):
        """ Get value of y in phenotype space.

        :return: Value of y
        :rtype: float
        """
        return self.__calculate_phenotype_value(self[int(self.size/2):])
