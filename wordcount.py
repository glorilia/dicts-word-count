# put your code here.
path = 'test.txt'

file = open(path)

# Create empty dictionary of word counts
word_counts = {}

# Fill in dictionary with words as keys and counts as values
for line in file:
    # tokenize line
    words = line.strip().split()

    # traverse list
    for word in words:
        # add to dictionary if not present
        # update by adding one if present
        word_counts[word] = word_counts.get(word,0) + 1

# Print out each each word with its count
for word, count in word_counts.items():
    print(word, count)

