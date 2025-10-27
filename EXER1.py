import os
from classevetor import Vetor

def limpa_tela_pausa():
    input("Enter para continuar..")
    os.system('cls')

def limpa_tela():
    os.system('cls')  

def print_entrada_invalida():
    print("\n-> Entrada inválida, tente novamente.")  
    print("=====================================")
    limpa_tela_pausa()


def menu():
    while True:
        limpa_tela()
        print("============================================")
        print("          ***** MENU TRABALHO *****")                  
        print("============================================")
        print("Estudante: Ketlin B Spindola")
        print("Matéria: Estrutura de dados")
        print("Exercício 1: Vetor")
        print("============================================")
        print("0 - Sair do programa.")
        print("1 - Inserir valor no vetor.")
        print("2 - Retirar valor do vetor.")
        print("3 - Mostrar elementos do vetor.")
        print("4 - Mostrar elementos do vetor de trás para frente.")
        print("5 - Informar frequencia de valor no vetor.")
        print("6 - Informar indíces de um valor no vetor.")
        print("7 - Ler valor e substitui-lo no vetor.")
        print("8 - Somar todos os valores incluidos.")
        print("9 - Mostrar maior e menor valor com índices.")
        print("============================================")
        try:
            entrada_usuario = int(input("Escolha uma opção: "))
            return entrada_usuario
        except ValueError:
            print_entrada_invalida()
        
