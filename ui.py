import tkinter as tk
import math
# from utils import calculate_fitness
from main import generate_population,selection_elitism,crossover,mutation,calculate_fitness
fitnessint=[None]*8
population = []
fitness = [None]*8
button_clicked = 0
# Create the main window
root = tk.Tk()
root.title("Flower Grid UI")

# Set up a frame for the flower grid
grid_frame = tk.Frame(root)
grid_frame.pack(padx=10, pady=10)

# Function to draw a static flower (simple circles for petals)
def draw_flower(canvas, x, y, flower):
    # Draw petals (circles)
     
    for i in range(flower[7]):
        angle = math.radians(360 / 7 * i)
        petal_x = x + 40 * math.cos(angle)
        petal_y = y + 40 * math.sin(angle)
        canvas.create_oval(petal_x - 20, petal_y - 20, petal_x + 20, petal_y + 20, fill=rgb_to_hex((flower[4],flower[5],flower[6])))
    
    # Draw the center of the flower
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill=rgb_to_hex((flower[1],flower[2],flower[3])))

# Function to handle mouse entering a canvas
def on_enter(canvas, label): 
    print(canvas)
    print(label)
    increment_counter(label)  # Start counting

# Recursive function to increment the counter
def increment_counter(label):

    current_count = int(label['text'])
    label['text'] = str(current_count + 1)  # Increment the label text
    label.after_id = label.after(100, increment_counter, label)  # Repeat every 1000ms (1 second)




# Function to handle mouse leaving a canvas
def on_leave( label):
    print("ON LEAVEEE!!")
    
    for i in range (0,8):
        print(fitness[i]['text'])
    if hasattr(label, 'after_id'):
        label.after_cancel(label.after_id) 
    # Optionally, you can keep the last counted value or reset it
    # You can do nothing or set a specific behavior here

def draw_grid(populationentry):
    global population
    global fitness
    global fitnessint
        # Create a grid of 1 row and 8 columns with static flower drawings
    cols = 8  # 1 row and 8 columns for the grid
    for i in range(cols):
        # Create a canvas for each box in the grid
        canvas = tk.Canvas(grid_frame, width=140, height=140, bg="white", bd=2, relief="solid")
        canvas.grid(row=0, column=i, padx=5, pady=15)

        # Draw a static flower on the canvas
        print("Population:" ,population)
        flower = population[i].dna
        draw_flower(canvas, 70, 70, flower)  # Center the flower at (70, 70)

        # Create a label to display the counter
        label = tk.Label(canvas, text="0", font=("Arial", 14), bg="white")
        label.place(relx=0.5, rely=0.8, anchor="center")  # Center the label below the flower

        label.canvas_id = canvas.winfo_id()
        
        fitness[i]=label
        # Store the label in fitness list

        # Bind mouse enter and leave events
        canvas.bind("<Enter>", lambda event, c=canvas, l=label: on_enter(c, l))
        canvas.bind("<Leave>", lambda event, l=label: on_leave(l))
# Add a button below the grid
def on_button_click():
    global button_clicked
    global fitness
    global population
    global fitnessint
    
    if button_clicked == 0:
        # First population generation
        population = generate_population()
        button_clicked += 1
        draw_grid(population)
    else:
        for i in range (8):
            fitnessint[i]=int(fitness[i]['text']) 
    
        
        sorted_population = calculate_fitness(fitnessint,population)
        selected_population = selection_elitism(sorted_population)
        crossedover_population = crossover(selected_population)
        mutated_population = mutation(crossedover_population)
        draw_grid(mutated_population)
        population = mutated_population  # Update the global population

    

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb  

button = tk.Button(root, text="Generate new population", command=on_button_click)
button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()


# Main method 
if __name__ == "__main__":
     
     population = generate_population()
     print("pop:",population)

     draw_grid(population)
