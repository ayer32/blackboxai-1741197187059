import schedule
import time
import threading

def run_task(task):
    """Run the scheduled task."""
    task()

def schedule_task(task, interval):
    """Schedule a task to run at a specified interval."""
    schedule.every(interval).seconds.do(run_task, task)

    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler(task, interval):
    """Start the task scheduler in a separate thread."""
    scheduler_thread = threading.Thread(target=schedule_task, args=(task, interval))
    scheduler_thread.start()
    return "Task scheduled successfully."

# Example usage
if __name__ == "__main__":
    def example_task():
        print("Task executed!")

    start_scheduler(example_task, 10)  # Schedule example_task to run every 10 seconds
