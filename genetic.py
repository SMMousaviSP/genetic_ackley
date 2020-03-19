"""
Genetic algorithm for Ackley function.

Author S.Mohammad Mousavi <smmousavisp@gmail.com>

Copyright under MIT License, you can find the license file in the main
directory of this project.
"""

import random


class Chromosome():
    """ Representation of a chromosome in both phenotype and genotype

    """
    def __init__(self, size):
        self.genotype = []
        for _ in range(size):
            self.genotype.append(bool(random.getrandbits(1)))

    def __str__(self):
        return ''.join(['1' if x else '0' for x in self.genotype])

    def __repr__(self):
        return ''.join(['1' if x else '0' for x in self.genotype])

    def __getitem__(self, key):
        return '1' if self.genotype[key] else '0'

    def __setitem__(self, key, value):
        self.genotype[key] = bool(int(value))
