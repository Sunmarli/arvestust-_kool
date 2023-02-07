

def loe_failist(file:str)->list:
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def lisamine(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def element_listisse(p:list,op:list):
    n=int(input("Mitu inimesi lisame?"))
    for j in range (n):
        nimi=input("Nimi: ")
        op.append(nimi)
        puudus=input("Puudus: ")
        p.append(puudus)
    return p,op

def top3(op:list,p:list):
    p=list(map(int,p))
    n=int(input("Mitu parimat opilast otsime? "))
    print(f"{n} Parimat opilast -- ",sorted(zip(p, op), reverse=False)[:n])

def puudumistejargikasv(op:list,p:list,a:int):
    N=len(p)
    for i in range(N):
        for j in range(i+1):
            if int(p[i])<int(p[j]):
                abi=p[i]
                p[i]=p[j]
                p[j]=abi 
                abi=op[i] 
                op[i]=op[j] 
                op[j]= abi
    return op,p
                
def sorteeriminekasv(p:list,op:list):
    p=list(map(int,p))
    arg_sort = sorted(range(len(p)), key=lambda i: p[i])
    print([p[i] for i in arg_sort])
    print([op[i] for i in arg_sort])

def komisiiooni(p:list,op:list):
    p=list(map(int,p))
    for i in range (len(p)):
        if p[i]>50:
            print(f"Opilane {op[i]} laheb kommissiooni!") 

def deletefromlist(p:list,op:list):
    p=list(map(int,p))
    for i in range(len(p)):
        for i in p:
            if i>100:
                ind=p.index(i)
                print(f" Opilane  {op[ind]}  eksmatrekuleeritud ")
                p.remove(i)
                op.pop(ind)        
    print(p)
    print(op)

def puudumistetoend(p:list,op:list):
    p=list(map(int,p))
    nimi=input("Sisesta opilase nimi kellel on toend --")
    n=int(input("Mitu paeva ta puudus haiguse tottu -- ")) 
    if nimi in op:
        ind=op.index(nimi) 
        s=int(p[ind])-n
        if s>0:
           p.insert(ind,s)
        elif s<0:
            print(f"Vale andmed, ei saa kustutada rohkem kui oli puudumist {p[ind]}")
    else: 
         print("Seda opilast ei ole meie koolis")   
    print(op) 
    print(p)


       


