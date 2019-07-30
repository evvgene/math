# -*- coding: utf-8 -*-
import re

def correct(text):
   if not text.endswith('.'):
       text += '.'
   return(text)

# s='texttext'
# if s.endswith('.'):
#    print (s)
# else:
#    print (s + '.')


def first_word(text: str) -> str:
   return re.search("([\w']+)", text).group(1)

# print (s.rfind(sub))

# def second_index(text: str, symbol: str):
#  try:
#        return text.index(symbol, text.index(symbol) + 1)
#    except ValueError:
#        return None

def btw(text, begin, end):
    a=text.find(begin)
    b=text.find(end)
    c=len(begin)
    if a == -1 and b == -1:
       return (text)
    elif a == -1:
       return (text[:b])
    elif b == -1:
       return (text[a+c:])
    else:
       return (text[a+c:b])

#    start = text.find(begin) + len(begin) if begin in text else None
#    stop = text.find(end) if end in text else None
#    return text[start:stop]

# print (btw('What is >apple<', '>', '<'))
# print (btw('No[/b] hi', '[b]', '[/b]'))
# print (btw('No [b]hi', '[b]', '[/b]'))
# print (btw('No hi', '[b]', '[/b]'))
# print (btw('No <hi>', '>', '<'))


def best_stock(data):
   max_price = 0
   for i in data:
       if data[i] > max_price:
           max_price = data[i]
           answer = i

   return(answer)

def best_stock2(data):
   return max(data, key=data.__getitem__)

def best_stock3(data):
   return max(data, key=lambda x: data[x]) 
# print (best_stock({'CAC': 10.0,'ATX': 390.2,'WIG': 1.2}))


def checkio1(number):
   while 0<number<=1000:
       if number % 3 == 0 and number % 5 == 0:
           return("Fizz Buzz")
       elif number % 3 == 0:
           return("Fizz")
       elif number % 5 == 0:
           return("Buzz")
       else:
           return(number)
# print(checkio(100000))

lambda n:("Fizz "*(1-n%3)+"Buzz "*(1-n%5))[:-1]or str(n)

def easy_unpack(tuple):
    return(tuple[0], tuple[2], tuple[-2])

# print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
# print(easy_unpack((6, 3, 7)))


from operator import itemgetter
easy_unpack = itemgetter(0, 2, ~1)


def checkio2(*args):
    while 0<=len(args)<=20:
        if args == ():
            return(int(0))
        else:
           return(max(args)-min(args))
        

# print(checkio((1, 2, 3)))
# print(checkio((0.1, 0.2, 0.3)))
# print(checkio())
# print(checkio(-0.07))

# return max(args) - min(args) if args else 0