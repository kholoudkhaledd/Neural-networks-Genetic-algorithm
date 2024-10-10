# main.py
from flower import Flower
import random
import tkinter as tk
from tkinter import *
crossover_rate =  0.75
mutation_rate = 0.05
original_population = []
# Function to generate a population of 8 flowers
def generate_population(size=8):
    global original_population
    """Generate a population of 'size' Flower objects."""
    print("----------------Generate Population----------------")
    population = [Flower() for _ in range(size)]
    for  i in range (0,size):
        print("Flower:",i)
        population[i].display() 
    original_population = population       
    return population
#calaculate fitness for each flower 
def calculate_fitness(fitness,population):

    print("fit:",type(fitness[0]))
    combined = list(zip(population, fitness))

    # Sort the combined list by the second element (the numbers) in descending order
    combined_sorted = sorted(combined, key=lambda x: x[1], reverse=True)

    sorted_objects, sorted_numbers = zip(*combined_sorted)
    print("sortedobj:" ,list(sorted_objects))
    return list(sorted_objects)

def selection_elitism(flowers):

    flower_population = [None]*8
    print("len:" ,len(flowers))
    for i in range (0,4):
       flower_population[i] = flowers[i]

    flower_population [4] = flower_population[0]   
    flower_population [5] = flower_population[1]
    flower_population [6] = flower_population[2]
    flower_population [7] = flower_population[3]

    print("flower pop:", flower_population)
   
    return flower_population

def crossover(flower_population):
    print("----------------CrossOver----------------")
    
    # Create a deep copy of the flower population to avoid modifying the original list in place
    
    number_of_crossover = int(8 * crossover_rate)  # 4
    print("Number of chromosomes to be crossed over:", number_of_crossover)

    for i in range(0, number_of_crossover, 2):
        chromosome1, chromosome2 = 0, 0
        flower1, flower2 = [], []
        
        # Loop until two different chromosomes are selected and their DNA is not the same
        while chromosome1 == chromosome2 or chromosomeraresame(flower1, flower2):
            chromosome1 = random.randint(0, 7)
            chromosome2 = random.randint(0, 7)
            
            # Assign the DNA sequences for the selected chromosomes
            flower1 = new_crossedover_population[chromosome1].dna
            flower2 = new_crossedover_population[chromosome2].dna
        
        print(f"Selected Chromosome 1: {chromosome1}, DNA: {flower1}")
        print(f"Selected Chromosome 2: {chromosome2}, DNA: {flower2}")
        # Randomly choose crossover points
        point1 = random.randint(0, len(flower1) - 1)
        point2 = random.randint(0, len(flower2) - 1)
        # Ensure point1 is less than point2
        if point1 > point2:
            point1, point2 = point2, point1
        
        print(f"Crossover points: {point1}, {point2}")

        # Perform crossover between point1 and point2
        for j in range(point1, point2 + 1):
            flower1[j], flower2[j] = flower2[j], flower1[j]
        new_crossedover_population[chromosome1]=Flower(flower1)
        new_crossedover_population[chromosome2]=Flower(flower2)

        print("Flower 1 after crossover:", flower1)
        print("Flower 2 after crossover:", flower2)
        print("-----------------------after crossover before return -----------------")
      

    return new_crossedover_population

def mutation(crossedover_population):  #mutate 1 flower
    
    print("----------------Mutation----------------")
    new_mutated_population = crossedover_population
    number_of_mutated_genes =(int)(8 * 8 * mutation_rate) 
    for i in range (0,number_of_mutated_genes):
       random_flower = random.randint(0,7)
       print("Random flower to be mutated:",random_flower)
       random_gene = random.randint (0,7)
       print("Random gene to be muatated:",random_gene)
       flower = new_mutated_population[random_flower].dna
       print("Flower before mutation:",flower)
       if(random_gene == 0): #size of center
          flower[random_gene] = random.randint(5,16)
       elif(random_gene == 7): #number of petals
          flower[random_gene] = random.randint(0,7)
       else:
          flower[random_gene] = random.randint(0,255)   
       new_mutated_population[random_flower] = Flower(flower)
       print("Flower after mutation:",flower)

    return new_mutated_population



   
