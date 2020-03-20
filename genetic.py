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
    def __init__(self, size, minimum=-5, maximum=5):
        if size % 2 == 1:
            print("size can't be odd, increasing by 1 automatically")
            size += 1
        self.size = size
        self.minimum = minimum
        self.maximum = maximum

        self.genotype = []
        for _ in range(self.size):
            self.genotype.append(bool(random.getrandbits(1)))

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
