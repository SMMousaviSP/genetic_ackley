"""
Command-line interface for genetic algorithm implementation for ackley
function.
"""

from models.genetic import Genetic


def main():
    """ Main function
    """
    chromosome_size = int(input("Enter size of binary chromosome:"))

    population_size = int(
        input("Enter size of population in each generation:")
    )

    generation_count = int(input("Enter number of generations:"))

    print("Enter crossover method:")
    print("1. n_point")
    print("2. single_point")
    print("3. uniform")
    crossover_method = ""
    crossover_method_number = int(input())
    if crossover_method_number == 1:
        crossover_method = int(input("Enter n:")) + "_point"
    elif crossover_method_number == 2:
        crossover_method = "single_point"
    elif crossover_method == 3:
        crossover_method = "uniform"
    genetic = Genetic(chromosome_size, population_size, generation_count)


if __name__ == "__main__":
    main()
