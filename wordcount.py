import sys


path = sys.argv[1]

file = open(path)

# Create empty dictionary of word counts
word_counts = {}

# Fill in dictionary with words as keys and counts as values
for line in file:
    # tokenize line
    words = line.strip().split()

    # make all lowercase so that case is irrelevant
    words = [word.lower() for word in words]

    # traverse list of words
    for word in words:

        for ch in word:
            if ch not in "abcdefghijklmnopqrstuvwxyz":
                word = word.replace(ch, '')

        # add to dictionary if not present
        # update by adding one if present
        word_counts[word] = word_counts.get(word,0) + 1

# Print out each each word with its count
for word, count in word_counts.items():
    print(word, count)

