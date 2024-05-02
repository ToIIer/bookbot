import collections

def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path) 
    word_count = get_num_words(text)  
    character_count = get_num_letters(text) 
    print("--- Text Analysis of Frankenstein ---")
    print(f"{word_count} words counted") 
    print(f"{character_count}") 

def get_num_words(text): 
    words = text.split()
    return len(words) 

def get_num_letters(text): 
    characters = {}
    for c in text: 
        lowercase = c.lower() 
        if lowercase in characters: 
            characters[lowercase] += 1 
        else: 
            characters[lowercase] = 1 
    return characters
    
         

      



def get_book_text(path): 
    with open(path) as f: 
        return f.read() 



main()