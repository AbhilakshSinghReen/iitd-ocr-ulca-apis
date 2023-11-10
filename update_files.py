import os
import json
import gdown

files_json_path = os.path.join(os.path.dirname(__file__), "files.json")
files_root_dir = os.path.join(os.path.dirname(__file__), "files")

def try_read_json_file(file_path, default_value = {}):
    try:
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
        return json_data
    except:
        return default_value

def download_file(file_dict):
    file_url = file_dict['url']
    output_path = os.path.join(files_root_dir, file_dict['name'])
    gdown.download(file_url, output_path, quiet=False)


if __name__ == "__main__":
    files = try_read_json_file(files_json_path)

    all_latest_file_paths = []

    for file in files:
        if file['downloadLocation'] != "":
            target_file_path = os.path.join(files_root_dir, file['downloadLocation'], file['name'])
        else:
            target_file_path = os.path.join(files_root_dir, file['name'])
        
        all_latest_file_paths.append(target_file_path)
        
        if os.path.exists(target_file_path): # check if file is already there
            continue
        
        print(f"Downloading new file: {file['name']}")
        download_file(file)
    
    all_latest_file_paths = set(all_latest_file_paths)
    
    # Delete outdated files
    all_files = os.listdir(files_root_dir)
    all_files.remove(".gitkeep")
    all_files = [os.path.join(files_root_dir, file) for file in all_files]
    all_files = set(all_files)

    files_to_delete = list(all_files - all_latest_file_paths)
    for file_to_delete in files_to_delete:
        file_name = os.path.basename(file_to_delete)
        try:
            os.remove(file_to_delete)
            print(f"Deleted outdated file: {file_name}")
        except OSError as e:
            print(f"Error deleting outdated file: {file_name}: {e}")
    