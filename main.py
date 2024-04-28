def main():
    path = "books/frankenstein.txt"
    frank_text = get_book_text(path)
    frank_num_words = get_num_words(frank_text)
    #print(frank_num_words)
    frank_letters = count_letters(frank_text)
    print_report(path,frank_num_words,frank_letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    num_words = len(words) 
    return num_words

def count_letters(text):
    chars = {}
    for letter in text:
        # print(letter)
        low = letter.lower()
        if low in chars:
            #print(False)
            chars[low] += 1
        else:
            chars[low] = 1
    #print(chars)
    return(chars)

def print_report(path,words,letters):
    print(f"--- Begin of report for {path} ---")
    print(f"{words} words found in the document")
    print(f"--- End of report for {path} ---")


main()