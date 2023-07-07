def punishment():
    sentence = input("Enter a sentence: ")
    repeats = int(input("Enter the number of times to repeat the sentence: "))
    with open("CompletedPunishment.txt", "w") as file:
        for i in range(repeats):
            file.write(sentence + "\n")
    print(f"Sentence repeated {repeats} times and written to CompletedPunishment.txt")

punishment()