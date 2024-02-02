import re
import requests
from bs4 import BeautifulSoup
a=""
b=""
c=""
x=""
y=""
z=""
stop_words=["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yorselves","←","use","13","-3",
"he","him","his","himself","she","her","hers","herself","it","its","itself","they",":","it's","","//","$","b","(",")","'","run","43","-23",
"them","their","theirs","themselves","what","which","who","whom","this","that","==","*","i'm","haven't","althouh","@#&","]","name","[name]","k",
"these","those","am","is","are","was","were","be","been","being","have","has","had","<",">","<=","shouldn't","won't","--",">=","[x]","line","value","next","first",
"having","do","does","did","doing","a","an","the","and","but","if","or","in","=","also","-","!=","what's","0","1","2","3","4","5","6","7","8","9","  ","233",
"because","as","until","while","of","at","by","for","with","about","against","between","into","can't","couldn't","#",">>>","/","'","%",",","33",
"though","during","before","after","above","below","to","from","up","down","out","on","off","over","under","you,ve","there's","##","**",".","that's","243","b23",
"again","further","then","once","here","there","when","where","why","how","all","any","both","each","doesn't","don't","you're","we're","here's","whether","next",
"few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"]#stop words list
nofiltered_sentences=[]
filtered_sentences=[]
only_word=[]

count_book=int(input("How many books do you want to see (1 or 2) :"))

if  count_book==1:
    book_name=input("Enter the book name: ")
elif count_book==2:
    book_name = input("Enter the first book name: ")
url =  f"https://en.wikibooks.org/wiki/{book_name}" # Site link

response =  requests.get(url) #  pull  web page.

html_icerigi = response.content  #  get the content of  website.

soup =  BeautifulSoup(html_icerigi,"html.parser") # throw it into the BeautifulSoup object to break up  website..

for i in soup.find_all("h1",{"class":"firstHeading"}):#get the title of the first book from the site
    book_n1=i.text

def main():#printing web page articles to txt
    outfile=open("book.txt","w",encoding="utf-8")# If there is a file named book, open it, otherwise create it
    for i in soup.find_all("div",{"class":"mw-body"}):#get div tags whose class is mw-body
        outfile.write(i.text)
    outfile.close()
main()

def main():# reading from txt
    readfile=open("book.txt","r",encoding="utf-8")
    file_contents=readfile.read()
    readfile.close()
    file_contents=file_contents.lower()#make all letters lower size
    nofiltered_sentences.append(file_contents)
main()

for word in nofiltered_sentences:# Splitting text in txt by space character
    only_word=word.split()

for i in only_word:
    a=a+"/"+i

only_word2=a.split('(')# Splitting text in txt by '(' character
for i in only_word2:
    b=b+"/"+i

only_word2=b.split('.')# Splitting text in txt by '.' character
for i in only_word2:
    c=c+"/"+i

only_words=re.split("_| |/", c)# Splitting text in txt by '_',' 'and'/' characters at the same time

for word in only_words:#remove unwanted characters from the left and right of the word
    word=word.rstrip(",")
    word = word.rstrip("!")
    word = word.rstrip("!)")
    word=word.rstrip(".")
    word = word.rstrip("'")
    word = word.rstrip("0")
    word = word.rstrip("1")
    word = word.rstrip("2")
    word = word.rstrip("3")
    word = word.rstrip("4")
    word = word.rstrip("5")
    word = word.rstrip("6")
    word = word.rstrip("7")
    word = word.rstrip("8")
    word = word.rstrip("9")
    word = word.rstrip(">")
    word = word.lstrip("*")
    word=word.rstrip(":")
    word=word.rstrip(";")
    word = word.rstrip(")")
    word = word.rstrip("(")
    word = word.rstrip("?")
    word = word.lstrip("(")
    word = word.lstrip("##")
    word = word.lstrip("<")
    word = word.rstrip("##")
    word = word.lstrip('"')
    word = word.rstrip('"')
    word = word.rstrip(':"')

    if word not in stop_words:#remove stop words
        filtered_sentences.append(word)

word_counter={}

for w in filtered_sentences:#count which word has been found how many times
    if w  not in word_counter.keys():
        word_counter[w]=1#Create if not found before
    else:
        word_counter[w]+=1#add 1 if found before
