numero=[30,40,10,20,70]
print(numero)
numero.append(4.5)
numero.append(5.5)
numero.append(6.7)
numero.append(7.6)
numero.append(8.8)
print(numero)
print(ler(num))
numero.pop()
numero.pop()

lista_ordenada= sorted(numero)
print(lista_ordenada)
print("menor numero: ",min(numero))
print("maior numero: ",max(numero))
print("soma: ",sum(numero))
print("media: ",sum(numero) / len(numero))

numero.insert(0,"1")
numero.insert(1,"2")
print(numero)
