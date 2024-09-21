import cv2
from matplotlib import pyplot as plt
import os


def imshow(cv2_array):
    image_rgb = cv2.cvtColor(cv2_array, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off') 
    plt.show()

def split_image(image_path):
    # Load the image, channel_1: cv2.IMREAD_GRAYSCALE
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    else:
        print(f"image_shape: {image.shape}")
        height, width = image.shape
    # Cut the image in the vertical direction
    top_half, bottom_half = image[0:height//2, :], image[height//2:, :]
    return top_half, bottom_half

def crop_to_content(img):
    # Find non-zero (i.e., non-white) pixels
    coords = cv2.findNonZero(255 - img)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        return img[y:y+h, x:x+w]
    else:
        return img  

def split_problem_solution(problems_set_path, chapter_num):
    chapter_num = str(chapter_num)
    directory_path = os.path.join(problems_set_path, "_"+chapter_num)
    print(directory_path)
    image_names = [file for file in os.listdir(directory_path) if file.lower().endswith(image_extensions)]
    image_paths = [os.path.join(directory_path,image_name) for image_name in image_names]
    output_directory = os.path.join(problems_set_path, "_"+chapter_num+"_split") 
    os.makedirs(output_directory, exist_ok=True)  
    for image_path, image_name in zip(image_paths,image_names):
        extracted_name = os.path.splitext(image_name)[0]
        top_half, bottom_half = split_image(image_path)
        top_half_cropped = crop_to_content(top_half)
        bottom_half_cropped = crop_to_content(bottom_half)
        top_half_cropped_path = os.path.join(output_directory, f"{extracted_name}_problem.jpg")
        bottom_half_cropped_path = os.path.join(output_directory, f"{extracted_name}_solution.jpg")
        cv2.imwrite(top_half_cropped_path, top_half_cropped)
        cv2.imwrite(bottom_half_cropped_path, bottom_half_cropped)
    print(f"Chapter{chapter_num}_Split_Complete")
        
image_extensions = ('.jpg', '.jpeg', '.png')
problems_set_path = ".\database\problems_set"
chapter_num = 45
split_problem_solution(problems_set_path, chapter_num)