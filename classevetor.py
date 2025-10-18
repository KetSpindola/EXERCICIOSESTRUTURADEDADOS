#Classe vetor
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
    def entrada_vetor(self):
        if not self.esta_cheia():
            entrada_usuario = int(input("Digite um número: "))
            self.vetor[self.fim] = entrada_usuario
            print(f"Número {entrada_usuario} incluido com sucesso no índice {self.fim}")
            self.fim += 1
        else:
            print("-> O vetor esta cheio.")

    #2
    #printando os itens do vetor
    def printar(self):
        if not self.esta_vazio():
            print("Printando dados.")
            for i in range (self.fim):
                print(f"| {self.vetor[i]} |", end="")
        else:
            print("-> O vetor esta vazio.")

    #3
    #printando de tras para frente os itens do vetor
    def printar_trasfrente(self):
        if not self.esta_vazio():
            print("Printando dados de trás para frente.")
            for i in range(self.fim-1,-1,-1):
                print(f"{self.vetor[i]}")
        else:
            print("-> O vetor esta vazio.")

    #4
    #retorna quantas vezes determinado número consta no vetor
    def frequencia_valor(self, valor):
        contador = 0
        for i in range (self.fim):
            if self.vetor[i] == valor:
                contador += 1
        return contador
    
    #5
    #retorna os indices que determinado número se encontra
    def retorna_indices(self,valor):
        vetor_indices = []
        for i in range(self.fim):
            if self.vetor[i] == valor:
                vetor_indices.append(i)
    
        return vetor_indices
    
    #substitui determinado valor por outro
    def troca_valor(self):
        if not self.esta_vazio():
            valor_vetor = int(input("Entre com o valor a ser substituido: "))
            vetor_indices = self.retorna_indices(valor_vetor)
            if len(vetor_indices) > 0:
                novo_valor = int(input("Entre com o novo valor: "))
                for item in vetor_indices:
                    self.vetor[item]  = novo_valor
            else:
                print("Esse número não esta no vetor.")
        else:
            print("-> O vetor esta vazio.")

    #soma todos os números do vetor    
    def soma_valores(self):
        if not self.esta_vazio():
            somador = 0
            for i in range(self.fim):
                somador += self.vetor[i]
            return somador
        else:
            print("-> O vetor esta vazio.")

    #retorna o maior e menor valor        
    def encontra_maior(self):
        if not self.esta_vazio:
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

        print(f" Menor valor: {menor} nos indices: {indices_menor}")
        print(f" Maior valor: {menor} nos indices: {indices_maior}")
        
    

    