import re
from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().lower()

def get_frequencies(text):
    text = re.sub(r'[^a-z]', '', text)
    letters = Counter(text)
    bigrams = Counter(text[i:i+2] for i in range(len(text) - 1))
    trigrams = Counter(text[i:i+3] for i in range(len(text) - 2))
    return letters, bigrams, trigrams

def print_frequencies(letters, bigrams, trigrams):
    print("Letters:")
    for letter, count in letters.most_common():
        print(f"{letter}: {count}")
    
    print("\nTop 10 Bigrams:")
    for bigram, count in bigrams.most_common(10):
        print(f"{bigram}: {count}")
    
    print("\nTop 10 Trigrams:")
    for trigram, count in trigrams.most_common(10):
        print(f"{trigram}: {count}")

def analyze_text(file_path):
    text = read_file(file_path)
    letters, bigrams, trigrams = get_frequencies(text)
    print_frequencies(letters, bigrams, trigrams)

if __name__ == "__main__":
    import sys
    analyze_text(sys.argv[1])
