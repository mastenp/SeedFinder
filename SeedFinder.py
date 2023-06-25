import os

def search_files(directory, extensions):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in extensions):
                files.append(os.path.join(root, filename))
    return files

def search_words_in_files(files, words):
    found_files = []
    for file in files:
        with open(file, 'r') as f:
            content = f.read().lower()
            word_count = 0
            for word in words:
                if word.lower() in content:
                    word_count += 1
                if word_count >= 9:
                    found_files.append(file)
                    break
    return found_files

directory = "path/to/directory"  # Specify the directory to search in
extensions = ['.txt', '.csv', '.xls', '.xlsx', '.doc', '.docx']
words_to_search = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9']

found_files = search_files(directory, extensions)
matched_files = search_words_in_files(found_files, words_to_search)

if matched_files:
    print("Matched files:")
    for file in matched_files:
        print(file)
else:
    print("No files matched the search criteria.")
