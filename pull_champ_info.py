from html.parser import HTMLParser
from objCreator import *
from urllib.request import Request, urlopen
from urllib import parse
from champ_obj import *




start_url = "http://battlerite.gamepedia.com/"
champs = ["Ashka","Ezmo","Iva","Jade","Jumong","Taya","Varesh","Bakko","Croak","Freya","Rook","Ruh_Kaan","Shifu","Lucie","Oldur","Pearl","Pestilus","Poloma","Sirius"]

parser = AnHTMLParser()

for champ in champs:
    # ########## Get HTML version of chosen link ########## #
    req = Request(start_url+champ, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    # ### Convert HTML from bytes to str ### #
    str_page = webpage.decode("utf-8")

    # ### Print out feed results ### #
    print(parser.feed(data=str_page))











    # ### Test if HTML is str ### #
print(type(str_page))

    # ### Create parser instance ### #
