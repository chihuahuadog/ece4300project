import os
import subprocess
import time

model = 'best.pt'
input_folder = '/home/cat/Desktop/ece4300projectYolo5/tankPhotos'
timetrack = []

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        input_path = os.path.join(input_folder, filename)

        command = f"python detect.py --weights best.pt --img 416 --conf 0.1 --source {input_folder}"
        
        start_time = time.time()
        subprocess.run(command, shell=True)
        end_time = time.time()
        
        execution_time = end_time - start_time
        timetrack.append(execution_time)
        
total_time = sum(timetrack);
average = total_time/len(timetrack)
n = 0
for t in timetrack:
   print(f"Command took {t:.2f} seconds to execute for image {n}")
   n+=1
print(f"Average time for all images: {average:.2f}")
        
