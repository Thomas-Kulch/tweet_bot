# Function to load words from a file
def load_words(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words


def save_words(file_path, words):
    with open(file_path, 'w') as file:
        for word in words:
            file.write(f"{word}\n")
