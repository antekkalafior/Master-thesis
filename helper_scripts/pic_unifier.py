from PIL import Image
import os

def process_images(directory, target_size=(224, 224)):
    resized_count = 0
    converted_to_jpeg_count = 0
    converted_to_rgb_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            image = Image.open(file_path)
            
            if image.mode != 'RGB':
                image = image.convert('RGB')
                converted_to_rgb_count += 1
            
            if image.size != target_size:
                image = image.resize(target_size, Image.Resampling.LANCZOS)
                resized_count += 1

            new_file_path = os.path.splitext(file_path)[0] + '.jpeg'
            image.save(new_file_path, 'JPEG')
            

            if file_path != new_file_path:
                os.remove(file_path)
                converted_to_jpeg_count += 1
    
    return resized_count, converted_to_jpeg_count, converted_to_rgb_count


search_dir = r'C:\Users\anuja\Desktop\Magisterka\Dataset\MERGED_ALL\NORMAL'
target_size = (224, 224) 

resized, converted_to_jpeg, converted_to_rgb = process_images(search_dir, target_size)

print(f"Images resized: {resized}")
print(f"Images converted to .jpeg: {converted_to_jpeg}")
print(f"Images converted to RGB: {converted_to_rgb}")