def main():
    vetor = Vetor(5)
    while True:
        entrada_usuario = menu()
        if entrada_usuario > 1 and entrada_usuario <= 9 and vetor.esta_vazio():
            print("\n-> Primeiro, inclua um valor no vetor (Opção 1).")
            print("================================================")
            limpa_tela_pausa()
        elif entrada_usuario > 9 and vetor.esta_vazio():
            print("\n-> Escolha inválida, tente novamente.")  
            print("=====================================")
            limpa_tela_pausa() 
        else:
            match entrada_usuario:
                case 0:
                    limpa_tela()
                    print("Você escolheu a opção 0 - Sair.")
                    print("===============================")
                    print("-> Encerrando o programa.")
                    return
                case 1: 
                    if vetor.esta_cheia():
                        print("\n-> O vetor esta cheio. Não é possível inserir valores.")
                        print("======================================================")
                    else:
                        limpa_tela()
                        while True:
                            try:
                                print("Você escolheu a opção 1 - Inserir valor.")
                                print("========================================")
                                entrada_usuario = int(input("Informe qual valor deseja inserir: "))
                                if entrada_usuario < 1000:
                                    vetor.entrada_vetor(entrada_usuario)
                                    break
                                else:
                                    print("\n-> O valor é muito grande para incluir no vetor. Escolha outro.")
                                    print("============================================================")
                                    limpa_tela_pausa()
                            except ValueError:
                                print_entrada_invalida()
                        print("\n")
                        print(f"Valor {entrada_usuario} incluido com sucesso no índice {vetor.fim-1}")
                        print("==========================================")
                    limpa_tela_pausa()
                case 2:
                    limpa_tela()
                    print("Você escolheu a opção 1 - Retirar valor.")
                    print("========================================")
                    print("\n       **MENU**")
                    print("======================")
                    print("1- Retirar por valor.")
                    print("2- Retirar por índice.")
                    print("======================")
                    while True:
                        try:
                            entrada_usuario = int(input("Escolha uma opção: "))
                            if entrada_usuario == 1 or entrada_usuario == 2:
                                break
                        except ValueError:
                                print_entrada_invalida()

                    match entrada_usuario:
                        case 1:
                            while True:
                                try:
                                    limpa_tela()
                                    print("Você escolheu retirar por valor.")
                                    print("Para sua visualização, esse é o vetor atual: ")
                                    print("============================================")
                                    vetor.printar()
                                    print("")
                                    print("============================================")
                                    entrada_usuario = int(input("Informe qual valor deseja retirar: "))
                                    if vetor.encontrar_valor(entrada_usuario):
                                        indices_retirados = vetor.retirar_valor(entrada_usuario)
                                        print("\n")
                                        for item in indices_retirados:
                                            print(f"-> Valor {entrada_usuario} retirado do índice {item}.")
                                        print("\n")
                                        limpa_tela_pausa()
                                        break
                                    else:
                                        print("\n")
                                        print("-> O vetor não possui esse valor. Tente novamente.")
                                        print("===============================================")
                                        limpa_tela_pausa()
                                except ValueError:
                                    print_entrada_invalida()
                        case 2:
                            while True:
                                try:
                                    limpa_tela()
                                    print("Você escolheu retirar por índice.")
                                    print("Para sua visualização, esse é o vetor atual: ")
                                    print("============================================")
                                    vetor.printar()
                                    print("")
                                    vetor.printar_indices()
                                    print("")
                                    print("============================================")
                                    entrada_usuario = int(input("Informe qual valor deseja retirar: "))
                                    if vetor.encontrar_valor(entrada_usuario):
                                        indices_valor = vetor.retorna_indices(entrada_usuario)
                                        for item in indices_valor:
                                            valor_retirado = vetor.retirar_indice(item)
                                            print(f"-> Valor {valor_retirado} retirado do índice {item}.")
                                            print("\n")
                                        limpa_tela_pausa()
                                        break
                                    else:
                                        print("\n")
                                        print("O vetor não possui esse valor. Tente novamente.")
                                        print("===============================================")
                                        limpa_tela_pausa()
                                except ValueError:
                                    print_entrada_invalida()

                        case _:
                            print("\n-> Escolha inválida, tente novamente.")  
                            print("=====================================")
                            limpa_tela_pausa() 
                    print(f"Valor {entrada_usuario} retirado com sucesso.")
                    print("====================================")
                case 3:
                    limpa_tela()
                    print("Você escolheu a opção 2.")
                    print("========================")
                    print("Printando elementos:\n")
                    vetor.printar()
                    print("\n")
                    limpa_tela_pausa()
                case 4:
                    limpa_tela()
                    print("Você escolheu a opção 3.")
                    print("========================================")
                    print("Printando elementos de trás para frente:\n")
                    vetor.printr_tf()
                    print("\n")
                    limpa_tela_pausa()
                case 5:
                    limpa_tela()
                    while True:
                        try:
                            print("Você escolheu a opção 4 - Mostrar frequência de um valor.")
                            print("=========================================================")
                            valor = int(input("Informe qual valor deseja verificar: "))
                            break
                        except ValueError:
                            print_entrada_invalida()
                    retorno_funcao = vetor.frequencia_valor(valor)
                    if retorno_funcao is False:
                        print("\n")
                        print("O vetor não possui esse valor.")
                        print("==============================")
                    else:
                        print("\n")
                        print(f"O vetor possui esse valor em {retorno_funcao} índice(s).")
                        print("========================================")
                    limpa_tela_pausa()
                case 6:
                    limpa_tela()
                    while True:
                        try:
                            print("Você escolheu a opção 5 - Mostrar índices de um valor.")
                            print("======================================================")
                            valor = int(input("Informe qual valor deseja verificar: "))
                            if vetor.encontrar_valor(valor):
                                break
                            else:
                                print("\n")
                                print("O vetor não possui esse valor. Tente novamente.")
                                print("===============================================")
                                limpa_tela_pausa()
                        except ValueError:
                            print_entrada_invalida()
                    retorno_funcao = vetor.retorna_indices(valor)
                    if not retorno_funcao:
                        print("\n")
                        print("O vetor não possui esse valor.")
                        print("==============================")
                    else:
                        print("\n")
                        print(f"O valor {valor} se encontra no(s) índice(s): ")
                        print("=======================================")
                        for item in (retorno_funcao):
                            print(f"[{item}] ", end="")
                        print("")
                        print("=======================================")
                    limpa_tela_pausa()
                case 7:
                    limpa_tela()
                    while True:
                        try:
                            print("Você escolheu a opção 6 - Substituir valor.")
                            print("===========================================")
                            entrada_usuario = int(input("Informe qual valor deseja substituir: "))
                            if entrada_usuario < 1000:
                                break
                            else:
                                limpa_tela()
                                print("O valor é muito grande para incluir no vetor. Escolha outro.")
                                print("============================================================")
                                limpa_tela_pausa()
                        except ValueError:
                            print_entrada_invalida()
                    print("\n")
                    print(f"Você escolheu substituir o número {entrada_usuario}.")
                    if vetor.encontrar_valor(entrada_usuario):
                        while True:
                            try:
                                entrada_substituir = int(input("Informe o novo valor: "))
                                if entrada_substituir < 1000:
                                    print("\n")
                                    print("=============================================")
                                    break
                                else:
                                    print("O valor é muito grande para por no vetor. Escolha outro.")
                            except ValueError:
                                print_entrada_invalida()
                        indices_substituidos = vetor.substitui_valor(entrada_usuario, entrada_substituir)
                        for item in indices_substituidos:
                            print(f"-> {entrada_substituir} inserido no índice {item} - substituindo {entrada_usuario}.")
                        print("=============================================")
                        print("\n")
                        print("Vetor atualizado:\n")
                        vetor.printar()
                        print("\n")
                
                    else:
                        print("\n")
                        print("O vetor não possui esse valor.")
                        print("==============================")

                    limpa_tela_pausa()
                case 8:
                    limpa_tela()
                    print("Você escolheu a opção 7 - Somar valores.")
                    print("========================================")
                    retorno_funcao = vetor.soma_valores()
                    print(f"A soma total do vetor é: {retorno_funcao}")
                    print("\n")
                    limpa_tela_pausa()
                case 9:
                    limpa_tela()
                    print("Você escolheu a opção 7 - Printar maior e menor valor.")
                    print("======================================================")
                    retorno_funcao = vetor.encontra_maior_menor()
                    if not retorno_funcao is False:
                        maior,menor,indices_maior,indices_menor = retorno_funcao
                        print(f" Menor valor: {menor} no(s) indice(s): {indices_menor}")
                        print(f" Maior valor: {maior} no(s) indice(s): {indices_maior}")
                    else:
                        print("O vetor possui um único valor, portanto, o maior e menor é {retorno_funcao}")
                    print("\n")
                    limpa_tela_pausa()
                case _:
                    print("\n-> Escolha inválida, tente novamente.")  
                    print("=====================================")
                    limpa_tela_pausa() 


if __name__ == "__main__":
    main()