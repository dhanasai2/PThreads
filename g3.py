import threading
import time
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Function to simulate thread work
def task(thread_id, start_time):
    duration = random.randint(1, 5)  # Random duration between 1 and 5 seconds
    time.sleep(duration)
    end_time = datetime.now()
    print(f"Thread {thread_id} started at {start_time} and ended at {end_time}")
    gantt_data.append((thread_id, start_time, end_time))

# Data for Gantt chart
gantt_data = []

# Create and start threads
threads = []
for i in range(5):  # 5 threads
    start_time = datetime.now()
    thread = threading.Thread(target=task, args=(i, start_time))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Plot Gantt chart
fig, ax = plt.subplots()
for i, (thread_id, start, end) in enumerate(gantt_data):
    ax.barh(thread_id, end - start, left=start, color=f'C{i}', label=f'Thread {thread_id}')

# Formatting the chart
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax.xaxis.set_major_locator(mdates.SecondLocator(interval=1))
plt.xlabel('Time')
plt.ylabel('Threads')
plt.title('Gantt Chart for Threads with Random Durations')
plt.legend()
plt.grid(True)
plt.show()
