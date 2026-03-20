# Universal Turing Machine Simulator 🖥️

A Python-based simulator for a **Universal Turing Machine (UTM)** with a real-time graphical interface built using Tkinter. This project demonstrates how a Turing Machine processes input strings step-by-step — connecting theoretical computer science with working code.

---

## What It Does

This simulator runs a **String Reversal Turing Machine** — a classic TM that takes an input string over the alphabet `{a, b}` and produces its reverse on the tape.

- Visualizes the tape, read/write head position, and current state at every step
- Accepts or rejects input based on TM transition logic
- Lets you control simulation speed in real time

---

## Demo

```
Input:   a b a b
Output:  b a b a  ✅ Accepted
```

The tape display updates live as the machine runs, with the `^` marker tracking the head position.

---

## Features

- **Step-by-step execution** — watch the TM process each symbol in real time
- **Visual tape display** — scrollable tape with head indicator
- **State tracking** — current state and step count shown at every transition
- **Speed control** — adjustable step delay (0–500ms) via slider
- **Input validation** — rejects non-alphabet characters with an error prompt
- **Edge case handling** — handles blank symbols, tape extension, and invalid transitions gracefully

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3 |
| GUI | Tkinter, ttk |
| TM Logic | Custom transition function (dict-based) |

---

## How to Run

**Requirements:** Python 3.x (Tkinter is included in the standard library — no extra installs needed)

```bash
# Clone the repo
git clone https://github.com/Rajal-ui/universal-turing-machine.git
cd universal-turing-machine

# Run the simulator
python utm.py
```

---

## How to Use

1. Enter an input string using only `a` and `b` (e.g. `abba`, `aba`, `aab`)
2. Click **Run**
3. Watch the tape and head animate step by step
4. Result shown as ✅ Accepted (with reversed string on tape) or ❌ Rejected

Use the **Step delay slider** to slow down or speed up the simulation.

---

## TM Design — String Reversal

The machine operates over alphabet `{a, b, _, X, Y, #}` with the following high-level logic:

```
q0         → Scan right to find end of input, mark with #
q1         → Pick leftmost unprocessed symbol (mark as X or Y)
q2a / q2b  → Carry symbol (a or b) past # and write to output section
q3         → Clean up markers (X, Y, #) from the tape
q4         → Scan output section
q_accept   → String successfully reversed
q_reject   → Invalid transition encountered
```

The transition table covers all symbol/state combinations including blank handling, bidirectional head movement, and chained passes over the tape.

---

## Project Structure

```
universal-turing-machine/
│
├── utm.py          # Main file — TM logic + GUI
└── README.md
```

---

## Concepts Demonstrated

- Formal definition of a Turing Machine (states, alphabet, transitions, accept/reject)
- Tape as infinite memory with dynamic extension
- Multi-pass algorithms using marker symbols
- Bridging theoretical CS (TOC/Automata) with implementation

---

## Author

**Rajal Mistry**
[GitHub](https://github.com/Rajal-ui) · [LinkedIn](https://linkedin.com/in/rajal-mistry)
