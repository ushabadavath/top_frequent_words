# top_frequent_words
Top Frequent Words – Data Processing
Problem Statement

Given a text file containing millions of words (one word per line), the task is to find the top 10 most frequent words and display their frequency.

Example Input
apple
banana
apple
orange
banana
apple
Example Output
apple 3
banana 2
orange 1
Approach

The program reads the input file and counts how many times each word appears.
After counting, it retrieves the top 10 words with the highest frequency.

The solution is designed to handle large datasets efficiently.

Steps followed in the program:

Open the text file.

Read the file line by line to avoid loading the entire file into memory.

Store word counts using a dictionary (hash map).

Use a heap to extract the top 10 frequent words.

Print the results sorted by frequency.

Data Structure Used
1. Dictionary (Hash Map)

A dictionary is used to store word frequencies.

word_count[word] += 1

Example:

{
 "apple": 3,
 "banana": 2,
 "orange": 1
}

Reason for using dictionary:

Fast lookup and update

Average time complexity O(1)

2. Heap (Priority Queue)

A heap is used to efficiently retrieve the top 10 most frequent words without sorting the entire dataset.

heapq.nlargest(10, word_count.items(), key=lambda x: x[1])

This improves performance compared to sorting all words.

Handling Large Files Efficiently

Since the input file may contain millions of words, the program uses the following techniques:

1. Line-by-Line File Reading
with open(file_path, 'r') as file:
    for line in file:

This prevents loading the entire file into memory.

2. Efficient Counting

A dictionary ensures quick updates when counting frequencies.

3. Efficient Top-K Retrieval

Using a heap allows retrieving the top 10 results in:

O(n log k)

Where:

n = number of unique words

k = 10

Time Complexity
Operation	Complexity
Reading file	O(n)
Counting words	O(n)
Finding top 10	O(n log 10)

Overall complexity is approximately O(n).

How to Run the Program
1. Clone the repository
git clone <your-repo-link>
cd <repo-folder>
2. Place your input file

Example file name:

words.txt
3. Run the program
python top_frequent_words.py
Output

The program prints the top 10 most frequent words and their frequencies in descending order.

Example:

apple 3
banana 2
orange 1