#
if count_book==2:
    nofiltered_sentences2 = []
    filtered_sentences2 = []
    only_word22 = []



    book_name2 = input("Enter the second book name: ")
    url2 = f"https://en.wikibooks.org/wiki/{book_name2}"  # Site link

    response2 = requests.get(url2)  #  pull  web page.

    html_icerigi2 = response2.content  #  get the content of  website.

    soup2 = BeautifulSoup(html_icerigi2, "html.parser")  # throw it into the BeautifulSoup object to break up  website..

    for i in soup2.find_all("h1", {"class": "firstHeading"}):#get the title of the second book from the site
        book_n2 = i.text

    def main():  #printing web page articles to txt
        outfile2 = open("book2.txt", "w", encoding="utf-8")# If there is a file named book, open it, otherwise create it
        for i in soup2.find_all("div", {"class": "mw-body"}):#get div tags whose class is mw-body
            outfile2.write(i.text)
        outfile2.close()
    main()

    def main():  # reading from txt
        readfile2 = open("book2.txt", "r", encoding="utf-8")
        file_contents2 = readfile2.read()
        readfile2.close()
        file_contents2 = file_contents2.lower()#make all letters lower size
        nofiltered_sentences2.append(file_contents2)
    main()

    for word in nofiltered_sentences2:  # Splitting text in txt by space character
        only_word22 = word.split()

    for i in only_word22:
        x = x + "/" + i

    only_word2 = x.split('(')# Splitting text in txt by '(' character
    for i in only_word2:
        y = y + "/" + i

    only_word2 = y.split('.')# Splitting text in txt by '.' character
    for i in only_word2:
        z = z + "/" + i

    only_words2 = re.split("_| |/", z)# Splitting text in txt by '_',' 'and'/' characters at the same time

    for word in only_words2:  #remove unwanted characters from the left and right of the word
        word = word.rstrip(",")
        word = word.rstrip("!")
        word = word.rstrip("!)")
        word = word.rstrip(".")
        word = word.rstrip("'")
        word = word.rstrip("0")
        word = word.rstrip("1")
        word = word.rstrip("2")
        word = word.rstrip("4")
        word = word.rstrip("5")
        word = word.rstrip("6")
        word = word.rstrip("7")
        word = word.rstrip("8")
        word = word.rstrip("9")
        word = word.rstrip(">")
        word = word.lstrip("*")
        word = word.rstrip(":")
        word = word.rstrip(";")
        word = word.rstrip(")")
        word = word.rstrip("(")
        word = word.rstrip("?")
        word = word.lstrip("(")
        word = word.lstrip("##")
        word = word.lstrip("<")
        word = word.rstrip("##")
        word = word.lstrip('"')
        word = word.lstrip(',')
        word = word.rstrip('"')
        word = word.rstrip(':"')
        word = word.rstrip('=')

        if word not in stop_words:#remove stop words
            filtered_sentences2.append(word)

    word_counter2 = {}

    for w in filtered_sentences2:#count which word has been found how many times
        if w not in word_counter2.keys():
            word_counter2[w] = 1#Create if not found before
        else:
            word_counter2[w] += 1#add 1 if found before
#
common_words={}
only_first={}
only_second={}
hm_counter=0
hm=input("Do you want to specify the number of word frequency?(y or n) :")
if hm == "y":
    hmc = int(input("how many word frequency do you want to see :"))
elif hm == "n":
    hmc = 20
if count_book==1:

    s= sorted(word_counter.items(),key=lambda x:x[1],reverse=True)#sort by values in the dictionary in ascending order

    for i in s:#print book1
        if hm_counter<hmc:
            if hm_counter==0:
                print("***************************************************************************")
                print("BOOK 1:  ",book_n1)
                print('{:<5}{:^33} '.format('NO WORD', ' FREQ_1'))
                print("***************************************************************************")
            print("{:<5}{:<15}{:<15}".format(hm_counter+1,i[0],i[1]))
            hm_counter+=1
        elif hm_counter==hmc:
            break

elif count_book==2:

    for i,k in word_counter.items():#common words
        for j,l in word_counter2.items():
            if i==j:
                common_words[i]= k+l

    for i,j in word_counter.items():#only words in the first book
        if i not in word_counter2.keys():
            only_first[i]=j

    for i,j in word_counter2.items():#only words in the second book
        if i not in word_counter.keys():
            only_second[i]=j

    s2 = sorted(common_words.items(), key=lambda x: x[1], reverse=True)# common words#sort by values in the dictionary in ascending order

    for i in s2:#print common words
        if hm_counter<hmc:
            if hm_counter==0:
                print("***************************************************************************")
                print("BOOK 1:  ", book_n1)
                print("BOOK 2:  ", book_n2)
                print("COMMON WORDS")
                print('NO WORD             FREQ_1     FREQ_2    FREQ_SUM')
                print("***************************************************************************")
            print("{:<5}{:<15}{:<12}{:<12}{:<12}".format(hm_counter+1,i[0],word_counter[i[0]],word_counter2[i[0]],i[1]))
            hm_counter+=1
        elif hm_counter==hmc:
            break
    print()
    print()
    s3 = sorted(only_first.items(), key=lambda x: x[1], reverse=True)  #only words in the first book#sort by values in the dictionary in ascending order
    hm_counter = 0
    for i in s3:#print only words in the first book
        if hm_counter < hmc:
            if hm_counter==0:
                print("***************************************************************************")
                print("BOOK 1:  ", book_n1)
                print("DISTINCT WORDS")
                print('{:<5}{:^33} '.format('NO WORD', ' FREQ_1'))
                print("***************************************************************************")
            print("{:<5}{:<15}{:<15}".format(hm_counter + 1, i[0],i[1]))

            hm_counter += 1
        elif hm_counter == hmc:
            break
    print()
    print()
    s4 = sorted(only_second.items(), key=lambda x: x[1], reverse=True)  #only words in the second book#sort by values in the dictionary in ascending order
    hm_counter = 0
    for i in s4:#print only words in the second book
        if hm_counter < hmc:
            if hm_counter == 0:
                print("***************************************************************************")
                print("BOOK 2:  ", book_n2)
                print("DISTINCT WORDS")
                print('{:<5}{:^33} '.format('NO WORD', ' FREQ_2'))
                print("***************************************************************************")
            print("{:<5}{:<15}{:<15}".format(hm_counter + 1, i[0], i[1]))

            hm_counter += 1
        elif hm_counter == hmc:
            break











