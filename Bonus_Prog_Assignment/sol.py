import sys
import math
import random

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def parse_input():
    mode = input().strip()
    n = int(input().strip())

    coordinates = []
    for _ in range(n):
        x, y = map(float, input().strip().split())
        coordinates.append((x, y))

    distance_matrix = []
    for _ in range(n):
        row = list(map(float, input().strip().split()))
        distance_matrix.append(row)

    return mode, n, coordinates, distance_matrix

def nearest_neighbor_tour(n, distance_matrix):
    visited = [False] * n
    tour = [0]  # Start at the first city
    visited[0] = True

    for _ in range(1, n):
        last = tour[-1]
        next_city = min((distance_matrix[last][j], j) for j in range(n) if not visited[j])[1]
        tour.append(next_city)
        visited[next_city] = True

    return tour

def calculate_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour)):
        cost += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return cost

def two_opt(tour, distance_matrix):
    n = len(tour)
    best_tour = tour
    best_cost = calculate_tour_cost(tour, distance_matrix)

    improved = True
    while improved:
        improved = False
        for i in range(n - 1):
            for j in range(i + 2, n):
                if j == i + 1:
                    continue
                new_tour = tour[:i + 1] + tour[i + 1:j + 1][::-1] + tour[j + 1:]
                new_cost = calculate_tour_cost(new_tour, distance_matrix)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True
    return best_tour

def simulated_annealing(tour, distance_matrix, initial_temp=1000, cooling_rate=0.995, max_iter=10000):
    n = len(tour)
    current_tour = tour
    current_cost = calculate_tour_cost(tour, distance_matrix)
    best_tour = list(tour)
    best_cost = current_cost

    temp = initial_temp
    for _ in range(max_iter):
        if temp < 1e-3:
            break

        # Generate a neighboring solution
        i, j = sorted(random.sample(range(n), 2))
        new_tour = current_tour[:i] + current_tour[i:j + 1][::-1] + current_tour[j + 1:]
        new_cost = calculate_tour_cost(new_tour, distance_matrix)

        # Decide whether to accept the new solution
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_tour, current_cost = new_tour, new_cost
            if current_cost < best_cost:
                best_tour, best_cost = current_tour, current_cost

        # Cool down
        temp *= cooling_rate

    return best_tour

def main():
    mode, n, coordinates, distance_matrix = parse_input()

    # Step 1: Generate initial tour using Nearest Neighbor
    initial_tour = nearest_neighbor_tour(n, distance_matrix)

    # Step 2: Optimize using 2-opt
    optimized_tour = two_opt(initial_tour, distance_matrix)

    # Step 3: Further refine using Simulated Annealing
    final_tour = simulated_annealing(optimized_tour, distance_matrix)

    # Output the final tour
    print(" ".join(map(str, final_tour)))

if __name__ == "__main__":
    main()
