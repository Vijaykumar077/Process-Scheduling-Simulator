# Process Scheduling Simulator

## Overview
The *Process Scheduling Simulator* is a GUI-based application built with *Tkinter* and *Matplotlib* that visually demonstrates how different CPU scheduling algorithms work. Users can input process details such as *Process ID (PID), Arrival Time, Burst Time, and Priority, select a scheduling algorithm, and visualize the execution using a **Gantt chart*.

## Features
- *User-friendly GUI* to enter process details.
- Supports four CPU scheduling algorithms:
  - *First-Come, First-Served (FCFS)*
  - *Shortest Job First (SJF)*
  - *Round Robin (RR) (Quantum = 2)*
  - *Priority Scheduling*
- *Gantt chart visualization* for execution order.
- *Dynamic process addition* before scheduling.

## Prerequisites
Make sure you have Python installed. You will also need the following libraries:

sh
pip install matplotlib


## How to Run
1. *Clone the repository* (if using Git):
   sh
   git clone https://github.com/yourusername/process-scheduling-simulator.git
   cd process-scheduling-simulator
   
2. *Run the script:*
   sh
   python scheduler.py
   

## Usage
1. *Enter process details* (PID, Arrival Time, Burst Time, and optional Priority).
2. Click *"Add Process"* to add the process to the list.
3. Select a *Scheduling Algorithm* from the dropdown menu.
4. Click *"Schedule"* to generate and display the *Gantt chart*.

## Scheduling Algorithms Implemented
### 1️⃣ First-Come, First-Served (FCFS)
- Non-preemptive.
- Processes are scheduled in order of *arrival time*.

### 2️⃣ Shortest Job First (SJF)
- Non-preemptive.
- The process with the *shortest burst time* executes first.

### 3️⃣ Round Robin (RR) (Quantum = 2)
- Preemptive.
- Each process gets a *fixed time slice* (2 units).
- If a process isn't completed, it re-enters the queue.

### 4️⃣ Priority Scheduling
- Non-preemptive.
- Processes execute based on *priority* (lower value = higher priority).

## Example
### Input
| PID | Arrival Time | Burst Time | Priority |
|-----|-------------|-----------|----------|
| P1  | 0          | 5         | 2        |
| P2  | 1          | 3         | 1        |
| P3  | 2          | 4         | 3        |

### Output (Gantt Chart Example for Priority Scheduling)

| P2 |---| P1 |----| P3 |------|
0    3    7    12


## Future Enhancements
- Add *Preemptive SJF and Priority Scheduling*.
- Allow users to *adjust quantum size* dynamically.
- Implement *real-time scheduling* algorithms.
