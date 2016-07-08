def get_file_contents(file_path):
    with open(file_path, 'r') as content:
        return content.read()
