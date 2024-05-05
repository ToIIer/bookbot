

def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path) 
    word_count = get_num_words(text)  
    character_count = get_num_letters(text)  
    sorted_list = dictionary_sorted(character_count)
    print("--- Text Analysis of Frankenstein ---")
    print(f"{word_count} words counted") 
    print()

    # Checking if the characters in the sorted list are from the alphabet and ignoring the rest 
    # Displaying alpha character occurence count
    for item in sorted_list: 
        if not item["char"].isalpha(): 
            continue 
        print(f"The character '{item['char']}' was detected {item['num']} times") 
    
    print("--- End of Analysis ---")

# Splitting the text string on the whitespace and returning the word count
def get_num_words(text): 
    words = text.split()
    return len(words) 

# Takes a dictionary and returns the value of the "num" key 
# Required by the .sort() method to sort the list of dictionaries 
def sort_on(d): 
    return d["num"] 

# Creating a list of dictionaries and sorting it in descending order using the "num" value from sort_on
def dictionary_sorted(num_character_count): 
    sort_list = [] 
    for ch in num_character_count: 
        sort_list.append({"char": ch, "num": num_character_count[ch]}) 
    sort_list.sort(reverse=True, key=sort_on) 
    return sort_list 

# Iterating through the text file while counting how many times a character is used 
# Converting uppercase letters to lowercase to avoid duplicates
def get_num_letters(text): 
    characters = {}
    for c in text: 
        lowercase = c.lower() 
        if lowercase in characters: 
            characters[lowercase] += 1 
        else: 
            characters[lowercase] = 1 
    return characters
    
         

      


# Using a with statement to open the text file so that it is properly closed when execution is over
def get_book_text(path): 
    with open(path) as f: 
        return f.read() 



main()