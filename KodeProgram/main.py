# Nama File : main.py
# Deskripsi : Menu utama untuk menjalankan sistem navigasi kurir last-mile delivery
# Nama : Nayla Husna - 24060124140158
# Kelas : A

import os
import time
from graph_init import NODE_NAMES, adj_matrix,  show_heuristic_table
from Algoritma import ucs, gbfs, astar, nearest_neighbor, branch_and_bound

def measure_time(algo_func, *args):
    start_time = time.perf_counter()
    result = algo_func(*args)
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000 # (ms)
    return result, exec_time

def print_result(algo_name, path, cost, explored_order, exec_time=None):
    print(f"\n================ HASIL {algo_name} ================")
    if path:
        rute_str = ' -> '.join([NODE_NAMES[n] for n in path])
        print(f"Jalur Terpilih  : {rute_str}")
    
        if exec_time is not None:
            print(f"Waktu Eksekusi  : {exec_time:.4f} ms")

        if explored_order and isinstance(explored_order, list):
            tampil_eval = explored_order[:20]
            eval_str = ', '.join([NODE_NAMES[n].split(' ')[0] for n in tampil_eval])
            if len(explored_order) > 20:
                eval_str += " ... (+)"
            print(f"Urutan Evaluasi : {eval_str}")
        
        elif isinstance(explored_order, int):
            print(f"Total Evaluasi  : {explored_order} node")
    else:
        print("Rute tidak ditemukan atau terjebak jalan buntu")

def main():
    while True:
        print("====================================================")
        print("    SISTEM NAVIGASI KURIR LAST-MILE DELIVERY        ")
        print("====================================================")
        print("=== Pilih Algoritma ===")
        print("1. PATHFINDING (UCS, GBFS, A*)")
        print("2. TSP ROUTING (BNB, NNH)")
        print("0. Keluar ")
        
        mode = input("\nMasukkan pilihan mode (0/1/2): ")
        
        if mode == '0':
            print("\nTerima kasih ")
            break
            
        elif mode == '1': 
            print("\n" + "-"*50)
            print("Daftar Lokasi Tersedia:")
            for key, value in NODE_NAMES.items():
                print(f"[{key+1}] {value:<12}", end="\t") 
                if (key + 1) % 4 == 0: print()
            print("" + "-"*50)
                
            try:
                goal_input = int(input("Masukkan Angka Titik Tujuan (2-12) : "))
                
                start = 0 
                goal = goal_input - 1
                
                if goal not in NODE_NAMES or goal == 0:
                    input("Input tidak valid! Harus angka 2-12. Tekan Enter untuk mengulang.")
                    continue
                
                show_heuristic_table(goal)

                (p_ucs, c_ucs, e_ucs), t_ucs = measure_time(ucs, start, goal)
                (p_gbfs, c_gbfs, e_gbfs), t_gbfs = measure_time(gbfs, start, goal)
                (p_astar, c_astar, e_astar), t_astar = measure_time(astar, start, goal)

                print_result("Uniform Cost Search (UCS)", p_ucs, c_ucs, e_ucs, t_ucs)
                print_result("Greedy Best-First Search (GBFS)", p_gbfs, c_gbfs, e_gbfs, t_gbfs)
                print_result("A-Star (A*)", p_astar, c_astar, e_astar, t_astar)

                print("\n================ KESIMPULAN PATHFINDING ================")
                print(f"{'Algoritma':<10} | {'Total Jarak (Cost)':<20} | {'Total Dieksplor':<15}")
                print("-" * 55)
                print(f"{'UCS':<10} | {str(c_ucs) + ' meter':<20} | {len(e_ucs)} titik")
                print(f"{'GBFS':<10} | {str(c_gbfs) + ' meter':<20} | {len(e_gbfs)} titik")
                print(f"{'A*':<10} | {str(c_astar) + ' meter':<20} | {len(e_astar)} titik")
                print("========================================================\n")

            except ValueError:
                input("Harap masukkan format angka! Tekan Enter")

        elif mode == '2': 
            print("\n" + "="*50)
            print("MODE TSP: Kurir berangkat dari Depot (1), mengunjungi")
            print("semua pelanggan (2-12) tepat 1x, dan pulang ke Depot.")
            print("="*50)
            
            start = 0 

            (p_nnh, c_nnh, e_nnh), t_nnh = measure_time(nearest_neighbor, start)
            (p_bnb, c_bnb, e_bnb), t_bnb = measure_time(branch_and_bound, adj_matrix, start)

            print_result("Nearest Neighbor Heuristic (NNH)", p_nnh, c_nnh, e_nnh, t_nnh)
            print_result("Branch and Bound (B&B)", p_bnb, c_bnb, e_bnb, t_bnb)

            print("\n================ KESIMPULAN TSP ROUTING ================")
            print(f"{'Algoritma':<25} | {'Total Jarak (Cost)':<20}")
            print("-" * 50)
            print(f"{'Nearest Neighbor (NNH)':<25} | {str(c_nnh) + ' meter':<20}")
            print(f"{'Branch & Bound (B&B)':<25} | {str(c_bnb) + ' meter':<20}")
            print("========================================================\n")
                
        input("Tekan Enter untuk kembali ke menu utama.")

if __name__ == "__main__":
    main()