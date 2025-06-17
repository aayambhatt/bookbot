def no_of_words_in_book(text): 
    words = text.split()
    return len(words)

def character_count(text):
    count = {}
    for ch in text:
        ch = ch.lower()
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
    return count
    
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(count):
    sorted_list = []
    for ch, num in count.items():
        sorted_list.append({"char": ch, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list