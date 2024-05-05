
nome = input ("Qual seu nome: ")
print("------------------------------")
print("Selecione seus atributos")

atributos_forca = int   (input("Força: "))
atributos_vida = int    (input("Vida: "))
atributos_magia = int   (input("Magia: "))
atributos_vel = int     (input("Velocidade: "))


Bronze = int (100) 
Prata = int (250)
Ouro = int (500)
Platina = int (1000)
Diamante = int (5000)
Ruby = int (10000)
 
total = atributos_forca + atributos_vida + atributos_magia + atributos_vel
print("O seu OVER foi:",total)

if total <= int (100) and total <= int(249):
    print("Sua classe é Bronze")

if total >=  int (250) and total <= int(499):
    print("Sua classe é Prata" )

if total >= int (500) and total <= int(999):
    print("Sua classe é Ouro" )

if total >= int (1000) and total <= int(4999):
    print("Sua classe é Platina" )    

if total >= int(5000) and total <= int(9999):
    print("Sua classe é Diamante" )

if total >= int (10000):
    print("Sua classe é Ruby" )   

print("----------------------------------------------------") 

print("Agora irei gerar os seus oponentes...")

print("----------------------------------------------------") 

from random import randint

lista_monstro = []

def criar_monstro():
    level = randint(0,50)

    novo_monstro = {
            "": level,
            "Força": 10 * level, 
            "Vida": 50 * level,
            "Magia": 5 * level,
            "Velocidade": 2 * level ,
            "Level": level 
        }


    lista_monstro.append(novo_monstro)

criar_monstro()

print(lista_monstro)



