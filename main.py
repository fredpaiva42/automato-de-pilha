import json


class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        self.itens.pop()

    def topo(self):
        return self.itens[-1]


class APND:
    def __init__(self):
        self.estados = []
        self.alfabeto_pilha = []
        self.estado_inicial = None
        self.simbolo_inicial = None
        self.estados_finais = []
        self.transicoes = []

    def verificar_cadeia(self, entrada):
        pilha = Pilha()
        estado_atual = self.estado_inicial
        simbolo_atual = self.simbolo_inicial
        simbolos_a_empilhar = []
        pilha.empilhar(self.simbolo_inicial)
        entrada += 'e'

        for simbolo in entrada:
            transicao_existe = False
            for regra in self.transicoes:
                if regra[0] == estado_atual and regra[1] == simbolo and regra[2] == simbolo_atual:
                    transicao_existe = True
                    estado_atual = regra[3]
                    simbolos_a_empilhar = regra[4]
                    break

            if transicao_existe:
                if simbolos_a_empilhar != "e":
                    pilha.desempilhar()
                    for s in simbolos_a_empilhar[::-1]:
                        pilha.empilhar(s)
                if simbolos_a_empilhar == "e":
                    pilha.desempilhar()
                simbolo_atual = pilha.topo()
            else:
                return False

        return estado_atual in self.estados_finais


def main():
    with open("apnd1.json", "r") as apnd_file:
        dados = json.load(apnd_file)

    for i, dado in enumerate(dados):
        apnd = APND()
        apnd.estados = dado["estados"]
        apnd.alfabeto_pilha = dado["alfabeto_pilha"]
        apnd.estado_inicial = dado["estado_inicial"]
        apnd.simbolo_inicial = dado["simbolo_inicial"]
        apnd.estados_finais = dado["estados_finais"]
        apnd.transicoes = dado["transicoes"]

        cadeia_entrada = input("Informe a cadeia que deve ser verificada no APND: ")

        if apnd.verificar_cadeia(cadeia_entrada):
            print("Cadeia aceita pelo APND.")
        else:
            print("A cadeia não é aceita pelo APND.")


if __name__ == '__main__':
    main()

# apnd 1 é a^n b^n
# apnd 2 é a^n b^n+1
# apnd 3 é a^n b^m c^n
# apnd 4 é aX
