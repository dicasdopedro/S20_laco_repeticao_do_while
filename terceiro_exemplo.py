"""
PRESENTE DE ANIVERSÁRIO
"""
presente_esperado = "anel"

while True:
    presente = input("Qual presente o Hiago espera do Cleiton?: ")
    if presente == presente_esperado:
        print("Acertou! Sonho realizado!")
        break
    else:
        print("Errou! Continue tentando.")