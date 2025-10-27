#Classe vetor
import os  

def limpa_tela_pausa():
    input("Enter para continuar..")
    os.system('cls')

def limpa_tela():
    os.system('cls') 

class Vetor():
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [-1] * tamanho
        self.fim = 0

    #retorna se o vetor esta vazio
    def esta_vazio(self):
        return self.fim == 0

    #retorna se o vetor esta cheio
    def esta_cheia(self):
        return self.fim == self.tamanho
    
    #retorna bollean se um determinado valor esta no vetor ou não
    def encontrar_valor(self,valor):
        for i in range(self.fim):
            if self.vetor[i] == valor:
                return True
        return False
    
    #1
    #incluindo itens no vetor e aumentando fim
    def entrada_vetor(self, entrada_usuario):
        self.vetor[self.fim] = entrada_usuario
        self.fim += 1

    #2
    #retirar valor por numero
    def retirar_valor(self,valor_retirar):
        indices_valor = self.retorna_indices(valor_retirar)
        for item in indices_valor:     
            self.vetor[item] = -1
            self.fim -= (len(indices_valor))
        return indices_valor

    #retirar valor por numero índice  
    def retirar_indice(self,indice):
        valor_retirado = self.vetor[indice]
        self.vetor[indice] = -1
        self.fim -= 1
        return valor_retirado

    #3
    # printar elementos do vetor    
    def printar(self):
        for i in range (self.fim):
            print(f"| {self.vetor[i]} |", end="")
    
    def printar_indices(self):
        for i in range (self.fim):
            print(f"  {i}  ", end="")

    #4
    # printar de trás para frente os elementos do vetor 
    def printr_tf(self):
        for i in range(self.fim-1,-1,-1):
            print(f"| {self.vetor[i]} |", end="")
    #5
    #retorna quantas vezes determinado número consta no vetor
    def frequencia_valor(self,valor):
        if self.encontrar_valor(valor):
            contador = 0
            for i in range (self.fim):
                if self.vetor[i] == valor:
                    contador += 1
            return contador
        else:
            return False
    
    #6
    #retorna os indices que determinado número se encontra
    def retorna_indices(self,valor):
        if self.encontrar_valor(valor):
            vetor_indices = []
            for i in range(self.fim+1):
                if self.vetor[i] == valor:
                    vetor_indices.append(i)
            return vetor_indices
        else:
            return False
    
    #7
    #substitui determinado valor por outro
    def substitui_valor(self,valor_vetor, novo_valor):
        indices_valor = self.retorna_indices(valor_vetor)
        for item in indices_valor:
            self.vetor[item] = novo_valor
        return indices_valor
    
    #8
    #soma todos os números do vetor    
    def soma_valores(self):
        somador = 0
        for i in range(self.fim):
            somador += self.vetor[i]
        return somador

    #9
    #retorna o maior e menor valor        
    def encontra_maior_menor(self):
        maior = self.vetor[0]
        menor = self.vetor[0]
        indices_maior = [0]
        indices_menor = [0]
        
        for i in range(1,self.fim):
            atual = self.vetor[i]
            if atual > maior:
                maior = atual
                indices_maior = [i]
            elif atual == maior:
                 indices_maior.append(i)
            elif atual < menor:
                menor = atual
                indices_menor = [i]
            elif atual == menor:
                indices_menor.append(i)
        if maior == menor:
                return self.vetor[0]
        return maior,menor,indices_maior,indices_menor



    