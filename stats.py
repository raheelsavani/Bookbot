def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    lower = text.lower()
    counts = {}

    for char in lower:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    return counts

def sort(char_counts):
    lst = [{"char": key, "num": value} for key, value in char_counts.items()]
    lst.sort(key=lambda item: item["num"], reverse=True)
    return lst
