
#CALCULADORA
num_1 = input("diga seu numero")
num_2 = input("diga seu outro numero")
operacao = input("escolha sua operacao")
if operacao == "soma":
  print(float(num_1) + float(num_2))
elif operacao == "subtracao":
  print(float(num_1) - float(num_2))
elif operacao == "multiplicacao":
  print(float(num_1) * float(num_2))
elif operacao == "divisao":
  print(float(num_1) / float(num_2))