import re
#s="ba be bu ban banh bo bong ban bun bo ban boong boong ban bong bong ban bong ban buoi"
s=input('Nhap:')
words=s.split()
word=input('Nhap:')
pos = s.index(word)
new_words=s[pos:]
sotu=len(new_words.split())
count=0
for i in range(len(words)):
     if word in words[i][0]:
          count=count+1
print("So chu cai '",word,"' La: ",count)
print ('so luong tu: ',sotu)