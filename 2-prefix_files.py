from pathlib import Path

root_dir = Path('dados')

file_paths = root_dir.iterdir()

# print(list(file_paths))

for path in file_paths:
    # print(path.stem)
    # print(path.suffix)
    new_file_name = f'new-{path.stem}{path.suffix}'
    print(new_file_name)
    
    new_file_path = path.with_name(new_file_name)
    path.rename(new_file_path)