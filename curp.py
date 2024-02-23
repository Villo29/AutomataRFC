import tkinter as tk

class Curp:
    def __init__(self, root):
        self.Letters = ["R", "U", "G", "J"]
        self.input = tk.StringVar()
        self.input.trace_add("write", self.handle_input_change)

        root.title("AUTOMATA CURP/RFC")
        root.geometry("800x400")

        label = tk.Label(root, text="Ingresa la cadena 'RUGJ'")
        label.pack(pady=10)

        entry = tk.Entry(root, textvariable=self.input)
        entry.pack(pady=10)

        self.canvas = tk.Canvas(root, bg="white", width=800, height=200)
        self.canvas.pack()

    def handle_input_change(self, *args):
        value = self.input.get().upper()
        if len(value) <= 4 and all(char in self.Letters for char in value) and value.startswith('R'):
            self.draw_states_and_arrows(value)

    def draw_states_and_arrows(self, input_str):
        self.canvas.delete("all")
        num_states = min(5, len(input_str) + 1)
        state_radius = 30
        state_x = 100
        state_y = 100
        state_distance = 150

        for i in range(num_states):
            self.canvas.create_oval(state_x, state_y, state_x + 2*state_radius, state_y + 2*state_radius, outline="black", fill="lightgreen")
            self.canvas.create_text(state_x + state_radius, state_y + state_radius, text=f"q{i}", fill="black", font=("Arial", 14))

            if i < num_states - 1:
                self.canvas.create_line(state_x + 2*state_radius, state_y + state_radius, state_x + 2*state_radius + state_distance, state_y + state_radius, fill="green", width=2, arrow=tk.LAST)
                self.canvas.create_text(state_x + 2*state_radius + state_distance//2, state_y + state_radius - 20, text=input_str[i].upper(), fill="white", font=("Arial", 14))
                # Agregar letra en la flecha
                self.canvas.create_text(state_x + 2*state_radius + state_distance//2, state_y + state_radius + 20, text=input_str[i].upper(), fill="black", font=("Arial", 14))

            state_x += state_distance

if __name__ == "__main__":
    root = tk.Tk()
    app = Curp(root)
    root.mainloop()