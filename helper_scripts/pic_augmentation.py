import os
import random
from PIL import Image, ImageEnhance

base_dir = r"C:\Users\anuja\Desktop\Magisterka_working_data"
subdirectories = ['NORMAL', 'PNEUMONIA']

def augment_image(image):
    if random.choice([True, False]):
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    if random.choice([True, False]):
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    
    zoom_factor = random.uniform(1.0, 1.3)
    width, height = image.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
    image = image.resize((new_width, new_height), Image.LANCZOS)
    
    left = (new_width - width) // 2
    top = (new_height - height) // 2
    right = left + width
    bottom = top + height
    image = image.crop((left, top, right, bottom))
    
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(random.uniform(0.8, 1.2))
    
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(random.uniform(0.8, 1.2))
    
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(random.uniform(0.8, 1.2))
    
    return image

def augment_images_in_directory(source_dir, target_dir, num_augmented_images):
    original_images = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    original_count = len(original_images)
    
    print(f"Directory: {source_dir}")
    print(f"Original image count: {original_count}")
    
    augmented_count = 0
    
    while augmented_count < num_augmented_images:
        img_name = random.choice(original_images)
        img_path = os.path.join(source_dir, img_name)
        
        with Image.open(img_path) as img:
            augmented_img = augment_image(img)
            augmented_name = os.path.splitext(img_name)[0] + f"_augmented_{augmented_count}" + os.path.splitext(img_name)[1]
            augmented_img.save(os.path.join(target_dir, augmented_name))
            augmented_count += 1
    
    print(f"Total new augmented images created: {augmented_count}")
    print(f"Total image count after augmentation: {original_count + augmented_count}")
    print()

for i in range(1, 7):
    folder_name = f"MERGED_ALL_CLEAN_balanced_ready_{i * 1000}"
    main_dir = os.path.join(base_dir, folder_name)
    num_images_to_create = i * 1000
    
    for subdirectory in subdirectories:
        source_dir = os.path.join(main_dir, subdirectory)
        augmented_dir = os.path.join(main_dir, f"{subdirectory}_augmented")
        os.makedirs(augmented_dir, exist_ok=True)
        augment_images_in_directory(source_dir, augmented_dir, num_images_to_create)
