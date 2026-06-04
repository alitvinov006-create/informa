import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import math
import heapq
from typing import Dict, List, Tuple

def haversine(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:

    lon1, lat1 = coord1
    lon2, lat2 = coord2
    R = 6371  # Радиус Земли в км

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def dijkstra(graph: Dict[Tuple[float, float], List[Tuple[Tuple[float, float], float]]],
             start: Tuple[float, float],
             end: Tuple[float, float]) -> Tuple[List[Tuple[float, float]], float, List[str]]:
    priority_queue = [(0, start)]

    distances = {_: float('inf') for _ in graph}
    previous = {start: None}

    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == end:
            break
        for neighbor, weight in graph.get(current_node, []):
            if neighbor in visited:
                continue
            new_distance = current_distance + weight
            if new_distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))
    if end not in distances:
        return [], float('inf'), []
    street_names = []
    path = []
    current = end

    while current:
        path.append(current)
        current = previous.get(current)
    path.reverse()
    total_distance = distances[end]
    return path, total_distance, street_names


def build_graph(edges: List[Tuple[Tuple[float, float], Tuple[float, float], str]]) -> Dict[
    Tuple[float, float], List[Tuple[Tuple[float, float], float]]]:
    graph = {}
    for start, end, _ in edges:
        dist = haversine(start, end)
        graph.setdefault(start, []).append((end, dist))
        graph.setdefault(end, []).append((start, dist))  # если граф неориентированный
    return graph


def read_graphml(file_path: str) -> Tuple[
    Dict[str, Tuple[float, float]], List[Tuple[Tuple[float, float], Tuple[float, float], str]]]:
    tree = ET.parse(file_path)
    root = tree.getroot()
    ns = {'g': 'http://graphml.graphdrawing.org/xmlns'}

    nodes = {}
    for node in root.findall('.//g:node', ns):
        node_id = node.get('id')
        x, y = None, None
        for data in node.findall('.//g:data', ns):
            if data.get('key') == 'd4':  # x координата (обычно longitude)
                x = float(data.text)
            elif data.get('key') == 'd5':  # y координата (обычно latitude)
                y = float(data.text)
        if x is not None and y is not None:
            nodes[node_id] = (x, y)

    edges = []
    for edge in root.findall('.//g:edge', ns):
        source = edge.get('source')
        target = edge.get('target')
        street_name = None

        for data in edge.findall('.//g:data', ns):
            if data.get('key') == 'd13':  # название улицы
                street_name = data.text if data.text else None

        if source in nodes and target in nodes:
            edges.append((nodes[source], nodes[target], street_name))

    return nodes, edges


def find_street_index(edges: List[Tuple[Tuple[float, float], Tuple[float, float], str]],
                      street_name_query: str) -> Tuple[int, str]:
    for i, (_, _, name) in enumerate(edges):
        if name and name.lower() == street_name_query.lower():
            return i, name
    return -1, None


def visualize_path_with_network(nodes, edges, path, street_names=None, figsize=(20, 20)):
    plt.figure(figsize=figsize)
    ax = plt.gca()

    # Все рёбра — серые
    all_lines = [(start, end) for start, end, _ in edges]
    lc = LineCollection(all_lines, linewidths=0.3, colors='gray', alpha=0.4)
    ax.add_collection(lc)

    # Путь — красный
    if path and len(path) > 1:
        path_lines = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        lc_path = LineCollection(path_lines, linewidths=2.0, colors='red', alpha=0.9)
        ax.add_collection(lc_path)

        # Отображаем названия улиц, если они заданы
        if street_names:
            for i in range(len(path) - 1):
                mid_point = ((path[i][0] + path[i + 1][0]) / 2, (path[i][1] + path[i + 1][1]) / 2)
                if i < len(street_names) and street_names[i]:
                    plt.text(mid_point[0], mid_point[1], street_names[i],
                             fontsize=8, color='blue', ha='center')

    ax.autoscale()
    plt.axis('equal')
    plt.title('Кратчайший маршрут')
    plt.xlabel('Долгота')
    plt.ylabel('Широта')
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def save_visualization(filename: str, dpi: int = 300) -> None:
    plt.savefig(filename, dpi=dpi, bbox_inches='tight')
    plt.close()


def visualize_path_with_network(nodes, edges, path, street_names=None, figsize=(20, 20)):
    plt.figure(figsize=figsize)
    ax = plt.gca()

    # Все рёбра — серые
    all_lines = [(start, end) for start, end, _ in edges]
    lc = LineCollection(all_lines, linewidths=0.3, colors='gray', alpha=0.4)
    ax.add_collection(lc)

    # Путь — красный
    if path and len(path) > 1:
        path_lines = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        lc_path = LineCollection(path_lines, linewidths=2.0, colors='red', alpha=0.9)
        ax.add_collection(lc_path)

        # Отображаем названия улиц, если они заданы
        if street_names:
            for i in range(len(path) - 1):
                mid_point = ((path[i][0] + path[i + 1][0]) / 2, (path[i][1] + path[i + 1][1]) / 2)
                if i < len(street_names) and street_names[i]:
                    plt.text(mid_point[0], mid_point[1], street_names[i],
                             fontsize=8, color='blue', ha='center')

    ax.autoscale()
    plt.axis('equal')
    plt.title('Кратчайший маршрут')
    plt.xlabel('Долгота')
    plt.ylabel('Широта')
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def visualize_only_path(path, figsize=(10, 10)):
    if not path or len(path) < 2:
        print("Маршрут слишком короткий или отсутствует.")
        return

    plt.figure(figsize=figsize)
    ax = plt.gca()

    path_lines = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    lc_path = LineCollection(path_lines, linewidths=2.5, colors='red', alpha=0.9)
    ax.add_collection(lc_path)

    ax.autoscale()
    plt.axis('equal')
    plt.title("Кратчайший маршрут")
    plt.xlabel("Долгота")
    plt.ylabel("Широта")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Пример использования

if __name__ == "__main__":
    nodes, edges = read_graphml("lublana_network.graphml")

    start_street_query = "Slovenska cesta"  # Название улицы для старта (пример)
    end_street_query = "Slovenska cesta"  # Название улицы для финиша (пример)

    start_index, start_street = find_street_index(edges, start_street_query)
    end_index, end_street = find_street_index(edges, end_street_query)

    if start_index == -1 or end_index == -1:
        print("Не удалось найти заданную улицу для начала или конца маршрута")
    else:
        start_node = edges[start_index][0]
        end_node = edges[end_index][1]

        graph = build_graph(edges)
        path, distance, street_names = dijkstra(graph, start_node, end_node)

        if not path:
            print("Путь не найден")
        else:
            print(f"Найден путь длиной {distance:.2f} км")
            print("Улицы на пути:", ", ".join(filter(None, street_names)))

            # 6. Визуализация маршрута
            visualize_path_with_network(nodes, edges, path, street_names)

#  	A–B: 3, A–C: 5, A–D: 2, B–C: 6, B–D: 4, C–D: 1. Найти путь: C → A

