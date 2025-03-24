import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time, schedule = 0, []
    for p in processes:
        if time < p[1]:
            time = p[1]
        schedule.append((p[0], time, time + p[2]))
        time += p[2]
    return schedule

def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
    time, schedule, remaining = 0, [], processes[:]
    while remaining:
        available = [p for p in remaining if p[1] <= time]
        if not available:
            time = remaining[0][1]
            available = [remaining[0]]
        p = min(available, key=lambda x: x[2])
        schedule.append((p[0], time, time + p[2]))
        time += p[2]
        remaining.remove(p)
    return schedule

def round_robin_scheduling(processes, quantum=2):
    queue, time, schedule = processes[:], 0, []
    while queue:
        pid, arrival, burst = queue.pop(0)
        if time < arrival:
            time = arrival
        executed = min(burst, quantum)
        schedule.append((pid, time, time + executed))
        time += executed
        if burst > quantum:
            queue.append((pid, time, burst - quantum))
    return schedule

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[3], x[1]))  # Sort by priority, then arrival time
    time, schedule = 0, []
    for p in processes:
        if time < p[1]:
            time = p[1]
        schedule.append((p[0], time, time + p[2]))
        time += p[2]
    return schedule

def draw_gantt_chart(schedule):
    fig, ax = plt.subplots()
    yticks, ylabels = [], []
    for i, (pid, start, end) in enumerate(schedule):
        ax.barh(i, end - start, left=start, height=0.5)
        ax.text((start + end) / 2, i, f'P{pid}', ha='center', va='center', color='white', fontsize=12)
        yticks.append(i)
        ylabels.append(f'P{pid}')
    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels)
    ax.set_xlabel("Time")
    ax.set_title("Gantt Chart")
    return fig

def schedule_processes():
    try:
        processes = []
        for item in process_list.get_children():
            values = process_list.item(item, "values")
            pid, arrival, burst = int(values[0]), int(values[1]), int(values[2])
            priority = int(values[3]) if len(values) > 3 else 0
            processes.append((pid, arrival, burst, priority))
        
        if not processes:
            messagebox.showwarning("Warning", "No processes added!")
            return
        
        algorithm = algo_var.get()
        if algorithm == "FCFS":
            schedule = fcfs_scheduling(processes)
        elif algorithm == "SJF":
            schedule = sjf_scheduling(processes)
        elif algorithm == "Round Robin":
            schedule = round_robin_scheduling(processes, quantum=2)
        elif algorithm == "Priority":
            schedule = priority_scheduling(processes)
        else:
            messagebox.showerror("Error", "Invalid Scheduling Algorithm!")
            return
        
        gantt_chart = draw_gantt_chart(schedule)
        
        canvas = FigureCanvasTkAgg(gantt_chart, master=graph_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_process():
    try:
        pid = int(entry_pid.get())
        arrival = int(entry_arrival.get())
        burst = int(entry_burst.get())
        priority = int(entry_priority.get()) if entry_priority.get() else 0
        process_list.insert("", "end", values=(pid, arrival, burst, priority))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers only.")

root = tk.Tk()
root.title("Process Scheduling Simulator")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="PID").grid(row=0, column=0)
tk.Label(frame, text="Arrival Time").grid(row=0, column=1)
tk.Label(frame, text="Burst Time").grid(row=0, column=2)
tk.Label(frame, text="Priority (Optional)").grid(row=0, column=3)

entry_pid = tk.Entry(frame, width=5)
entry_pid.grid(row=1, column=0)
entry_arrival = tk.Entry(frame, width=5)
entry_arrival.grid(row=1, column=1)
entry_burst = tk.Entry(frame, width=5)
entry_burst.grid(row=1, column=2)
entry_priority = tk.Entry(frame, width=5)
entry_priority.grid(row=1, column=3)

tk.Button(frame, text="Add Process", command=add_process).grid(row=1, column=4)

process_list = ttk.Treeview(root, columns=("PID", "Arrival Time", "Burst Time", "Priority"), show="headings")
for col in ("PID", "Arrival Time", "Burst Time", "Priority"):
    process_list.heading(col, text=col)
process_list.pack()

algo_var = tk.StringVar()
algo_var.set("FCFS")
tk.Label(root, text="Select Scheduling Algorithm:").pack()
tk.OptionMenu(root, algo_var, "FCFS", "SJF", "Round Robin", "Priority").pack()

tk.Button(root, text="Schedule", command=schedule_processes).pack(pady=5)

graph_frame = tk.Frame(root)
graph_frame.pack()

root.mainloop()
