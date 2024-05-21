import os
import shutil
import argparse
# debug only
from collections import namedtuple 

def parse_args():
    parser = argparse.ArgumentParser(description='Рекурсивно копіює файли.')
    parser.add_argument('source_dir', help='Шлях до директорії для копіювання.')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до цільової директорії (за умовчанням "dist").')
    return parser.parse_args()

# debug
# def parse_args():
#     Args = namedtuple('parseargs', ['source_dir', 'dest_dir']) 
#     arg = Args('D:\git\GoIT-HW\goit-algo-hw-03\source_bob', 'D:\git\GoIT-HW\goit-algo-hw-03\dist')
#     return  arg

def copy_files_recursively(source_dir, dest_dir):
    
    try:
        for item in os.listdir(source_dir):
            
            item_path = os.path.join(source_dir, item)
            
            if os.path.isdir(item_path):
            
                new_dir_name = item_path.split(os.sep)[-1]
                new_path_dir = os.path.join(dest_dir, new_dir_name)
                os.makedirs(new_path_dir, exist_ok=True)
            
                copy_files_recursively(item_path, new_path_dir)
            else:
            
                file_ext = os.path.splitext(item)[1][1:].lower()
            
                if file_ext:
                    ext_dir = os.path.join(dest_dir, file_ext)
                    os.makedirs(ext_dir, exist_ok=True)
                    shutil.copy2(item_path, os.path.join(ext_dir, item))
    except Exception as e:
        print(f"Помилка обробки директорії {source_dir}: {e}")

def main():
    args = parse_args()
    source_dir = args.source_dir
    dest_dir = args.dest_dir

    print("Директорія до копіювання: ", source_dir)
    print("Цільова директорія: ", dest_dir)

    if not os.path.isdir(source_dir):
        print(f"Директорія {source_dir} не існує.")
        return

    os.makedirs(dest_dir, exist_ok=True)
    copy_files_recursively(source_dir, dest_dir)

if __name__ == "__main__":
    main()
