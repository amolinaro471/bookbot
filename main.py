def main():
    path = "books/frankenstein.txt"
    frank_text = get_book_text(path)
    frank_num_words = get_num_words(frank_text)
    print(frank_num_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    num_words = len(words) 
    return num_words


main()