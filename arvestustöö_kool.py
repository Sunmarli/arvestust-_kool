from mymodule import *

while True:
    print("0-andmete lugemine\n1-andmete lisamine\n2-salvestame failisse\n3 Parimad opilased\n4 puudumiste jargi kasvavalt\n5 Kommissiooni \n6 Kustuta kellel rohkem kui 100 puudumist\n7 Puudumistoend ")
    v=int(input()) 
    if v==0:
        opilsed=[]
        puudumised=[]
        opilased=loe_failist("opilased.txt")
        puudumised=loe_failist("puudumised.txt")
        print(opilased)
        print(puudumised)
    if v==1:
        opilased, puudumised=element_listisse(opilsed,puudumised)
        print(opilased)
        print(puudumised)
    elif v==2:
        lisamine(opilased,"opilased.txt")
        lisamine(puudumised,"puudumised.txt")
    elif v==3:
        top3(opilased,puudumised)
    elif v==4:
        puudumistejargikasv(opilased,puudumised,1)
        for i in range(len(puudumised)):
            print(f"{opilased[i]} - {puudumised[i]}")
            #sorteeriminekasv(puudumised,opilased)
    elif v==5:
        komisiiooni(puudumised,opilased) 
    elif v==6:
        deletefromlist(puudumised,opilased) 
    elif v==7:
        puudumistetoend(puudumised,opilased) 

