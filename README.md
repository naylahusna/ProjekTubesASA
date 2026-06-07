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

Cara termudah untuk menjalankan program ini adalah melalui **Google Colab** agar tidak perlu menginstal *library* secara manual.

1. Buka tautan Google Colab berikut: **[https://colab.research.google.com/drive/1NUZrYeYl5PFWUVsi5dDyZjMRdZbi4Gcf]**
2. Klik tombol **"Run All"** (atau tekan `Ctrl + F9`) untuk menjalankan seluruh sel kode dari atas sampai bawah.
3. Gulir ke bagian bawah (*Cell Main*) untuk melihat teks *tracing* dan visualisasi grafiknya.

**Menjalankan di Komputer Lokal (VS Code / Jupyter Notebook):**
Pastikan kamu sudah menginstal Python dan *library* yang dibutuhkan:
```bash
pip install matplotlib numpy seaborn
