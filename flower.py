import random
# If dna is provided, it's used as the DNA string for the flower.
# If dna is not provided, a random DNA string is generated using the generate_random_dna() 
class Flower:
    def __init__(self, dna=None):
        if dna and len(dna) == 8:
            self.dna = dna  
        else:
            self.dna = self.generate_random_dna()

        # Decode the DNA string to gene values 
        self.Sizeofcenter = self.dna[0]  
        self.Colorofcenterred = self.dna[1]
        self.Colorofcentergreen = self.dna[2]
        self.Colorofcenterblue = self.dna[3]
        self.Colorofpetalsred = self.dna[4]
        self.Colorofpetalsgreen = self.dna[5]
        self.Colorofpetalsblue = self.dna[6]
        self.Numberofpetals = self.dna[7]

    def generate_random_dna(self):
        size_of_center = random.randint(5,16)  
        color_of_center_red = random.randint(0,255)
        color_of_center_green = random.randint(0,255)
        color_of_center_blue = random.randint(0,255)
        color_of_petals_red = random.randint(0,255)
        color_of_petals_green = random.randint(0,255)
        color_of_petals_blue = random.randint(0,255)
        number_of_petals = random.randint(0,7)
        flower = [size_of_center,color_of_center_red,color_of_center_green,color_of_center_blue,
                  color_of_petals_red,color_of_petals_green,color_of_petals_blue,number_of_petals]
        return flower
    
    def display(self):
        """Display the flower's characteristics based on DNA String that we decoded in the flower class."""
        print(f"Flower Characteristics:")
        print(f"  - Size of center: {self.Sizeofcenter}")
        print(f"  - Color of center red: {self.Colorofcenterred}")
        print(f"  - Color of center green: {self.Colorofcentergreen}")
        print(f"  - Color of center blue: {self.Colorofcenterblue}")
        print(f"  - Color of petals red: {self.Colorofpetalsred}")
        print(f"  - Color of petals green: {self.Colorofpetalsgreen}")
        print(f"  - Color of petals blue: {self.Colorofpetalsblue}")
        print(f"  - Number of petals: {self.Numberofpetals}")

# Main method 
if __name__ == "__main__":    
    specific_dna = [10, 255, 100, 50, 200, 150, 50, 5]  # Custom DNA
    custom_flower = Flower(dna=specific_dna)
    custom_flower.display()  # Corrected by adding parentheses to call the method
