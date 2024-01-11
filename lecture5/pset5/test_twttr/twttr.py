def main():
    word = input("Input: ").strip()
    output = shorten(word)
    print(f"Output: {output}")
def shorten(word):
    l_word = []
    for w in word:
        if w.upper() in ["A", "E", "I", "O", "U"]:
            pass
        else:
            l_word.append(w)
    return "".join(l_word)
if __name__ == "__main__":
    main()
