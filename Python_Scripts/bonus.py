import matplotlib.pyplot as plt
import plotly as py

s = """
During static analysis of the file, we realize it has a binary resource embedded inside of it. The hex begins with 4D 5A, which is the MZ header for PE files.
As it turns out the program will drop this binary as a DLL tucked hidden away in an AppData folder. We'll simply dump it to disk using Resource Hacker, saving it as crackme1.dll
Inspecting the DLL
We open the DLL using PEView, or alternatively (and often better) PEStudio. We go to the Export Address Table (EAT) and see it exports a function called DisplayMessage.
"""
word = s.split()
words = {}
tmp = []
for i in word:
    words[i] = words.get(i, 0) + 1

for key, value in words.items():
    tmp.append((value, key))
tmp.sort()
tmp.reverse()
almost_word = tmp[0:10]

print(almost_word[0], type(almost_word[0][0]))
y = []
for i in almost_word:
    y.append(i[0])
    print(y)

# y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1 / 1.5
plt.bar(x, y, width, color="blue")

fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')
