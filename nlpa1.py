import nltk
#nltk.download()
from nltk.book import*
import matplotlib.pyplot as plt

def lexical_diversity(text):
    return len(text)/len(set(text))

def percentage(count,total):
    return 100*(count/total)

lexical_diversity(text1)

sentence1=['my','name','is','Abhishek Maira','.']
sent4 + sent1
sent1.append('my name')
text1[4]
text1.index("awaken")  
text1[20:100]
name='abcdefg'
name[0:4]
name[0]
name + name
name*5
' '.join(['abcdef', 'Python'])
'abcdef Python'.split()

fdist=FreqDist(text1)
vocab=fdist.keys()
vocab = list(fdist.keys())#returns an iteratable but not indexable object python 3
vocab[:50]
fdist.items()
fdist.plot(50,cumulative=True)
fdist.hapaxes()
fdist['monstrous']
fdist.freq('monstrous')
fdist.N()
fdist.max()
fdist.tabulate()

fdist1=FreqDist(text2)
fdist>fdist1
colo=text1.collocation_list()
text1.collocation_list()
text4.collocation_list()
V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted([w for w in set(text1) if len(w) > 7 and fdist[w] > 7])

[len(w) for w in text1]
fdist = FreqDist([len(w) for w in text1])
fdist.keys()

#q1
text5.collocation_list()

#q2
l1=['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
string = ''
for i in l1:
    string = string + i + ' ' 
l2 = string.split()

#q3
print(text9.index('sunset'))

#6th
def slicer():
    l=len(text2)
    last=text2[l-1]
    second_last=text2[l-2]
    print(last,second_last)
   
#q7
def freqdist():
    x=[i for i in text5 if(len(i)==4)]
    d=dict()
    for i in x:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1        
    sorted_d=sorted(d.items(),key=lambda x:x[1],reverse=True)
    x1=[i[0] for i in sorted_d]
    x2=[i[1] for i in sorted_d]
    plt.bar(x1[0:7],x2[0:7])

#q8
def upper():
    print([i for i in text6 if i.isupper()])
   
#q9
print([i for i in text5 if i.endswith('ize')])
print([i for i in text6 if i.endswith('z')])
print([i for i in text6 if 'pt' in i])

#q10
l=['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
#10.a
print([i for i in l if i.startswith('sh')])
#10.b
print([i for i in l if len(i) > 4],"\n")

#q11
sum1 = sum([len(w) for w in text1])
no = [i for i in text1]
average = sum1/len(no)
print(average,"\n")

#q12
def vocab_size(text):
    return len(set(text))
print(vocab_size(text1))

#q13
def percent(word,text):
    d = dict()
    for i in text:
        if i in d:
            d[i] = d[i]+1
        else: d[i] = 1
    return d[word]/len(text)
print(percent('she',text1))
        


