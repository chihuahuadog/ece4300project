from PIL import Image, ImageEnhance
import os

# Get the input folder path from the user
input_folder = input("Enter the path to the input folder: ")

# Ensure the input folder exists
if not os.path.exists(input_folder):
    print(f"The specified input folder '{input_folder}' does not exist.")
    exit()

# Get the output folder path from the user
output_folder = input("Enter the path to the output folder: ")

# Ensure the output folder exists, or create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the brightness factor from the user
brightness_factor = float(input("Enter the brightness factor (e.g., 1.5 for increased brightness): "))

# List all files in the input folder
files = os.listdir(input_folder)

for file in files:
    if file.endswith((".jpg", ".jpeg", ".png", ".bmp")):
        # Open the image
        image = Image.open(os.path.join(input_folder, file))

        # Apply brightness adjustment
        enhancer = ImageEnhance.Brightness(image)
        brightened_image = enhancer.enhance(brightness_factor)

        # Save the adjusted image to the output folder
        output_file = os.path.join(output_folder, file)
        brightened_image.save(output_file)

print("Brightness adjustment complete.")
