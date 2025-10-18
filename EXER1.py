from EXERCICIOS.classevetor import Vetor
import os

def limpa_tela():
    return os.system('cls')

def limpa_tela_tempo():
    limpa_tela()
    return os.system('cls')

def menu():
    print("      ***** MENU TRABALHO *****")
    print("=====================================")
    print("Estudante: Ketlin B Spindola")
    print("Matéria: Estrutura de dados")
    print("Exercício 1: Vetor")
    print("=====================================")
    print("0 - Sair do programa.")
    print("1 - Inserir valor no vetor.")
    print("2 - Mostrar vetor.")
    print("3 - Mostrar vetor de trás para frente.")
    print("4 - Informar frequencia de valor no vetor.")
    print("5 - Informar indíces de um vlar no vetor.")
    print("6 - Ler valor e substitui-lo no vetor.")
    print("3 - Somar todos os valores incluidos.")
    print("3 - Mostrar maior e menor valor com índices.")
    print("=====================================")
    escolha_usuario = int(input("Escolha uma opção: " ))
    return escolha_usuario


def escolhas_menu(escolha_usuario):
    vetor = Vetor(11)
    if escolha_usuario != 1 and Vetor.esta_vazio:
        limpa_tela()
        print("Primeiro inclua um valor no vetor.")
        limpa_tela_tempo()
    else:
        match escolha_usuario:
            case 0:
                limpa_tela()
                print("Encerrando o programa.")
                limpa_tela_tempo()
                return
            case 1:
                limpa_tela()
                Vetor.entrada_vetor()
                limpa_tela_tempo()
            case 2:
                limpa_tela()
                Vetor.printar()
                limpa_tela_tempo()
            case 3:
                limpa_tela()
                Vetor.printar_trasfrente()
                limpa_tela_tempo()
            case 4:
                limpa_tela()
                print(f"A frequência desse valor no vetor é: {Vetor.frequencia_valor()}")
                limpa_tela_tempo()
            case 5:
                limpa_tela()
                valor = int(input("Informe qual número deseja retornar os índices: "))
                print(f"O {valor} se encontra no índice: ", end="")
                for item in (Vetor.retorna_indices):
                    print(item, end="")
                limpa_tela_tempo()


