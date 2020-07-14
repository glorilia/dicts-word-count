import sys
from collections import Counter


path = sys.argv[1]

file = open(path)


# Create empty list for all words
all_words = []

# Add words to list
for line in file:
    # tokenize line
    raw_words = line.strip().split()

    # make all lowercase so that case is irrelevant
    lower_words = [word.lower() for word in raw_words]

    for word in lower_words:
        # replace non-letters with ''
        for ch in word:
            if ch not in "abcdefghijklmnopqrstuvwxyz":
                word = word.replace(ch, '')

        all_words.append(word)

# Make counter to make a Counter dictionary
word_counts = Counter(all_words)
alpha_words = sorted(word_counts)
by_count_words = sorted(alpha_words, key=word_counts.__getitem__, reverse=True)

# Print out each each word with its count
for word in by_count_words:
    print(word, word_counts[word])



# Code without using the Counter object

# Create empty dictionary of word counts
# word_counts = {}

    # # traverse list of words
    # for word in words:

    #     for ch in word:
    #         if ch not in "abcdefghijklmnopqrstuvwxyz":
    #             word = word.replace(ch, '')

    #     # add to dictionary if not present
    #     # update by adding one if present
    #     word_counts[word] = word_counts.get(word,0) + 1



