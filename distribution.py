"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
text = input("Please enter a string of text (the bigger the better): ") 
print('The distribution of characters in "' +  text + '" is:')

lettera = (text.count('a'))
print('a'*lettera)
lettera = (text.count('b'))
print('b'*lettera)
lettera = (text.count('c'))
print('c'*lettera)
lettera = (text.count('d'))
print('d'*lettera)
lettera = (text.count('e'))
print('e'*lettera)
lettera = (text.count('f'))
print('f'*lettera)
lettera = (text.count('g'))
print('g'*lettera)
lettera = (text.count('h'))
print('h'*lettera)
lettera = (text.count('i'))
print('i'*lettera)
lettera = (text.count('j'))
print('j'*lettera)
lettera = (text.count('k'))
print('k'*lettera)
lettera = (text.count('l'))
print('l'*lettera)
lettera = (text.count('m'))
print('m'*lettera)
lettera = (text.count('n'))
print('n'*lettera)
lettera = (text.count('o'))
print('o'*lettera)
lettera = (text.count('p'))
print('p'*lettera)
lettera = (text.count('q'))
print('q'*lettera)
lettera = (text.count('r'))
print('r'*lettera)
lettera = (text.count('s'))
print('s'*lettera)
lettera = (text.count('t'))
print('t'*lettera)
lettera = (text.count('u'))
print('u'*lettera)
lettera = (text.count('v'))
print('v'*lettera)
lettera = (text.count('w'))
print('w'*lettera)
lettera = (text.count('x'))
print('x'*lettera)
lettera = (text.count('y'))
print('y'*lettera)
lettera = (text.count('z'))
print('z'*lettera)


































