cislo= [2,5,8,7]
hodnota= input ("zadejte cislo, které byste chtěli najít")
for i in range (len(cislo)):
    if hodnota==cislo:
        print(f"našel jsem cislo")
    else:
        print ("zadaná hodnota se zde nenachází")
