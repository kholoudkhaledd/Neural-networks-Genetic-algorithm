import tkinter as tk
from tkinter import Button
import math

# Function to draw a flower in a given canvas
def draw_flower(canvas, x, y, petal_radius=30, center_radius=20):
    # Draw petals
    for i in range(7):
        angle = i * (360 / 7)  # Divide the circle into 7 equal parts
        petal_x = x + petal_radius * math.cos(math.radians(angle))
        petal_y = y + petal_radius * math.sin(math.radians(angle))
        canvas.create_oval(petal_x - 15, petal_y - 15, petal_x + 15, petal_y + 15, fill="pink", outline="black")

    # Draw the center of the flower
    canvas.create_oval(x - center_radius, y - center_radius, x + center_radius, y + center_radius, fill="yellow", outline="black")

# Create the root window
window = tk.Tk()
window.title("Genetic Algorithm For Flowers")
window.geometry("1200x400")  # Adjusted width for better visibility

# Button for evolving new generations
button = Button(window, text="Evolve New Generations")
button.grid(row=0, columnspan=8, pady=(5, 10))  # Button in row 0, spans all columns

# Create a grid with 1 row and 8 columns for flower frames starting from row 1
for i in range(1):  # Only one row for flowers
    for j in range(8):  # Eight columns
        frame = tk.Frame(window, borderwidth=2, width=150, height=300, bg="white")
        frame.grid(row=1, column=j, padx=15, pady=20)  # Start placing frames from row 1

        # Create a canvas in each frame
        canvas = tk.Canvas(frame, bg="white", width=150, height=300)
        canvas.pack(expand=True)

        # Draw a flower in the canvas
        draw_flower(canvas, 75, 150)  # Center the flower in the canvas

# Start the GUI event loop
window.mainloop()


# Main method 
if __name__ == "__main__":
    draw_flower()