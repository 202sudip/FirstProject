from urllib.request import urlopen

def read_file():
        contents = open("C:\\cursewords\movie_quotes.txt")
        quotes = contents.read()
        print(quotes)
        check_badwords(quotes)




def check_badwords(word_to_check):
    print("Checking for the word ", word_to_check)
    connection = urlopen("http://wdylike.appspot.com/?q=" + word_to_check)
    output = connection.read()
    print(output)

read_file()