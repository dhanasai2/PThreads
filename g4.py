import threading
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Function to simulate thread work
def task(thread_id, start_time, priority):
    duration = priority  # Higher priority threads have shorter durations
    time.sleep(duration)
    end_time = datetime.now()
    print(f"Thread {thread_id} (Priority {priority}) started at {start_time} and ended at {end_time}")
    gantt_data.append((thread_id, start_time, end_time, priority))

# Data for Gantt chart
gantt_data = []

# Create and start threads
threads = []
priorities = [1, 2, 3, 4]  # Lower number means higher priority
for i, priority in enumerate(priorities):
    start_time = datetime.now()
    thread = threading.Thread(target=task, args=(i, start_time, priority))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Plot Gantt chart
fig, ax = plt.subplots()
for i, (thread_id, start, end, priority) in enumerate(gantt_data):
    ax.barh(thread_id, end - start, left=start, color=f'C{i}', label=f'Thread {thread_id} (Priority {priority})')

# Formatting the chart
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax.xaxis.set_major_locator(mdates.SecondLocator(interval=1))
plt.xlabel('Time')
plt.ylabel('Threads')
plt.title('Gantt Chart with Thread Priority Simulation')
plt.legend()
plt.grid(True)
plt.show()
