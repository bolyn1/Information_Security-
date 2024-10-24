
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_text(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
