from collections import defaultdict, deque


def parse_input(file_path):
    with open(file_path, 'r') as f:
        content = f.read().strip()

    sections = content.split("\n\n")
    rules = [tuple(map(int, line.split("|")))
             for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(",")))
               for line in sections[1].splitlines()]

    return rules, updates


def build_graph(rules, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)

    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    return graph, in_degree


def is_valid_order(graph, in_degree, update):
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return len(sorted_order) == len(update), sorted_order


def solve(file_path):
    rules, updates = parse_input(file_path)
    total_middle_sum = 0

    for update in updates:
        graph, in_degree = build_graph(rules, update)
        valid, sorted_order = is_valid_order(graph, in_degree, update)
        if valid:
            middle_page = sorted_order[len(sorted_order) // 2]
            total_middle_sum += middle_page

    return total_middle_sum


file_path = "input1.txt"
result = solve(file_path)
print(result)
