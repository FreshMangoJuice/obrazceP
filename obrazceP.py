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
                #Vy printi mi prvni polovinu diamantu do prostredka, pak zastav
                print(" " * ((radky - 1)- i) + "*"*hvezda)
                hvezda += 2
                if hvezda == radky:
                    break
                #Vyprinti druhou pulku
            while (hvezda > 0):
                print(" " * ((radky - 2)- i) + "*"*hvezda)
                i -= 1
                hvezda -= 2
    if obrazec != 1 and obrazec !=2:  
        print("Zadal jste spatnou hodnotu")
        start()

start()
