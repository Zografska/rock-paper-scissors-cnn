import os
import shutil
import random

def split_dataset(source_dir, output_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1, seed=42):
    random.seed(seed)
    
    classes = os.listdir(source_dir)
    
    for label in classes:
        label_path = os.path.join(source_dir, label)

        images = os.listdir(label_path)
        random.shuffle(images)

        total_number = len(images)
        training_length = int(train_ratio * total_number)
        validation_length = int(val_ratio * total_number)

        train_files = images[:training_length]
        validation_files = images[training_length:training_length + validation_length]
        test_files = images[training_length + validation_length:]

        for subset, files in zip(["train", "validation", "test"], [train_files, validation_files, test_files]):
            subset_label_path = os.path.join(output_dir, subset, label)
            os.makedirs(subset_label_path, exist_ok=True)
            for f in files:
                shutil.copy(os.path.join(label_path, f), os.path.join(subset_label_path, f))


split_dataset(
    source_dir="data",
    output_dir="data_reconstructed",
    seed=17,
    train_ratio=0.7,
    val_ratio=0.2,
    test_ratio=0.1
)
