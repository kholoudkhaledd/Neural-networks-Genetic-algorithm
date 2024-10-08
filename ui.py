import tkinter as tk
import math
from main import generate_population,selection_elitism,crossover,mutation,calculate_fitness

fitnessint=[None]*8
population = []
fitness = [None]*8
button_clicked = 0
generation_number = 0
root = tk.Tk()
root.title("Flower Grid UI")

grid_frame = tk.Frame(root)
grid_frame.pack(padx=10, pady=10)


def draw_flower(canvas, x, y, flower):
    center_size = flower[0]
    center_color = (flower[1], flower[2], flower[3])
    petal_color = (flower[4], flower[5], flower[6])
    num_petals = flower[7]
    
    for i in range(num_petals):
        angle = math.radians(360 / num_petals * i)
        petal_x = x + 40 * math.cos(angle)
        petal_y = y + 40 * math.sin(angle)
        canvas.create_oval(petal_x - 20, petal_y - 20, petal_x + 20, petal_y + 20, fill=rgb_to_hex(petal_color))
    
    canvas.create_oval(x - center_size, y - center_size, x + center_size, y + center_size, fill=rgb_to_hex(center_color))

def on_enter(canvas, label): 
    increment_counter(label)  

def increment_counter(label):

    current_count = int(label['text'])
    label['text'] = str(current_count + 1)  
    label.after_id = label.after(100, increment_counter, label)  



def on_leave( label):
    print("ON LEAVEEE!!")
    
    for i in range (0,8):
        print(fitness[i]['text'])
    if hasattr(label, 'after_id'):
        label.after_cancel(label.after_id) 
  

def draw_grid(populationentry):
    global population
    global fitness
    global fitnessint

    cols = 8  
    for i in range(cols):
        canvas = tk.Canvas(grid_frame, width=140, height=140, bg="white", bd=2, relief="solid")
        canvas.grid(row=0, column=i, padx=5, pady=15)

        flower = population[i].dna
        draw_flower(canvas, 70, 70, flower) 

        
        label = tk.Label(canvas, text="0", font=("Arial", 14), bg="white")
        label.place(relx=0.5, rely=0.8, anchor="center")  

        label.canvas_id = canvas.winfo_id()
        
        fitness[i]=label
        


        canvas.bind("<Enter>", lambda event, c=canvas, l=label: on_enter(c, l))
        canvas.bind("<Leave>", lambda event, l=label: on_leave(l))

def on_button_click():
    global button_clicked
    global fitness
    global population
    global fitnessint
    global generation_number
    
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

        generation_number += 1
        generation_label.config(text=f"Generation: {generation_number}")

    

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb  

button = tk.Button(root, text="Generate new population", command=on_button_click)
button.pack(pady=20)

# Add a label for generation number
generation_label = tk.Label(root, text=f"Generation: {generation_number}", font=("Arial", 16))
generation_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()


# Main method 
if __name__ == "__main__":
     
     population = generate_population()
     draw_grid(population)
