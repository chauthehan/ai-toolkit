import os

def rename_images(folder_path):
    # Get a list of all image files in the folder
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    images = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Sort images to maintain order
    images.sort()
    
    # Rename images sequentially
    for index, image in enumerate(images, start=1):
        ext = os.path.splitext(image)[1].lower()
        new_name = f"tok_{index}{ext}"
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        with open(folder_path + "/" + f"tok_{index}" + ".txt", "w") as f:
            f.write("")
        print(f'Renamed: {image} -> {new_name}')

if __name__ == "__main__":
    folder_path = "dataset/ban_chi_hai_2"
    rename_images(folder_path)
