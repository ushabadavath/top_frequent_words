from collections import defaultdict
import heapq

def top_frequent_words(file_path, top_n=10):
    # Dictionary to store word frequencies
    word_count = defaultdict(int)

    # Read the file line by line (efficient for large files)
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                word_count[word] += 1

    # Get top N frequent words using a heap
    top_words = heapq.nlargest(top_n, word_count.items(), key=lambda x: x[1])

    # Print results sorted by frequency
    for word, freq in top_words:
        print(f"{word} {freq}")


# Example usage
if __name__ == "__main__":
    file_path = "words.txt"   # input file
    top_frequent_words(file_path)