import tkinter as tk
from tkinter import ttk, messagebox

class UniversalTuringMachine:
    def __init__(self, tm_description, tape_input):
        self.blank = tm_description['blank']
        self.state = tm_description['start_state']
        self.accept_state = tm_description['accept_state']
        self.reject_state = tm_description['reject_state']
        self.transitions = tm_description['transitions']
        self.tape = [self.blank] * 5 + tape_input + [self.blank] * 5
        self.head = 5
        self.steps = 0

    def step(self):
        symbol = self.tape[self.head]
        key = (self.state, symbol)
        if key not in self.transitions:
            self.state = self.reject_state
            return
        new_state, new_symbol, direction = self.transitions[key]
        self.tape[self.head] = new_symbol
        self.state = new_state
        if direction == 'R':
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append(self.blank)
        elif direction == 'L':
            self.head -= 1
            if self.head < 0:
                self.tape.insert(0, self.blank)
                self.head = 0
        self.steps += 1

string_reversal_tm = {
    "blank": "_",
    "start_state": "q0",
    "accept_state": "q_accept",
    "reject_state": "q_reject",
    "transitions": {
        ("q0", "a"): ("q0", "a", "R"),
        ("q0", "b"): ("q0", "b", "R"),
        ("q0", "_"): ("q1", "#", "L"),

        ("q1", "a"): ("q2a", "X", "R"),
        ("q1", "b"): ("q2b", "Y", "R"),
        ("q1", "X"): ("q1", "X", "L"),
        ("q1", "Y"): ("q1", "Y", "L"),
        ("q1", "_"): ("q3", "_", "R"),

        ("q2a", "a"): ("q2a", "a", "R"),
        ("q2a", "b"): ("q2a", "b", "R"),
        ("q2a", "X"): ("q2a", "X", "R"),
        ("q2a", "Y"): ("q2a", "Y", "R"),
        ("q2a", "#"): ("q2a_to_out", "#", "R"),

        ("q2a_to_out", "a"): ("q2a_to_out", "a", "R"),
        ("q2a_to_out", "b"): ("q2a_to_out", "b", "R"),
        ("q2a_to_out", "_"): ("q2a_back", "a", "L"),

        ("q2a_back", "a"): ("q2a_back", "a", "L"),
        ("q2a_back", "b"): ("q2a_back", "b", "L"),
        ("q2a_back", "_"): ("q2a_back", "_", "L"),
        ("q2a_back", "#"): ("q1", "#", "L"),

        ("q2b", "a"): ("q2b", "a", "R"),
        ("q2b", "b"): ("q2b", "b", "R"),
        ("q2b", "X"): ("q2b", "X", "R"),
        ("q2b", "Y"): ("q2b", "Y", "R"),
        ("q2b", "#"): ("q2b_to_out", "#", "R"),

        ("q2b_to_out", "a"): ("q2b_to_out", "a", "R"),
        ("q2b_to_out", "b"): ("q2b_to_out", "b", "R"),
        ("q2b_to_out", "_"): ("q2b_back", "b", "L"),

        ("q2b_back", "a"): ("q2b_back", "a", "L"),
        ("q2b_back", "b"): ("q2b_back", "b", "L"),
        ("q2b_back", "_"): ("q2b_back", "_", "L"),
        ("q2b_back", "#"): ("q1", "#", "L"),

        ("q3", "X"): ("q3", "_", "R"),
        ("q3", "Y"): ("q3", "_", "R"),
        ("q3", "a"): ("q3", "a", "R"),
        ("q3", "b"): ("q3", "b", "R"),
        ("q3", "#"): ("q4", "_", "R"),

        ("q4", "a"): ("q4", "a", "R"),
        ("q4", "b"): ("q4", "b", "R"),
        ("q4", "_"): ("q_accept", "_", "R")
    }
}

class UTMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Turing Machine - String Reversal")
        self.root.geometry("800x400")
        self.root.minsize(700, 350)

        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 11))
        style.configure("Result.TLabel", font=("Segoe UI", 14, "bold"))

        self.tm_description = string_reversal_tm

        # Input frame
        input_frame = ttk.Frame(root, padding=10)
        input_frame.pack(fill="x")
        ttk.Label(input_frame, text="Enter input over {a,b}:").pack(side="left", padx=(0, 10))
        self.input_entry = ttk.Entry(input_frame, font=("Consolas", 14), width=30)
        self.input_entry.pack(side="left", padx=(0, 10))
        ttk.Button(input_frame, text="Run", command=self.run_tm).pack(side="left")

        # Tape display
        self.tape_display = tk.Text(root, height=4, font=("Consolas", 14), bg="#f4f4f4", wrap="none")
        self.tape_display.pack(fill="x", padx=10, pady=10)

        # Result label
        self.result_label = ttk.Label(root, text="", style="Result.TLabel")
        self.result_label.pack(pady=5)

        # Status bar
        self.status_label = ttk.Label(root, text="State: - | Steps: 0", anchor="w")
        self.status_label.pack(fill="x", side="bottom", padx=5, pady=5)

        # Speed control
        speed_frame = ttk.Frame(root, padding=5)
        speed_frame.pack()
        ttk.Label(speed_frame, text="Step delay (ms):").pack(side="left")
        self.delay_var = tk.IntVar(value=80)
        ttk.Scale(speed_frame, from_=0, to=500, orient="horizontal",
                  variable=self.delay_var, length=200).pack(side="left", padx=5)

    def run_tm(self):
        tape_input = list(self.input_entry.get().strip())
        if any(ch not in {"a", "b"} for ch in tape_input):
            messagebox.showerror("Error", "Input must contain only 'a' and 'b'.")
            return

        utm = UniversalTuringMachine(self.tm_description, tape_input)
        self.update_display(utm)

        while utm.state not in {utm.accept_state, utm.reject_state}:
            utm.step()
            self.update_display(utm)
            self.root.update()
            self.root.after(self.delay_var.get())

        if utm.state == utm.accept_state:
            self.result_label.config(text="✅ Accepted (reversed string on tape)", foreground="green")
        else:
            self.result_label.config(text="❌ Rejected", foreground="red")

    def update_display(self, utm):
        left = max(0, utm.head - 30)
        right = min(len(utm.tape), utm.head + 31)
        segment = utm.tape[left:right]
        tape_str = ''.join(segment)
        head_pos = utm.head - left
        head_indicator = ' ' * head_pos + '^'

        self.tape_display.delete("1.0", tk.END)
        self.tape_display.insert(tk.END, tape_str + "\n" + head_indicator)
        self.status_label.config(text=f"State: {utm.state} | Steps: {utm.steps}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UTMGUI(root)
    root.mainloop()