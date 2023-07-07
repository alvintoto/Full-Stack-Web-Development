def word_count():
    word = input("Enter a word: ").lower().strip(".,!?")
    with open("PythonSummary.txt", "r") as file:
        contents = file.read().lower()
        count = contents.count(word)
    print(f"The word {word} occurs {count} times")

word_count()