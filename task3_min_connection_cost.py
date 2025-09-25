# Щоб мінімізувати сумарні витрати з’єднання, завжди потрібно з’єднувати два найкоротші кабелі першими.
# Це правило гарантує мінімальні витрати, оскільки найдешевше об’єднувати короткі кабелі на ранніх етапах.
# Для цього використовується мінімальна купа (heap), яка дозволяє ефективно знаходити два найменші елементи.
# Алгоритм має складність O(n log n), де n — кількість кабелів.

import heapq

def min_total_connection_cost(cables):
    """
    Обчислює мінімальні загальні витрати на з'єднання кабелів.

    Parameters:
    cables (list): Список довжин кабелів.

    Returns:
    int: Мінімальні загальні витрати на з'єднання.
    """
    if not cables:
        return 0
    
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    print("Довжини кабелів:", cables)
    print("Мінімальні загальні витрати на з'єднання кабелів:", min_total_connection_cost(cables))  # 29 