import osmnx as ox

city_name = "Любляна, Словения"
G = ox.graph_from_place(city_name, network_type="drive")

ox.save_graphml(G, filepath="lublana_network.graphml")