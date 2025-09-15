def distEdProgDina(A: str, B: str):
    m = len(A)
    n = len(B)

    # Criar a matriz (m+1) x (n+1)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar contagem de iterações
    iteracoes = 0

    # Inicialização da primeira coluna
    for i in range(1, m + 1):
        matriz[i][0] = matriz[i - 1][0] + 1  # remoção
        iteracoes += 1

    # Inicialização da primeira linha
    for j in range(1, n + 1):
        matriz[0][j] = matriz[0][j - 1] + 1  # inserção
        iteracoes += 1

    # Preenchimento da matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            iteracoes += 1
            if A[i - 1] == B[j - 1]:
                custoExtra = 0  # match
            else:
                custoExtra = 1  # substituição

            matriz[i][j] = min(
                matriz[i - 1][j] + 1,      # remoção
                matriz[i][j - 1] + 1,      # inserção
                matriz[i - 1][j - 1] + custoExtra  # substituição/match
            )

    return matriz[m][n], iteracoes


def main():
    testes = [
       # string vazia e outra
        ("kitten", "sitting"),
        ("flaw", "lawn"),
        ("intention", "execution")
    ]

    print(f"{'A':<10} {'B':<10} {'Distância':<10} {'Iterações':<10}")
    for A, B in testes:
        dist, it = distEdProgDina(A, B)
        print(f"{A:<10} {B:<10} {dist:<10} {it:<10}")


if __name__ == "__main__":
    main()
