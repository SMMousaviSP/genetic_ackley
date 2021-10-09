# Genetic Algorithm for Ackley Function
In this program, you can test the efficiency of the genetic algorithm on Ackley function.

You can choose the binary chromosome size, the population in each generation, crossover method, parent selection method, survival selection method, probability of selecting a chromosome for mutation, and probability of changing a gene for mutation.

### Supported Crossover Methods:
- n point
- single point
- uniform

### Supported Parent Selection Methods:
- Roulette Wheel Selection (RWS)
- Stochastic Universal Sampling (SUS)
- Tournament Selection (TS)

### Supported Survival Selection Methods:
- Roulette Wheel Selection (RWS)
- Stochastic Universal Sampling (SUS)
- Tournament Selection (TS)
- Elitism

![Average Fitness in Each Iteration](https://raw.githubusercontent.com/SMMousaviSP/genetic_ackley/master/genetic_ackley_average_fitness.png)

After choosing all of the parameters, the program will show you the best-found answer (the binary chromosome, fitness, x, y, and the output of Ackley function), the best answer in the last iteration, maximum fitness in different iterations plot, and average fitness in different iterations plot.

## How to Run
Install required packages in requirements.txt
```bash
pip install -r requirements.txt
```
run cli_app.py file in the app folder
```bash
python app/cli_app.py
```
