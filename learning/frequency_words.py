#Find frequency of words in a sentence 
def freq_words():
    str = input("Enter a sentence: ")
    li = str.split()
    d = {}
    
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i] = d[i]+1
    print(d)
    
freq_words()