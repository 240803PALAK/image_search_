import random
import os
from PIL import Image

def searchanimalname(userinput):
    animalsname = []
    with open("animals_names.txt") as names:
        for name in names.readlines():
            name=name.split('\n')
            animalsname.append(name[0])
    for animalname in animalsname:
        if str(animalname) ==str(userinput):
            return 1

def listthefiles(path):
    folder_path = f'{path}'  # Replace with the path to your folder
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Print the file names
    listfile=[]
    for file in files:
        listfile.append(file)
    # Randomly select 5 files from the list
    random_files = random.sample(listfile, 4)
    return random_files

def collage(image_files,userinput):
    # List of image files to include in the collage
    # Open and resize all images to the same size (adjust as needed)
    width, height = 400, 400  # Set the desired width and height for each image
    images = [Image.open(f'{path}/{filename}').resize((width, height)) for filename in image_files]
    # Calculate the dimensions of the collage based on the number of images
    cols = int(len(images) ** 0.5)  # Number of columns
    rows = (len(images) // cols) + (len(images) % cols)  # Number of rows
    # Create a blank canvas for the collage
    collage = Image.new('RGB', (width * cols, height * rows))
    # Paste images onto the canvas
    for i in range(len(images)):
        collage.paste(images[i], (width * (i % cols), height * (i // cols)))
    # Save or display the collage
    collage.save('collage.jpg')
    collage.show()


userinput=input("Enter the Animal name: ")
check=searchanimalname(userinput)
if check==int(1):
    path=f"animals/{userinput}"
    listfile=listthefiles(path)
    collage(listfile,path)
    print("Executed Successfully")
else:
    print("Information is not present")