# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES


a =str(input("digite algo"))
a = a.upper().replace(" " , "")
inv = a .upper() [::-1]
inv = inv.replace (" " ,"")
if a == inv:
      print("é um polindromo")
else:
       print("nao é")
     
   