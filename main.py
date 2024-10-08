from flower import Flower
import random
import tkinter as tk
from tkinter import *
crossover_rate =  0.25
mutation_rate = 0.05
original_population = []

def generate_population(size=8):
    global original_population
   
    population = [Flower() for _ in range(size)]
    for  i in range (0,size):
        print("Flower:",i)
        population[i].display() 
    original_population = population       
    return population

def calculate_fitness(fitness,population):

   
    combined = list(zip(population, fitness))


    combined_sorted = sorted(combined, key=lambda x: x[1], reverse=True)

    sorted_objects, sorted_numbers = zip(*combined_sorted)

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
    
    number_of_crossover = int(8 * crossover_rate)
    print("Number of chromosomes to be crossed over:", number_of_crossover)
    
    for i in range(0, number_of_crossover, 2):
        chromosome1 = random.randint(0,7)
        chromosome2 = random.randint(0, 7)
        while chromosome1 == chromosome2:
            chromosome2 = random.randint(0, 7)
        
        flower1 = flower_population[chromosome1].dna
        flower2 = flower_population[chromosome2].dna
        
        print(f"Flower 1 before crossover (Index {chromosome1}): {flower1}")
        print(f"Flower 2 before crossover (Index {chromosome2}): {flower2}")
        
       
        point1 = random.randint(0, 7)
        point2 = random.randint(point1, 7)
        
        print(f"Crossover points: {point1}, {point2}")
        
        
        for j in range(point1, point2 + 1):
        
            temp = flower2[j]
            flower2[j]=flower1[j]
            flower1[j]=temp
        
        print(f"Flower 1 after crossover: {flower1}")
        print(f"Flower 2 after crossover: {flower2}")

        new_crossedover_population[chromosome1] = Flower(flower1)
        new_crossedover_population[chromosome2] = Flower(flower2)
    
    return new_crossedover_population


def mutation(crossedover_population):  
    
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
       if(random_gene == 0): 
          flower[random_gene] = random.randint(8,32)
       elif(random_gene == 7): 
          flower[random_gene] = random.randint(0,7)
       else:
          flower[random_gene] = random.randint(0,255)   
       new_mutated_population[random_flower] = Flower(flower)
       print("Flower after mutation:",flower)

    for  i in range (0,8):
        print("Flower:",i)
        new_mutated_population[i].display() 

    return new_mutated_population



   
