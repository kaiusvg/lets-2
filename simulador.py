import json
import sys

class TM:
    def __init__(self, spec_file):
        self.spec = self.carregar_spec(spec_file)
        self.estado_inicial = self.spec["initial"]
        self.estados_finais = set(self.spec["final"])
        self.branco = self.spec["white"]
        self.transicoes = self.criar_dicionario_transicoes(self.spec["transitions"])

    def carregar_spec(self, path):
        with open(path, "r") as f:
            return json.load(f)

    def criar_dicionario_transicoes(self, transicoes):
        d = {}
        for t in transicoes:
            d[(t["from"], t["read"])] = (t["to"], t["write"], t["dir"])
        return d

    def simular(self, fita):
        fita = list(fita)
        estado = self.estado_inicial
        cabeca = 0

        while estado not in self.estados_finais:
            simbolo = fita[cabeca] if cabeca < len(fita) else self.branco
            chave = (estado, simbolo)
            if chave not in self.transicoes:
                break  # Não existe transição → halt
            proximo_estado, escrever, mover = self.transicoes[chave]

            
            if cabeca >= len(fita):
                fita.append(self.branco)
            fita[cabeca] = escrever
            estado = proximo_estado

            
            if mover == "R":
                cabeca += 1
                if cabeca >= len(fita):
                    fita.append(self.branco)
            elif mover == "L":
                cabeca -= 1
                if cabeca < 0:
                    fita.insert(0, self.branco)
                    cabeca = 0

        resultado = 1 if estado in self.estados_finais else 0
        print(resultado)
        return "".join(fita).strip()

def main(spec_file, input_file, output_file):
    tm = TM(spec_file)

    with open(input_file, "r") as f:
        entradas = [line.strip() for line in f if line.strip()]

    with open(output_file, "w") as f:
        for entrada in entradas:
            fita_final = tm.simular(entrada)
            f.write(f"{fita_final}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python simulador.py <arquivo_maquina.json> <arquivo_entrada.txt> <arquivo_saida.txt>")
        sys.exit(1)

    spec_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    main(spec_file, input_file, output_file)
