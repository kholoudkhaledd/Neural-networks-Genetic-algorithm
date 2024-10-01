# main.py
from flower import Flower
import random
import tkinter as tk
from tkinter import *
from ui import ui_generation

#Generate Random Population
#Calculate Fitness
#Selection by Elitism
#CrossOver Rate 0.75 , 6 Chromosomes
#Mutate 22 Bits 22/2=11 Bits 
#Calculate Fitness

# Function to generate a population of 8 flowers
def generate_population(size=8):
    """Generate a population of 'size' Flower objects."""
    population = [Flower() for _ in range(size)]
    return population

def calculate_fitness():
    #Rule of fitness
    return


def selection_elitism():
    return

def crossover(flower_population):

    crossover_population = []
    for i in range( 0, 5, 2 ):
        pointer1 = random.randint(0,26)
        print("pointer 1:", pointer1)
        pointer2 = random.randint(27,54)
        print("pointer 2:", pointer2)
        flower0 = flower_population[i].dna
        print("F1 before crossover:",flower0)
        flower1 = flower_population[i+1].dna
        print("F2 before crossover:",flower1)
        flower0_end = flower0[pointer1:pointer2]
        print("F1 part:",flower0_end)
        flower1_end = flower1[pointer1:pointer2]
        print("F2 part:",flower1_end)
        flower0_new = flower0[0:pointer1]+flower1_end+flower0[pointer2:]
        print("F1 after crossover:",flower0_new)
        flower1_new = flower1[0:pointer1]+flower0_end+flower1[pointer2:]
        print("F2 after crossover:",flower1_new)
        crossover_population.append(Flower(flower0_new))
        crossover_population.append(Flower(flower1_new))
        print("----------------------")
 
    crossover_population.append(flower_population[6])
    crossover_population.append(flower_population[7])
    return crossover_population


def mutation(crossedover_population):
 
 crossedover_population[6] = Flower(flip_bits(crossedover_population[6].dna)) 
 crossedover_population[7] = Flower(flip_bits(crossedover_population[7].dna)) 

 return crossedover_population


#Extra Methods
def flip_bits(dna):
  
  indices = random.sample(range(55), 11)
  print("indices to be changed:",indices)
  dna_list  = list(dna)  
    
  for index in indices:
    if  dna_list[index] == '0':
      dna_list[index] = '1'
    else: 
      dna_list[index] = '0'

  return ''.join(dna_list) 


        



# Main method 
if __name__ == "__main__":
   ui_generation()

