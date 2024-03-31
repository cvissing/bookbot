def get_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def word_count(book):
    words = book.split()
    return len(words)


def letter_count(book):
    counts = {}
    lowered_book = book.lower()
    for word in lowered_book:
        for i in word:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
    return counts


def sort_on(dict):
    return dict[1]


def report(book):
    counts = letter_count(book)
    counts = {key: value for key, value in counts.items() if key.isalpha()}
    trimmed_counts = list(counts.items())
    trimmed_counts.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(book)} words found in the document")
    print("")
    for k, v in trimmed_counts:
        print(f"The {k} character was found {v} times")
    print("--- End report ---")


def main():
    book = get_contents("books/frankenstein.txt")
    # word_count(book)
    report(book)


main()
