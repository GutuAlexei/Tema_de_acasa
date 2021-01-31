prenume=['Mihai' , 'George' , 'Ana' , 'Dan' , 'Ion' , 'Geta' , 'Vio']
varsta=[14 , 23 , 15 , 14 , 12 , 41 , 39]
for i in range(0 , len(prenume)):
    print(prenume[i] , 'are varsta de ' , varsta[i] , 'ani')
    i+=1
prenume.extend(['Andreea' , 'Ion'])
varsta.extend([34 , 23])
print('Adăugați în liste la final: (Andreea,Ioan)'  , prenume)
print('Adăugați în liste la final: 34 și 23' , varsta)
prenume.pop(2)
varsta.pop(2)
print('Ștergeți numele Ana:' ,prenume)
print('Ștergeți varsta a Anei:' ,varsta)
print('Afișați primele trei elemente din lista prenume:' ,prenume[0:3])
print('Afișați lista prenume de la dreapta la stânga:' ,prenume[::-1])
print('Afişaţi elementele cu indicii 2 și 4:' ,prenume[2] , prenume[4])
print('Afişaţi elementele de la 0 la 5:' , varsta[0:5])