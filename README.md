# ProjekTubesASA
Kode Program Tugas Besar ASA

## Sistem Navigasi Kurir Last-Mile Delivery

Proyek ini berisi implementasi komputasional dan analisis algoritma pencarian untuk menyelesaikan permasalahan optimasi rute kurir pada tahap *last-mile delivery* e-commerce.

Permasalahan dimodelkan ke dalam graf berukuran 12 titik (1 Depot dan 11 Pelanggan) dan dibagi menjadi dua skenario penyelesaian utama:
1. **Pathfinding (Pencarian Rute Tunggal):** Mencari rute terpendek dari Depot ke satu pelanggan tertentu.
2. **Traveling Salesperson Problem / TSP (Rute Keliling):** Menyusun urutan rute keliling ke seluruh titik pelanggan dan kembali lagi ke Depot.

### Algoritma yang Dievaluasi
Proyek ini membandingkan 5 algoritma pencarian berdasarkan Total Jarak, Jumlah Evaluasi Node, dan Waktu Komputasi:
* **Uniform Cost Search (UCS)** - *Pathfinding*
* **Greedy Best-First Search (GBFS)** - *Pathfinding*
* **A-Star (A*)** - *Pathfinding*
* **Branch and Bound (B&B)** - *TSP*
* **Nearest Neighbor Heuristic (NNH)** - *TSP*

### Fitur Utama
* **Tracing Otomatis:** Menampilkan langkah-langkah (*step-by-step*) komputasi dari setiap algoritma saat membongkar *node*.
* **Visualisasi Komparatif:** Menghasilkan grafik untuk membandingkan performa algoritma.
* **Metrik Akurat:** Menghitung waktu eksekusi program dalam satuan milidetik (ms).

### Cara Menjalankan Program

Dapat menggunakan VSCode atau Terminal lainnya, dan juga melalui Google Colab dengan tautan dibawah ini:
**[https://colab.research.google.com/drive/1NUZrYeYl5PFWUVsi5dDyZjMRdZbi4Gcf]**

Jika menggunakan terminal, bisa mnegikuti perintah dan pilihan yang diberikan oleh program.
