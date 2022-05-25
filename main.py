# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re



def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
      just = f.read()
    return just
    # return "Hello World"


def count_words():
    text = read_file_content('Reading-Text-Files/story.txt')
    # [assignment] Add your code here
    check = {}
    res = re.sub(r'[^\w\s]', '', text)
    name =  res.split()
    for word in name:
        if word in check:
            check[word] += 1
        else:
            check[word] = 1
    return check
    # return {"as": 10, "would": 20}


print(read_file_content('Reading-Text-Files/story.txt'))
print(count_words())