def create_adjacency_list(N, M, combinations):
  adjacency_list = [[] for _ in range(N)]
  for combination in combinations:
    adjacency_list[combination[0] - 1].append(combination[1] - 1)
  return adjacency_list


N,M,K = map(int, input().split())

combinations = []

for _ in range(K):
    x,y = map(int, input().split())
    combinations.append([x, y])

graph = create_adjacency_list(N,M,combinations)

capacities = list(map(int, input().split()))

years = int(input())

for _ in range(years):
    r,p = map(int, input().split())
    products = 0
    available_capacities = capacities.copy()
    for product in graph:
      selected_assembly_line = -1
      for assembly_line in product:
        if available_capacities[assembly_line] > 0:
          selected_assembly_line = assembly_line
          break
      if selected_assembly_line != -1:
        products += 1
        available_capacities[selected_assembly_line] -= 1
    print(products)
    capacities[r-1] -= p
