import itertools
import numpy as np


def check_isom(graph1, graph2):
    if len(graph1) != len(graph2) or len(graph1[0]) != len(graph2[0]):
        return False

    n = len(graph1)

    vertices = list(range(n))

    visited = set()

    # перебирання всіх можливих перестановок вершин
    for perm in itertools.permutations(vertices):
        if perm not in visited:
            visited.add(perm)  # додання нової перестановки до відвіданого набору

            # перевірка, чи є поточна перестановка дійсним ізоморфізмом
            mapping = {}
            is_valid = True
            for j in range(n):
                for k in range(n):
                    if graph1[j][k] != graph2[perm[j]][perm[k]]:
                        is_valid = False
                        break
                if not is_valid:
                    break
                mapping.setdefault(graph1[j][j], graph2[perm[j]][perm[j]])

                if mapping[graph1[j][j]] != graph2[perm[j]][perm[j]]:
                    is_valid = False
                    break
            if is_valid:
                return True

    return False  # графи не ізоморфні


# Головна функція для зчитування файлів і виводу результату
def main():
    with open('matrix1.txt', 'r') as f:
        n = int(f.readline())
        graph1 = [[int(x) for x in f.readline().split()] for i in range(n)]
        matr1 = np.matrix(graph1)
        print(f"Матриця суміжності першого графа: \n{matr1}")

    with open('matrix1.txt', 'r') as f:
        n = int(f.readline())
        graph2 = [[int(x) for x in f.readline().split()] for i in range(n)]
        matr2 = np.matrix(graph2)
        print(f"\nМатриця суміжності другого графа: \n{matr2}")

    # Перевірка чи графи ізоморфні
    if check_isom(graph1, graph2):
        print("\nГрафи ізоморфні.")
    else:
        print("\nГрафи не ізоморфні.")


if __name__ == "__main__":
    main()