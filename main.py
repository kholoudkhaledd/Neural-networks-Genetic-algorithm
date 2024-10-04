# main.py
from flower import Flower
import random
import tkinter as tk
from tkinter import *
crossover_rate =  0.25
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

    #print("fit:",type(fitness[0]))
    combined = list(zip(population, fitness))

    # Sort the combined list by the second element (the numbers) in descending order
    combined_sorted = sorted(combined, key=lambda x: x[1], reverse=True)

    sorted_objects, sorted_numbers = zip(*combined_sorted)
    #print("sortedobj:" ,list(sorted_objects))
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
    new_crossedover_population = flower_population
    number_of_crossover =(int)(8 * crossover_rate) #4
    chromosome1 = 0
    chromosome2 = 0
    print("Number of chrormosomes to be crossedover:", number_of_crossover)
    for i in range(0 , number_of_crossover , 2):
       while(chromosome1 == chromosome2):
             chromosome1 = random.randint(0,7)
             print("Index 1:",chromosome1)
             chromosome2 = random.randint(0,7) 
             print("Index 2:",chromosome2)
       flower1 = flower_population[chromosome1].dna
       print("Flower 1 before crossover:",flower1)
       flower2 = flower_population[chromosome2].dna 
       print("Flower 2 before crossover:",flower2)
       dna_to_be_flipped = random.randint(0,7)
       print("Index to be flipped:",dna_to_be_flipped)
       temp = flower1[dna_to_be_flipped]
       flower1[dna_to_be_flipped] = flower2[dna_to_be_flipped]
       flower2[dna_to_be_flipped] = temp
       new_crossedover_population[chromosome1] = Flower(flower1)
       print("Flower 1 after crossover:",flower1)
       new_crossedover_population[chromosome2] = Flower(flower2)  
       print("Flower 2 after crossover:",flower2)
       chromosome1 = 0
       chromosome2 = 0
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
          flower[random_gene] = random.randint(8,32)
       elif(random_gene == 7): #number of petals
          flower[random_gene] = random.randint(0,7)
       else:
          flower[random_gene] = random.randint(0,255)   
       new_mutated_population[random_flower] = Flower(flower)
       print("Flower after mutation:",flower)

    for  i in range (0,8):
        print("Flower:",i)
        new_mutated_population[i].display() 

    return new_mutated_population



   
