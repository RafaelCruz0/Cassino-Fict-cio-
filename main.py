import random
import time
def mostrar_menu():
    print("""
===== CASSINO =====
[1] Jogar roleta
[2] Jogar Cara ou coroa
[3] Jogar fortune
[4] Ver saldo
[5] Colocar saldo
[6] Sair
""")

def colocardinheiro(saldo, qtdadicionada):
    if qtdadicionada < 0:
        print("Depósito inválido!")
        return saldo
    saldo += qtdadicionada
    print("Carregando transação...........")
    time.sleep(2)
    print("Recarga feita! Aproveite!")
    return saldo
def tigrinho(saldo, qtdaposta):
    if qtdaposta < 0:
        print("Aposta inválida!")
        return saldo
    if saldo < qtdaposta:
            print("❌ Saldo insuficiente!")
            return saldo
    saldo -= qtdaposta
    coluna1 = ["casa", "casa", "bomba", "bomba", "bomba"]
    coluna2 = ["casa", "casa", "bomba", "bomba", "bomba"]
    coluna3 = ["casa", "casa", "bomba", "bomba", "bomba"]
    prim = random.choice(coluna1)
    sec = random.choice(coluna2)
    third = random.choice(coluna3)
    resultados = [prim, sec, third]
    qtdcasas = resultados.count("casa")
    print(f"Resultado: {prim} | {sec} | {third}")
    if qtdcasas == 3:
        saldo += qtdaposta * 3
        print(f"🎉 3 COMBINAÇÕES!! LENDÁRIO! Você ganhou: R${qtdaposta * 3}")
    elif qtdcasas == 2:
        ganho = int(qtdaposta * 1.5)  # Ganha 1.5x a aposta (dinheirinho)
        saldo += ganho
        print(f"✨ Quase lá! 2 COMBINAÇÕES! Você ganhou: R${ganho}")
    else:
        print("Não foi dessa vez!")
    print(f"💰 Saldo atual: R${saldo}")
    return saldo

def mostrar_saldo(saldo):
    print(f"\nSaldo atual: R$ {saldo}")

def sair():
    print("Ok, finalizando...")

def erro(perg):
    while True:
        try:
            valor = int(input(perg))
            return valor
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.\n")

def jogar_roleta(saldo, qtd_aposta):
    if qtd_aposta < 0:
        print("Aposta inválida!")
        return saldo
    if saldo < qtd_aposta:
        print("❌ Saldo insuficiente!")
        return saldo

    # Validação do número escolhido entre 0 e 10
    while True:
        num_escolhido = erro("De 0 a 10, qual número você irá escolher? ")
        if 0 <= num_escolhido <= 10:
            break
        print("⚠️ Número fora do intervalo! Escolha entre 0 e 10.\n")

    num_sorteado = random.randint(0, 10)
    print(f"🎲 Número sorteado: {num_sorteado}")

    if num_sorteado == num_escolhido:
        print("🎉 Ganhou!")
        saldo += qtd_aposta
    else:
        print("❌ Perdeu!")
        saldo -= qtd_aposta

    return saldo
def cara_ou_coroa(saldo, qtd_aposta):
    if qtd_aposta < 0:
        print("Aposta inválida!")
        return saldo
    if saldo < qtd_aposta:
        print("❌ Saldo insuficiente!")
        return saldo
    possivel = ["cara", "coroa"]
    sorteado = random.choice(possivel)
    while True:
        escolha2 = input("Cara ou coroa?").strip().lower()
        if escolha2 in possivel:
            break
        else:
            print("Valor inválido")
    print(f"🎲 Face sorteada: {sorteado}")
    if escolha2 == sorteado:
        print("🎉 Ganhou!")
        saldo += qtd_aposta
    else:
        print("❌ Perdeu!")
        saldo -= qtd_aposta

    return saldo

saldo = 1000  

while True:
    mostrar_menu()
    escolha = erro("Escolha uma opção: ")

    if escolha == 1:
        qtd = erro("Escolha quanto você deseja apostar: ")
        saldo = jogar_roleta(saldo, qtd)
        mostrar_saldo(saldo)
    elif escolha == 2:
        qtd2 = erro("Escolha quanto você deseja apostar: ")
        saldo = cara_ou_coroa(saldo, qtd2)
        mostrar_saldo(saldo)
    elif escolha == 3:
        qtdaposta = erro("Quanto você deseja apostar? ")
        saldo = tigrinho(saldo, qtdaposta)
        mostrar_saldo(saldo)
    elif escolha == 4:
        mostrar_saldo(saldo)
    elif escolha == 5:
        qtdadicionada = erro("Quanto você deseja adicionar? ")
        saldo = colocardinheiro(saldo, qtdadicionada)
        print(f"Saldo: {saldo}")
    elif escolha == 6:
        sair()
        break    
    else:
        print("⚠️ Opção inválida! Escolha entre 1 e 6.")