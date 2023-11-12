import os
import subprocess
import time

# Get the input folder path from the user
input_folder = input("Enter the path to the input folder: ")

# Ensure the input folder exists
if not os.path.exists(input_folder):
    print(f"The specified input folder '{input_folder}' does not exist.")
    exit()

# Get the YOLO model file path from the user
model = input("Enter the path to the YOLO model file (e.g., 'best.pt'): ")

# Check if the model file exists
if not os.path.exists(model):
    print(f"The specified YOLO model file '{model}' does not exist.")
    exit()

timetrack = []

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        input_path = os.path.join(input_folder, filename)

        command = f"python ultralytics/yolo/v8/detect/predict.py model='{model}' source='{input_path}'"
        
        start_time = time.time()
        subprocess.run(command, shell=True)
        end_time = time.time()
        
        execution_time = end_time - start_time
        timetrack.append(execution_time)
        
total_time = sum(timetrack)
average = total_time / len(timetrack)
n = 0
for t in timetrack:
    print(f"Command took {t:.2f} seconds to execute for image {n}")
    n += 1
print(f"Average time for all images: {average:.2f}")
