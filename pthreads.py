import threading

# Number of threads to create
NUM_THREADS = 5

# Function that will be executed by each thread
def print_message(thread_id):
    print(f"Hello from thread {thread_id}!")

# Create and start threads
threads = []
for i in range(NUM_THREADS):
    thread = threading.Thread(target=print_message, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed execution.")
