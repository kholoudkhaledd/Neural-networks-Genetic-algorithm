import tkinter as tk
import math

fitness = []

# Create the main window
root = tk.Tk()
root.title("Flower Grid UI")

# Set up a frame for the flower grid
grid_frame = tk.Frame(root)
grid_frame.pack(padx=10, pady=10)

# Function to draw a static flower (simple circles for petals)
def draw_flower(canvas, x, y):
    # Draw petals (circles)
    for i in range(7):
        angle = math.radians(360 / 7 * i)
        petal_x = x + 40 * math.cos(angle)
        petal_y = y + 40 * math.sin(angle)
        canvas.create_oval(petal_x - 20, petal_y - 20, petal_x + 20, petal_y + 20, fill="purple")
    
    # Draw the center of the flower
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="orange")

# Function to handle mouse entering a canvas
def on_enter(canvas, label): 
    increment_counter(label)  # Start counting

# Recursive function to increment the counter
def increment_counter(label):
    current_count = int(label['text'])
    label['text'] = str(current_count + 1)  # Increment the label text
    label.after_id = label.after(100, increment_counter, label)  # Repeat every 1000ms (1 second)
    for i in range (0,len(fitness)):
        if(label== fitness[i]):
            fitness[i]['text'] = label['text']



# Function to handle mouse leaving a canvas
def on_leave( label):
    print("ON LEAVEEE!!")
    print("fitness:",fitness)
    if hasattr(label, 'after_id'):
        label.after_cancel(label.after_id) 
    # Optionally, you can keep the last counted value or reset it
    # You can do nothing or set a specific behavior here

# Create a grid of 1 row and 8 columns with static flower drawings
cols = 8  # 1 row and 8 columns for the grid
for col in range(cols):
    # Create a canvas for each box in the grid
    canvas = tk.Canvas(grid_frame, width=140, height=140, bg="white", bd=2, relief="solid")
    canvas.grid(row=0, column=col, padx=5, pady=5)

    # Draw a static flower on the canvas
    draw_flower(canvas, 70, 70)  # Center the flower at (70, 70)

    # Create a label to display the counter
    label = tk.Label(canvas, text="0", font=("Arial", 14), bg="white")
    fitness.append(label)
    label.place(relx=0.5, rely=0.8, anchor="center")  # Center the label below the flower

    # Bind mouse enter and leave events
    canvas.bind("<Enter>", lambda event, c=canvas, l=label: on_enter(c, l))
    canvas.bind("<Leave>", lambda event, l=label: on_leave(l))

# Add a button below the grid
def on_button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()


# Main method 
if __name__ == "__main__":
    draw_flower()