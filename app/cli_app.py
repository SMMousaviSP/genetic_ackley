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

    genetic = Genetic(chromosome_size, population_size, generation_count)

    print("Enter crossover method:")
    print("1. n_point")
    print("2. single_point")
    print("3. uniform")
    crossover_method = ""
    crossover_method_number = int(input())
    if crossover_method_number == 1:
        crossover_method = input("Enter n:") + "_point"
    elif crossover_method_number == 2:
        crossover_method = "single_point"
    elif crossover_method == 3:
        crossover_method = "uniform"

    parent_selection_method = selection_input("parent selection")

    survival_selection_method = selection_input("survival selection")

    genetic.run(
        crossover_method,
        parent_selection_method,
        survival_selection_method
    )


def selection_input(selection_type):
    """ Get selection method from input

    :param selection_type: Type of selection (parent selection or
    survival selection)
    :type selection_type: str
    """
    print(f"Enter {selection_type} method:")
    print("1. Roulette Wheal Selection (RWS)")
    print("2. Stochastic Universal Sampling (SUS)")
    print("3. Tournament Selection (TS)")
    selection_number = int(input())
    if selection_number == 1:
        return "rws"
    if selection_number == 2:
        return "sus"
    if selection_number == 3:
        return "ts_" + input("Enter size of tournament:")


if __name__ == "__main__":
    main()
