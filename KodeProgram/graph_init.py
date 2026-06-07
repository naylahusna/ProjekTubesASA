# Nama File : graph_init.py
# Deskripsi : Inisialisasi graph
# Nama : Nayla Husna - 24060124140158
# Kelas : A


import math

INF = 9999

# Penamaan Node
NODE_NAMES = {
    0: "1 (Depot)", 1: "2", 2: "3", 3: "4",
    4: "5", 5: "6", 6: "7", 7: "8",
    8: "9", 9: "10", 10: "11", 11: "12"
}

# Koordinat Node (x, y) untuk perhitungan heuristik
NODE_COORDS = {
    0:  (400, 600),   
    1:  (500, 650),   
    2:  (900, 450),   
    3:  (1000, 750),  
    4:  (550, 950),   
    5:  (480, 800),   
    6:  (100, 850),   
    7:  (150, 650),   
    8:  (150, 400),   
    9:  (0, 150),     
    10: (300, 0),     
    11: (400, 350)    
}

# Adjacency Matrix (dalam meter)
adj_matrix = [
    #   1    2    3    4    5    6    7    8    9   10   11   12
    [   0, 200, INF, INF, INF, INF, INF, 300, INF, INF, INF, 200], # 1
    [ 200,   0, 300, INF, INF, 400, INF, INF, INF, INF, INF, INF], # 2
    [ INF, 300,   0, 200, INF, INF, INF, INF, INF, INF, INF, INF], # 3
    [ INF, INF, 200,   0, 200, INF, INF, INF, INF, INF, INF, INF], # 4
    [ INF, INF, INF, 200,   0, 200, INF, INF, INF, INF, INF, INF], # 5
    [ INF, 400, INF, INF, 200,   0, 250, INF, INF, INF, INF, INF], # 6
    [ INF, INF, INF, INF, INF, 250,   0, 200, INF, INF, INF, INF], # 7
    [ 300, INF, INF, INF, INF, INF, 200,   0, 200, INF, INF, INF], # 8
    [ INF, INF, INF, INF, INF, INF, INF, 200,   0, 200, 400, 300], # 9  
    [ INF, INF, INF, INF, INF, INF, INF, INF, 200,   0, 250, 350], # 10 
    [ INF, INF, INF, INF, INF, INF, INF, INF, 400, 250,   0, 200], # 11 
    [ 200, INF, INF, INF, INF, INF, INF, INF, 300, 350, 200,   0], # 12 
]

# Untuk menghitung nilai heuristik (h)
def get_heuristic(node, goal):
    x1, y1 = NODE_COORDS[node]
    x2, y2 = NODE_COORDS[goal]
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return round(distance, 2)

# tabel heuristik
def show_heuristic_table(goal):
    print(f"\n[INFO] Tabel Estimasi Jarak Heuristik (h) ke {NODE_NAMES[goal]}:")
    print("-" * 60)
    for i in range(len(NODE_NAMES)):
        h_val = get_heuristic(i, goal)
        print(f"Dari Titik {NODE_NAMES[i]:<15} -> {h_val} meter")
    print("-" * 60)
    