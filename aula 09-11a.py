print("olar")

contador = 1

#laço exibir de 1 a 10

while(contador <=10):
  print(contador)
  contador = contador+1

fruta="morango"
print("morango")

#lista
frutas = ["morango", "laranja", "manga"]
for f in frutas:
  print(f)

#quero exibir apenas a 3 fruta
  print (frutas[1])

#quantas frutas tem na lista
  print (len(frutas))
  
#adicionar nova fruta
frutas.append("caqui")
print(frutas)


#substituir item da lista
frutas[0] = "caqui"

print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print ("exemplo de fruta com while")
i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i+1

print ("exemplo de fruta com for")
for fruta in frutas:
    print (fruta)
  
