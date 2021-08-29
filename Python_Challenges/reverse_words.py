def reverse_words(text):
    words = text.split()
    r_words = []
    for i in words:
        r_words.append(i[::-1])
    results = " ".join(r_words)

    return results

print(reverse_words("hello prince"))