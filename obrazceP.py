# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:48:48 2023

@author: jindr
"""
def start():
    radky = int(input("Kolik chcete radku?(Pro diamant musi byt liche): "))
    obrazec = int(input("1.Kosoctverec \n2.Diamant\n"))
    hvezda = 1
    if obrazec == 1:
        for i in range(radky):
            #podle pozice radku odecitam mezery a printim *
            print(" " * ((radky - 1)- i) + "* " * radky)
    if obrazec == 2:
        if radky % 2 == 0:
            print("Zadal jste sude cislo, zadejte liche")
            start()
        else:
            for i in range(radky):
                print(" " * ((radky - 1)- i) + "*"*hvezda)
                hvezda += 2
                if hvezda == radky:
                    print(" " * ((radky - 1)- i) + "*"*hvezda)
                    
    if obrazec != 1 and obrazec !=2:  
        print("Zadal jste spatnou hodnotu")
        start()

start()        
