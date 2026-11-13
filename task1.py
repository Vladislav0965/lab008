def word_counts(text):
    if not text:
        return {}
    counts = {}
    for i in text.lower().split():
        word = i.strip(".,!?;:")
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts
def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")