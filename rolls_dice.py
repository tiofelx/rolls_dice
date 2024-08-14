import random

def lancar_dado(n_lados):
    return random.randint(1, n_lados)

def simulador_lancamento():
    try:
        n_lados = int(input("Digite o número de lados do dado: "))
        if n_lados < 2:
            print("Um dado deve ter pelo menos 2 lados.")
            return

        n_lancamentos = int(input("Quantas vezes deseja lançar o dado? "))
        print("\nResultados dos lançamentos:")

        resultados = []
        for _ in range(n_lancamentos):
            resultado = lancar_dado(n_lados)
            resultados.append(resultado)
            print(f"Lançamento {_+1}: {resultado}")

        print("\nResumo dos resultados:")
        for lado in range(1, n_lados + 1):
            print(f"Lado {lado}: {resultados.count(lado)} vezes")

    except ValueError:
        print("Por favor, insira um número válido.")

# Executar o simulador
simulador_lancamento()