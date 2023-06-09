import urllib.request

# URL of the English word list
#url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
url = 'https://github.com/gokhanyavas/Oxford-3000-Word-List/blob/master/Oxford%203000%20Word%20List%20No%20Spaces.txt'

# Download the word list
response = urllib.request.urlopen(url)
words = response.read().decode().splitlines()

# Write the words to a text file
with open('english_words.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')