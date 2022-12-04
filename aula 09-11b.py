print("criiação de funções")

preco = 1999.90

print(preco)

#calcular 5 % de imposto guardar na variável e exibir na tel

imposto = preco* 0.05
print(imposto)


#criar a função calcular_imposto() que calcula um importo de 5% e retorna a quem pediu

def calcular_imposto(preco_produto):
  imposto = preco_produto* 0.05
  return imposto


#aqui eu uso pra calcular
preco = 299
imposto = calcular_imposto(preco)
print("O imposto de ", preco, "é",imposto)
print (preco)


#Explicação de variável local x global
print(preco) #????
preco_produto = 100
print(preco_produto) #????


#agora calcular o imposto a alíquota é agora 7%

ali= 0.07
def calcular_imposto(preco_produto):
  imposto = preco_produto* ali
  return imposto

  preco = 299
imposto = calcular_imposto(preco)
print("O imposto de ", preco, "é",imposto)
print (preco)

# agora calcular o imposto com vários valores
valores =[1.99, 24.50, 78.27, 1515.5]
# se eu quiser o imposto destes quatro valores e exibir assim o imposto de é ..."
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#Declarar um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota =7):
  imposto = valor * aliquota/100
  return imposto
#e se for 10%
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")
