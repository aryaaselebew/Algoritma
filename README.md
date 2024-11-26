#Arya Nanda Putra
#Nim: f55123087
#Kelas: C

Hasil Analisis Quiz 2
-Hasil Analisis Naive Method Pada file naive.py, dataset berupa 50 bilangan acak dalam rentang 0-100 diurutkan menggunakan metode Naive dengan pendekatan bucket sorting. Hasil menunjukkan bahwa waktu eksekusi untuk menyortir dataset adalah sekitar 0.00002 detik, dengan hasil sorting yang benar sesuai urutan dari terkecil ke terbesar. Proses sorting berjalan cepat karena metode ini langsung mendistribusikan bilangan ke dalam bucket berdasarkan nilainya, sehingga iterasi untuk penggabungan kembali sangat sederhana. Metode ini efisien untuk dataset kecil dengan rentang nilai yang tidak terlalu besar.

-Hasil Analisis Conquer Method Pada kode program conquer.py, yang menggunakan metode Merge Sort, program berhasil menyortir 50 bilangan acak menggunakan pendekatan rekursif dengan kompleksitas waktu 𝑂(𝑛log𝑛). Meskipun sedikit lebih lambat dibandingkan dengan metode bucket sorting, dengan waktu eksekusi sekitar 0.00011 detik, Merge Sort tetap lebih efisien dan stabil pada dataset yang lebih besar. Hasil sorting dari program ini juga menunjukkan urutan yang benar. Keunggulan utama dari Merge Sort adalah kemampuannya untuk menangani dataset besar secara efisien, menjadikannya pilihan yang lebih baik untuk kasus sorting dengan data yang lebih kompleks.
