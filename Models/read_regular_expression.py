import re

#Patron que debe seguir la expresion regular
patron = re.compile(r'\bbar\b')

texto = """ bar foo bar
foo barbarfoo
foofoo foo bar
"""

m = patron.match('foo bar')
print('MATCH 2: ', m)

s = patron.search(texto)
print('SEARCH: ', s)

fa = patron.findall(texto)
print('FINDALL: ', fa)