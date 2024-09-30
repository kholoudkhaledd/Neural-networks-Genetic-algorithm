import random
# If dna is provided, it's used as the DNA string for the flower.
# If dna is not provided, a random DNA string is generated using the generate_random_dna() 
class Flower:
    def __init__(self, dna=None):
        if dna:
            self.dna = dna  # Use existing binary DNA string if provided
        else:
            self.dna = self.generate_random_dna()

        # Decode the DNA string to gene values 
        self.Sizeofcenter = int(self.dna[0:4], 2)  # First 4 bits
        self.Colorofcenter = (
            int(self.dna[4:12], 2),  # Next 8 bits for Red
            int(self.dna[12:20], 2),  # Next 8 bits for Green
            int(self.dna[20:28], 2)  # Next 8 bits for Blue
        )
        self.Colorofpetals = (
            int(self.dna[28:36], 2),  # Next 8 bits for Red
            int(self.dna[36:44], 2),  # Next 8 bits for Green
            int(self.dna[44:52], 2)  # Next 8 bits for Blue
        )
        self.Numberofpetals = int(self.dna[52:55], 2)  # Last 3 bits
# The link I useed for genratng the binary strings with the n bits
#  https://www.geeksforgeeks.org/python-program-to-generate-random-binary-string/
    def generate_binary_string(self,n,gene): 
        # Generate a random number with n bits
        if gene:
            return format(random.randint(1, 10), '04b') 
        number = random.getrandbits(n)
        # Add leading zeros to complte n
        binary_string = format(number, f'0{n}b')
        return binary_string
    #Genarte the entre random DNA string for the flower 
    def generate_random_dna(self):
        """Generate a random DNA sequence as a binary string."""
        size_of_center = self.generate_binary_string(4,True)  # 4-bit binary string
        color_of_center = ''.join([self.generate_binary_string(8,False) for _ in range(3)])  # 3x8-bit RGB
        color_of_petals = ''.join([self.generate_binary_string(8,False) for _ in range(3)])  # 3x8-bit RGB
        number_of_petals = self.generate_binary_string(3,False)  # 3-bit binary string

        # Combine all into a single DNA string
        return size_of_center + color_of_center + color_of_petals + number_of_petals
    
    def display(self):
        """Display the flower's characteristics based on DNA String that we decoded in the flower class."""
        print(f"Flower Characteristics:")
        print(f"  - Size of center: {self.Sizeofcenter}")
        print(f"  - Color of center (RGB): {self.Colorofcenter}")
        print(f"  - Color of petals (RGB): {self.Colorofpetals}")
        print(f"  - Number of petals: {self.Numberofpetals}")
        print(f"  - DNA (Binary): {self.dna}")

