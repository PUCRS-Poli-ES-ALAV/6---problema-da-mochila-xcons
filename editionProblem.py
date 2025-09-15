from typing import Tuple

# Variável global para contar chamadas recursivas
counter: int = 0

def edit_distance_recursive(s1: str, s2: str, i: int, j: int) -> int:
    global counter
    counter += 1

    # Casos base
    if i == 0:
        return j
    if j == 0:
        return i

    # Se os caracteres são iguais, nenhuma operação necessária
    if s1[i - 1] == s2[j - 1]:
        return edit_distance_recursive(s1, s2, i - 1, j - 1)

    # Três operações possíveis: inserção, remoção, substituição
    insert_op = edit_distance_recursive(s1, s2, i, j - 1)
    remove_op = edit_distance_recursive(s1, s2, i - 1, j)
    replace_op = edit_distance_recursive(s1, s2, i - 1, j - 1)

    return 1 + min(insert_op, remove_op, replace_op)

def compute_edit_distance(s1: str, s2: str) -> Tuple[int, int]:
    """
    Calcula a distância de edição entre s1 e s2 de forma recursiva.
    Retorna (distância, número de chamadas recursivas).
    """
    global counter
    counter = 0
    distance = edit_distance_recursive(s1, s2, len(s1), len(s2))
    return distance, counter

# Execução principal
if __name__ == "__main__":
    s1 = "Casablanca"
    s2 = "Portentoso"

    print("Calculando distância de edição (força bruta recursiva)...")
    dist, calls = compute_edit_distance(s1, s2)
    print(f"\n Resultado:")
    print(f"Distância de edição entre '{s1}' e '{s2}': {dist}")
    print(f"Número de chamadas recursivas: {calls}")
