# -*- coding: utf-8 -*-

carro1 = ("Gol", 2020, 55000.0, ["Ar-condicionado", "Direção hidráulica"])
carro2 = ("Civic", 2022, 120000.0, ["Ar digital", "Bancos de couro", "Câmera de ré"])
carro3 = ("Onix", 2021, 75000.0, ["Ar-condicionado", "Central multimídia"])

print(" Carros Criados ")
print(carro1)
print(carro2)
print(carro3)
lista_carros=[carro1,carro2,carro3]

def carro_novo(lista):
    novo_carro=lista[0]
    for listas in lista:
        if listas[1] > novo_carro[1]:
         novo_carro=listas
    return novo_carro[0]        
modelo_mais_novo=carro_novo(lista_carros)
print(f"O modelo mais novo é :{modelo_mais_novo}")
novo_carro=("brasilia",1978,50000.0,["friso-lateral"])
lista_carros.append(novo_carro)
print(f"/nSua nova listas de carro atualizada é :{lista_carros}")
carro1[3].append("Vidros elétricos")
print(carro1)
print(f"Modelo: {novo_carro[0]},Preço: R${novo_carro[2]:.2f}")
