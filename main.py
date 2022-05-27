# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
# [assignment] Add your code here
    file = open(filename, "r")
    txt = file.read()
    return txt

print(read_file_content("story.txt"))

def count_word(txt):
#         create an empty dictionary
        counts = dict()
        words = txt.split()

#       loop through each line of the file
        for word in words:
          if word in counts:
            counts[word] += 1
          else:
           counts[word] = 1
        return counts
txt = read_file_content("story.txt")
print(count_word(txt))