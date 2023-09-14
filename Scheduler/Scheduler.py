#This code uses the schedule library in Python to schedule the execution of .py files at random times during the day.
#In this code, you need to replace the 'script1.py', 'script2.py', 'script3.py' with the actual names of your .py files. You can modify the start_hour and end_hour variables to define the range of hours during which the scripts can be executed.#
#The code uses the schedule library to schedule the execution of the random script at random times. It selects a random hour and minute within the specified range, and then executes a randomly chosen .py file using the subprocess.run() function.#
# The script will keep running and execute the scheduled tasks as per the defined schedule.

# Please note that you need to have the schedule library installed in your Python environment for this code to work. You can install it using pip install schedule.

import schedule
import time
import random
import subprocess
# Define a list of .py files you want to execute randomly
py_files = ['script1.py', 'script2.py', 'script3.py']

# Define the range of hours during which the scripts can be executed
start_hour = 8  # 8 AM
end_hour = 20  # 8 PM

# Function to execute a random .py file
def execute_random_script():
    script = random.choice(py_files)
    subprocess.run(['python', script])

# Schedule the execution of the random script at random times during the day
def schedule_scripts():
    while True:
        hour = random.randint(start_hour, end_hour)
        minute = random.randint(0, 59)
        schedule.every().day.at(f'{hour:02d}:{minute:02d}').do(execute_random_script)
        time.sleep(60)  # Wait for 1 minute before scheduling the next script

# Start scheduling the scripts
schedule_scripts()

# Keep the script running to execute the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

