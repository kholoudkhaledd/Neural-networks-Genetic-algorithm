# main.py
from flower import Flower

# Function to generate a population of 8 flowers
def generate_population(size=8):
    """Generate a population of 'size' Flower objects."""
    population = [Flower() for _ in range(size)]
    return population

# Main method 
if __name__ == "__main__":
    population = generate_population()  # Generate a population of 8 flowers
    for idx, flower in enumerate(population):
        print(f"Flower {idx+1}:")
        flower.display()
        print()  # Print a blank line between flowers
