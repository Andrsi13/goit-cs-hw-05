import os
import random
import string

def create_test_files(base_path: str, num_files: int, num_folders: int):
    os.makedirs(base_path, exist_ok=True)

    extensions = ['txt', 'pdf', 'jpg', 'png', 'docx', 'xlsx']
    
    for i in range(num_folders):
        folder_name = ''.join(random.choices(string.ascii_letters, k=8))
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for j in range(num_files):
            ext = random.choice(extensions)
            file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '.' + ext
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'w') as f:
                f.write('This is a test file.')

def main():
    base_path = 'test_source'
    num_files = 10  # Number of files in each folder
    num_folders = 5  # Number of folders to create

    create_test_files(base_path, num_files, num_folders)
    print(f"Created {num_folders} folders with {num_files} files each in {base_path}")

if __name__ == "__main__":
    main()
