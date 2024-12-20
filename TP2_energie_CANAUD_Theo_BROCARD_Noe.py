import matplotlib.pyplot as plt
import csv

angleterre=[] 
espagne=[]
italie=[]
suisse=[]
allemagne_belgique=[]

with open("RTE_2022.csv",newline="") as csvfile:                   #On lit le fichier
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        if row[18]=='':                                            #On supprime les espaces vides 
            row[18]=0
        elif row[19] == '':
            row[19]=0
        elif row[20] == '':
            row[20]=0
        elif row[21] == '':
            row[21]=0
        elif row[22] == '':
            row[22]=0
        else:
            angleterre.append(row[18])                              #Je mets dans mes listes tous les valeurs pour chaque pays   
            espagne.append(row[19])
            italie.append(row[20])
            suisse.append(row[21])
            allemagne_belgique.append(row[22])
del angleterre[0]                                                   #On enlève la première ligne
del espagne[0]  
del italie[0]  
del suisse[0]  
del allemagne_belgique[0]  

m_angleterre= sum(int(x) for x in angleterre)                       #Addition de tous les valeurs pour chaque pays
m_espagne= sum(int(x) for x in espagne)
m_italie= sum(int(x) for x in italie)
m_suisse= sum(int(x) for x in suisse)
m_allemagne_belgique= sum(int(x) for x in allemagne_belgique)

pays = []                                                           #Création d'une liste pour stocker les moyennes de tous les pays
pays.append(m_angleterre)           
pays.append(m_espagne)
pays.append(m_italie)
pays.append(m_suisse)
pays.append(m_allemagne_belgique)

noms=["Angleterre","Espagne","Italie","Suisse","Allemagne/Belgique"]

plt.bar(noms, pays,color='red',edgecolor='black',alpha=0.7,)                        #Paramétrage de la courbe
plt.ylabel('Energie donnée ou reçu')                                                
plt.title('Echange des ressoures avec la France en fonction des autres pays')
plt.show()                                                                          #Affichage de la courbe