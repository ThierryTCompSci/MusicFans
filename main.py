# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from db import *
from add_fan_account import *
from add_artist import *
from add_fan import *
from show_fan import *
from search_artist_fans import *
from menu import *

<<<<<<< HEAD
from math import *
=======

def quickmath():
	varx = int(input("x: "))
	vary = int(input("y: "))
	answyx = vary + varx
	print (answyx)
	
quickmath()
>>>>>>> dae9f6eafc725b66bca22370035393ebff587d9f

db = FansDb("ArtistsFans.db")

'''for genre in db.genres():
    print(genre['label'])
'''

#Edited

show_menu(db)
