# Kumpulan Tugas Konsep Jaringan

Nama : Ahmad Syahani
NRP  : 3125600058

## Tugas Bab 1

1. **Jelaskan pengertian jaringan komputer dengan menyebutkan empat unsur pokoknya.**  
Jaringan komputer merupakan sekumpulan perangkat mandiri (otonom) yang saling terkoneksi lewat media transmisi untuk berbagi data dan sumber daya menggunakan protokol tertentu. Empat elemen utamanya meliputi perangkat akhir (end devices), perangkat perantara (intermediary devices), media jaringan, dan aturan komunikasi (protokol).

2. **Apa yang dimaksud dengan perangkat otonom dalam definisi jaringan?**  
Perangkat otonom adalah alat yang memiliki kontrol, fungsi, dan kapabilitas komputasinya sendiri. Sifat mandiri ini tidak akan hilang walaupun perangkat tersebut sedang terhubung ke dalam sebuah jaringan.

3. **Bedakan data, sinyal, dan paket.**  
Data merupakan wujud asli dari informasi. Sinyal adalah representasi fisik atau gelombang dari data tersebut yang merambat di media transmisi. Sementara itu, paket adalah potongan kecil dari data yang sudah diberi tambahan informasi kontrol (header) agar bisa dikirimkan melintasi jaringan.

4. **Jelaskan perbedaan PAN, LAN, MAN, dan WAN tanpa hanya menggunakan ukuran jarak.**  
Selain cakupan area, keempatnya beda di sisi teknologi dan kepemilikan. PAN digunakan untuk perangkat pribadi seorang pengguna. LAN dikelola secara mandiri untuk area lokal terbatas (seperti gedung/kantor). MAN menghubungkan infrastruktur berskala kota/metropolitan. Sedangkan WAN mencakup geografis yang sangat luas dan biasanya membutuhkan layanan operator telekomunikasi (ISP).

5. **Apa perbedaan intranet, ekstranet, dan Internet publik?**  
Perbedaannya ada pada hak akses. Intranet itu privat, hanya bisa diakses oleh kalangan internal suatu organisasi. Ekstranet adalah intranet yang sebagian aksesnya dibuka untuk mitra bisnis atau pihak luar yang diizinkan. Internet publik bersifat terbuka dan bisa diakses oleh siapa saja di seluruh dunia.

6. **Mengapa Wi-Fi tidak dapat disamakan dengan Internet?**  
Wi-Fi hanyalah teknologi nirkabel pengganti kabel (media transmisi) untuk menghubungkan perangkat ke jaringan lokal (LAN). Memiliki koneksi Wi-Fi tidak otomatis menjamin adanya koneksi ke jaringan Internet global.

7. **Jelaskan perbedaan client, server, dan peer.**  
Client adalah pihak yang me-request atau meminta layanan. Server adalah pihak terpusat yang menyediakan layanan tersebut. Sedangkan peer adalah perangkat dalam jaringan (P2P) yang bisa berperan sebagai client yang meminta data dan server yang membagikan data di saat bersamaan.

8. **Apa perbedaan bandwidth, throughput, dan goodput?**  
Bandwidth adalah kapasitas maksimal teoritis saluran jaringan. Throughput adalah kecepatan transfer data riil yang terjadi (sudah termasuk data overhead). Goodput adalah kecepatan transfer dari data aplikasi itu sendiri tanpa menghitung ukuran header jaringan.

9. **Sebutkan empat komponen nodal delay.**  
Empat sumber delay pada node jaringan adalah delay pemrosesan (processing), delay antrean (queuing), delay transmisi (transmission), dan delay propagasi (propagation).

10. **Mengapa Web tidak sama dengan Internet?**  
Internet merujuk pada keseluruhan infrastruktur fisik jaringannya di seluruh dunia. Web hanyalah salah satu layanan atau aplikasi perangkat lunak (layanan dokumen HTML) yang beroperasi menumpang di atas infrastruktur Internet tersebut.

11. **Sebuah paket berukuran 1.000 byte dikirim melalui tautan 10 Mbps. Hitung transmission delay ideal paket tersebut. Jelaskan komponen delay yang belum tercakup.**  
Transmission delay idealnya adalah: (1.000 byte * 8) / 10.000.000 bps = 0,0008 detik atau 0,8 milidetik. Angka ini murni waktu dorong data ke kabel, belum memperhitungkan waktu pemrosesan router, lamanya paket mengantre, dan waktu tempuh rambatan sinyal (propagasi).

12. **Sebuah kampus memiliki koneksi Internet 2 Gbps, tetapi pengguna di satu lantai hanya memperoleh throughput rendah. Susun sedikitnya lima hipotesis yang tidak langsung menyalahkan koneksi ISP.**  
Beberapa kemungkinannya: (1) Ada interferensi sinyal pada Wi-Fi lokal, (2) Access Point terlalu padat pengguna, (3) Kerusakan atau limitasi pada switch lokal lantai tersebut, (4) Bandwidth di-limit (shaping) oleh admin jaringan kampus, atau (5) Spek perangkat pengguna memang lambat (bottleneck hardware).

13. **Bandingkan kebutuhan jaringan untuk transfer berkas cadangan dan panggilan video. Metrik apa yang paling penting bagi masing-masing aplikasi?**  
Transfer data backup butuh throughput yang besar dan memastikan data tidak rusak atau hilang sama sekali (reliabilitas). Sebaliknya, video call tidak terlalu menuntut ketepatan data 100%, tapi sangat butuh latensi (delay) sekecil mungkin dan tingkat variasi delay (jitter) yang rendah.

14. **Sebuah organisasi mempunyai dua koneksi Internet dari dua operator. Keduanya melewati tiang dan jalur ducting yang sama. Evaluasi kualitas redundansinya.**  
Redundansi ini sangat buruk secara fisik. Walaupun operator ISP-nya berbeda, risiko kegagalan fisik (single point of failure) masih tinggi. Jika tiang rubuh atau jalur kabel terpotong, kedua koneksi akan mati bersamaan.

15. **Jelaskan mengapa penambahan bandwidth tidak selalu mengurangi waktu akses ke server yang sangat jauh.**  
Menaikkan bandwidth hanya memperlebar "jalan" atau kapasitas transfer, tapi tidak meningkatkan kecepatan rambatan sinyal listrik atau cahaya (propagasi). Latensi utama ke server jauh diakibatkan oleh jarak tempuh fisiknya.

16. **Sebuah layanan tersedia 99,9% selama satu tahun. Hitung perkiraan maksimum durasi ketidaktersediaannya. Bandingkan dengan target 99,99%.**  
Tingkat ketersediaan 99,9% menoleransi waktu offline maksimal sekitar 8 jam 45 menit dalam setahun. Jika ditingkatkan ke 99,99%, toleransi downtime menyusut drastis menjadi maksimal sekitar 52 menit setahun.

17. **Analisis kelebihan dan kelemahan client–server serta P2P untuk distribusi berkas berukuran besar kepada ribuan pengguna.**  
Model client-server gampang dimanajemen namun server bisa overload (down) jika dibombardir banyak unduhan. P2P lebih tangguh dan kapasitas sebaran makin naik seiring banyaknya pengunduh, tapi sulit mengatur sekuritas serta tidak ada jaminan ketersediaan file utuhnya.

18. **Berikan contoh ketika topologi fisik dan topologi logis pada jaringan kampus berbeda.**  
Misalnya semua komputer dicolok pakai kabel ke satu switch pusat (fisiknya topologi Star). Namun secara logika lalu lintasnya dibuat terpisah menggunakan teknologi VLAN, sehingga interaksi komunikasinya seperti beda jaringan.

19. **Rancang klasifikasi kebutuhan jaringan kampus untuk mahasiswa, staf administrasi, tamu, kamera pengawas, dan laboratorium riset. Jelaskan alasan segmentasi dan aturan komunikasi utamanya.**  
Jaringan wajib disegmentasi per VLAN. Mahasiswa diberi kuota besar tapi dibatasi dari sistem internal. Staf Admin butuh akses ke sistem akademik (VLAN khusus yang aman). Tamu dikasih akses internet saja yang terisolasi. CCTV punya jalur lokal tersendiri tanpa internet publik. Lab dipisah agar aktivitas riset/eksperimen tidak merusak stabilitas jaringan kampus. Semua dibatasi aturan firewall.

20. **Evaluasi pernyataan: “Jaringan internal tidak memerlukan enkripsi karena sudah dilindungi firewall.” Gunakan prinsip kerahasiaan, integritas, dan ketersediaan.**  
Pernyataan ini salah fatal. Firewall hanya menjaga pintu gerbang luar. Ancaman bisa dari dalam (misal laptop karyawan kena malware). Tanpa enkripsi, kerahasiaan dan integritas data lokal bisa disadap atau dimodifikasi oleh perangkat internal yang terinfeksi.

21. **Diskusikan mengapa Internet dapat berkembang tanpa otoritas teknis pusat tunggal. Jelaskan manfaat serta risikonya.**  
Karena pengelolaannya disebar dan mengandalkan konsensus terbuka (seperti dari IETF), inovasi jadi lebih cepat dan tidak dimonopoli. Risikonya, jika ada miskonfigurasi perutean (contoh kebocoran BGP), dampaknya bisa meluas secara global dan tidak ada satu otoritas pun yang bisa langsung mematikannya secara terpusat.

22. **Bandingkan circuit switching dan packet switching untuk layanan suara. Jelaskan mengapa suara modern tetap dapat berjalan pada jaringan paket.**  
Circuit switching mengunci satu jalur khusus secara utuh sehingga menjamin kualitas tapi boros sumber daya. Packet switching lebih hemat karena jalur dipakai bergantian. Layanan suara modern (VoIP) mulus di jaringan paket berkat implementasi QoS (Quality of Service) yang memberi prioritas pada paket lalu lintas suara.

23. **Ambil satu keluhan nyata atau hipotetis berupa “Internet lambat”. Susun prosedur pengumpulan bukti, pengujian hipotesis, dan kriteria keberhasilan perbaikannya.**  
Prosedur diagnosa: Pertama, kumpulkan data (cek ping, traceroute). Kedua, tes kecepatan lokal menuju switch/AP, lalu tes ke luar (Internet) untuk mencari lokasi bottleneck. Ketiga, hipotesakan masalahnya (misal DNS lemot). Terakhir, ubah DNS dan uji kembali. Perbaikan sukses jika latency stabil dan packet loss 0%.

24. **Kunjungi statistik IPv6 Google atau sumber pengukuran APNIC. Catat tanggal, definisi metrik, populasi yang diukur, dan nilai untuk Indonesia. Jelaskan mengapa angka dari dua sumber dapat berbeda.**  
Statistik dari Google dan APNIC sering berbeda akibat metode pengambilan data. Google mendasarkan pengukurannya pada perangkat pengguna yang benar-benar tersambung dan berinteraksi langsung ke server Google via IPv6. Di sisi lain, APNIC memakai script iklan pihak ketiga untuk mengetes kapabilitas perangkat secara pasif.

25. **Buat argumen mengenai penggunaan satelit orbit rendah sebagai koneksi utama atau cadangan bagi kampus di wilayah terpencil. Nilai kinerja, biaya, ketergantungan cuaca, pengelolaan, dan keamanan.**  
Satelit orbit rendah (LEO) cocok jadi tulang punggung atau cadangan di pelosok sebab latensinya minim dibanding satelit tradisional. Minus utamanya ada pada biaya perangkat dan langganan bulanan, sangat dipengaruhi kondisi cuaca (hujan/awan tebal), dan perlu pengamanan ekstra untuk parabolanya.

26. **Jelaskan bagaimana otomatisasi jaringan dapat meningkatkan konsistensi sekaligus memperbesar dampak kesalahan. Usulkan kontrol teknis dan proses untuk mengurangi risiko tersebut.**  
Script otomatis memastikan semua perangkat terkonfigurasi sama secara cepat. Namun kalau ada salah ketik, semua perangkat bakal mati seketika. Solusinya adalah melakukan testing di lab, menerapkan skema peluncuran bertahap (canary release), dan membuat sistem auto-rollback jika terdeteksi gagal ping.

27. **Tentang kabel UTP**  
Kabel UTP dibagi berdasar frekuensi dan speed. Cat 1 untuk telepon lawas. Cat 2-4 untuk sistem jadul semacam Token Ring. Cat 5 dan 5e lumrah untuk 1 Gbps. Cat 6 dan 6a mendukung transmisi hingga 10 Gbps (isolasi lebih rapat). Cat 7/7a juga 10 Gbps tapi pelindung interferensinya jauh lebih tebal, sedangkan Cat 8 sanggup menangani kecepatan 25-40 Gbps untuk koneksi data center jarak dekat.

28. **Standar Wi-Fi abgn**  
Protokol ini disusun IEEE (802.11). Versi 802.11b (Wi-Fi 1) tembus 11 Mbps di frekuensi 2,4 GHz. Versi 802.11a (Wi-Fi 2) pakai jalur 5 GHz dengan kecepatan 54 Mbps. Versi 802.11g (Wi-Fi 3) berjalan di 2,4 GHz tapi tembus 54 Mbps. Versi 802.11n (Wi-Fi 4) sudah dual band (2,4 GHz dan 5 GHz) serta mampu mencapai 600 Mbps menggunakan antena MIMO.

## Tugas Bab 2

1. **Jelaskan alasan komunikasi jaringan disusun berlapis.**  
Supaya desainnya modular dan tidak membingungkan (abstraksi). Dengan membagi proses komunikasi menjadi lapisan-lapisan kecil, pembuat hardware dan software jaringan tidak perlu pusing memikirkan cara kerja detail dari lapisan lainnya, cukup fokus di tugas lapisannya sendiri.

2. **Bedakan layanan, antarmuka, dan protokol.**  
Layanan adalah fungsi atau fasilitas yang ditawarkan sebuah layer untuk layer di atasnya. Antarmuka (interface) adalah pintu masuk/cara layer atas meminta layanan tersebut. Protokol adalah aturan komunikasi teknis antara layer yang selevel pada perangkat pengirim dan penerima.

3. **Sebutkan tujuh lapisan OSI dari bawah ke atas beserta fungsi utamanya.**  
- Physical: ngurusin sinyal mentah (bit) masuk media kabel/wireless.  
- Data Link: ngurus kiriman data (frame) per hop via MAC Address.  
- Network: cari rute terbaik dan urus alamat logis (IP).  
- Transport: mastiin transmisi data end-to-end terjamin (segmentasi).  
- Session: bikin, ngejaga, dan mengakhiri sesi interaksi.  
- Presentation: enkripsi, kompresi, dan penerjemahan format data.  
- Application: tempat interaksi software pengguna ke jaringan (HTTP, FTP).

4. **Sebutkan empat lapisan model TCP/IP.**  
Mulai dari bawah: Network Access, Internet, Transport, dan Application.

5. **Mengapa model TCP/IP kadang disajikan sebagai lima lapisan?**  
Terkadang Network Access layer dipisah menjadi dua lapisan (Data Link dan Physical) seperti model OSI. Hal ini dilakukan untuk kebutuhan edukasi biar mahasiswa lebih gampang bedain urusan hardware pemancar (fisik) dengan pengalamatan hardware lokal (MAC).

6. **Apa perbedaan frame, IP packet, TCP segment, dan UDP datagram?**  
Ini semua cuma nama bungkusan (PDU). Frame itu bungkusan lapis Data Link. Packet IP itu bungkusan lapis Network. Segment TCP itu bungkusan Transport yang sistem pengirimannya dijaga kuat. Datagram UDP itu bungkusan Transport tapi untuk pengiriman cepat tanpa jaminan pasti sampai.

7. **Definisikan header, trailer, dan payload.**  
Header adalah data tambahan pembawa instruksi yang ditaruh di depan paket. Trailer itu instruksi (biasanya untuk cek error) di ekor/belakang paket. Payload adalah data asli/inti yang beneran mau dikirim oleh user.

8. **Jelaskan enkapsulasi dan dekapsulasi.**  
Enkapsulasi itu proses ngebungkus data dengan header/trailer dari lapisan atas ke bawah waktu lagi ngirim. Dekapsulasi adalah proses ngebuka bungkusan itu satu per satu dari bawah ke atas ketika paketnya udah nyampe di penerima.

9. **Apa fungsi multiplexing dan demultiplexing?**  
Multiplexing itu menyatukan banyak jenis data aplikasi yang berbeda ke dalam satu pipa pengiriman jaringan bawahnya. Demultiplexing itu waktu paket datang, penerima menyortir paket-paket itu berdasar port supaya nyasar ke aplikasi yang tepat.

10. **Mengapa OSI tidak boleh dianggap sebagai spesifikasi implementasi?**  
OSI cuma kerangka teoritis (model konseptual) buat bahan rujukan akademis aja. Di dunia nyata, vendor software nggak bikin kode sesuai layer OSI plek-ketiplek karena kurang praktis dan lambat diproses komputer.

11. **Petakan HTTP, TLS, TCP, UDP, QUIC, IPv6, ICMP, Ethernet, Wi-Fi, dan DNS ke model TCP/IP. Tandai protokol yang pemetaannya memerlukan penjelasan.**  
- Application: HTTP, DNS.  
- Transport: TCP, UDP, QUIC (meski jalan di UDP, fungsinya ambil alih kendali transpor).  
- Internet: IPv6, ICMP (numpang di dalam paket IP tapi kerjanya di level IP).  
- Network Access: Ethernet, Wi-Fi.  
- Antara Application & Transport: TLS (Sering dianggap Presentation).

12. **Gambarkan enkapsulasi permintaan DNS melalui UDP, IPv4, dan Ethernet. Sebutkan pengenal yang digunakan pada setiap batas.**  
Data (DNS) dibungkus UDP (pakai Port 53). Bungkusan UDP masuk ke IPv4 (ditandai kolom Protocol 17). Terakhir masuk ke Ethernet (ditandai kolom EtherType `0x0800` plus nomor MAC).

13. **Ulangi soal sebelumnya untuk HTTP/3 melalui QUIC. Jelaskan mengapa QUIC tetap dapat dianggap transport meskipun menggunakan UDP.**  
Data HTTP/3 dibungkus pakai QUIC (sudah include keamanan TLS 1.3), lalu dibungkus paket UDP port 443. Biarpun di atas UDP, QUIC masuk kategori Transport karena dia ngambil alih fungsi penjaminan data, manajemen urutan, dan pengontrol kongesti layaknya TCP.

14. **Dua host berada pada subnet berbeda. Jelaskan header mana yang berubah dan tetap ketika paket melewati satu router, dengan mengabaikan NAT.**  
Isi IP Header (Sumber & Tujuan IP) tidak diubah sama sekali oleh router (kecuali nilai TTL yang dipotong 1). Namun, Header Datalink (MAC Address) dibongkar dan diganti total menyesuaikan kartu jaringan router dan tujuan hop selanjutnya.

15. **Jelaskan perubahan analisis apabila router tersebut juga melakukan NAT/PAT.**  
Kalau fitur NAT aktif, IP asal dan Port pengirim akan diganti oleh router menjadi IP Publik milik si router itu. Otomatis, checksum di header Internet dan Transport wajib dikalkulasi ulang.

16. **Sebuah capture menunjukkan checksum TCP salah pada paket keluar, tetapi tidak ada gangguan komunikasi. Ajukan hipotesis yang berkaitan dengan NIC offload.**  
Aplikasi sniffer (seperti Wireshark) mencegat paket pada sistem operasi sebelum masuk hardware lancard (NIC). Padahal, tugas menghitung TCP checksum dilempar OS ke NIC (TCP Checksum Offload) biar lebih efisien. Jadi paket aslinya sih tetap dikirim pakai checksum yang benar.

17. **Pengguna dapat membuka portal dengan alamat IP, tetapi tidak dengan nama. Gunakan model lapisan untuk menyusun diagnosis.**  
Artinya koneksi mulai layer Physical sampai Transport beres, buktinya IP bisa jalan. Kendalanya murni di Lapisan Aplikasi (Layer 7), yaitu macet di sistem resolusi DNS (port 53 terblokir atau server DNS salah isi).

18. **Ping ke server berhasil, tetapi HTTPS gagal. Susun sedikitnya enam hipotesis pada lapisan Transport hingga Application.**  
(1) Port 443 server sedang ditutup. (2) Firewall lokal men-drop akses port 443. (3) Web server/Aplikasi crash meski OS server jalan. (4) Sertifikat SSL/TLS invalid atau kedaluwarsa. (5) Gagal negosiasi keamanan TLS. (6) Kebijakan proxy jaringan kantor memutus akses web HTTPS.

19. **Bandingkan sesi aplikasi dengan koneksi TCP. Berikan contoh ketika sesi bertahan setelah koneksi berubah.**  
TCP itu cuma koneksi pengiriman di bawah yang sifatnya fisik/sementara. Sesi aplikasi itu kondisi logis berjangka panjang. Contohnya akun Instagram kita tetap login (sesi aplikasi) meski kita keluar rumah dan sambungan HP ganti dari Wi-Fi ke Mobile Data (TCP putus dan nyambung baru).

20. **Jelaskan mengapa enkripsi tidak dapat selalu ditempatkan secara mutlak pada Presentation layer.**  
Praktiknya enkripsi bisa ditempel di semua lapisan tergantung kebutuhan. Mengamankan hardware switch ke router pakai MACsec (L2), VPN kantor pakai IPsec (L3), transaksi bank pakai SSL/TLS (L4/L5), dan mengunci file ZIP (L7) sebelum masuk jaringan.

21. **Evaluasi pernyataan: “Model OSI tidak lagi relevan karena Internet menggunakan TCP/IP.” Susun argumen akademik yang membedakan model, protokol, dan kegunaan pedagogis.**  
Pernyataan itu menyesatkan. Memang protokol implementasi dunia nyatanya adalah TCP/IP karena lincah. Tapi sebagai bahan ajar, peta jalan, dan bahasa standar teknisi saat memperbaiki error (troubleshooting), model konseptual OSI tetap jadi rajanya (sangat relevan).

22. **Analisis keuntungan dan kerugian *strict layering*. Kapan cross-layer information dapat membantu dan kapan ia merusak modularitas?**  
Aturan pembatasan lapis yang kaku (strict layering) bagus supaya gampang dikelola, kalau mau perbaiki 1 layer nggak ngerusak sistem lain. Tapi kelemahannya jadi kurang lincah. Informasi lintas layer (misal TCP minta laporan sinyal Wi-Fi lagi jelek ke layer bawah) sangat optimal buat perbaikan peforma, tapi rentan bikin error jangka panjang karena layer-layer jadi saling ketergantungan.

---

## Soal 1 – Analisis Alamat IP

Diketahui daftar alamat IP di bawah ini:
1. `21.26.8.5`
2. `212.6.8.3`
3. `103.24.56.32`
4. `1.1.1.1`
5. `172.31.16.8`

**Tentukan komponen berikut untuk tiap alamat:**
- IP Network
- IP Gateway (Host Pertama)
- IP Host Terakhir
- Alamat Broadcast

### Jawaban Soal 1:

| No | IP Address | Kelas/Prefix | IP Network | Host Awal / Gateway | Host Akhir | Alamat Broadcast |
|:--:|:-----------|:-------------|:-----------|:--------------------|:-----------|:-----------------|
| 1 | `21.26.8.5` | Kelas A (`/8`) | `21.0.0.0` | `21.0.0.1` | `21.255.255.254` | `21.255.255.255` |
| 2 | `212.6.8.3` | Kelas C (`/24`) | `212.6.8.0` | `212.6.8.1` | `212.6.8.254` | `212.6.8.255` |
| 3 | `103.24.56.32` | Kelas A (`/8`) | `103.0.0.0` | `103.0.0.1` | `103.255.255.254` | `103.255.255.255` |
| 4 | `1.1.1.1` | Kelas A (`/8`) | `1.0.0.0` | `1.0.0.1` | `1.255.255.254` | `1.255.255.255` |
| 5 | `172.31.16.8` | Kelas B (`/16`) | `172.31.0.0` | `172.31.0.1` | `172.31.255.254` | `172.31.255.255` |

---

## Soal 2 – Visualisasi Sinyal Harmonisasi

Simulasi perancangan sinyal harmonisasi pada deret harmonik 1, 3, 5, 7, 9, dan 10 menggunakan bahasa Python.

<details>
<summary><b>Klik untuk melihat source code Python (main.py)</b></summary>

```python
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 5000)
f0 = 1
batas_harmonik = [1, 3, 5, 7, 9, 10]
fig, ax = plt.subplots(figsize=(10, 6))

for batas in batas_harmonik:
    sinyal = np.zeros_like(t)
    for n in range(1, batas + 1, 2):
        sinyal += np.sin(2 * np.pi * n * f0 * t) / n

    label = f"Harmonik 1 s/d {batas}"
    if batas == 10:
        sinyal += np.sin(2 * np.pi * 10 * f0 * t) / 10
        label += " (genap)"

    ax.plot(t, sinyal, label=label, linewidth=1.2)

ax.set_title("Simulasi Pembentukan Sinyal Digital di "
             "Physical Layer (Fourier Series)")
ax.set_xlabel("Waktu (detik)")
ax.set_ylabel("Amplitudo")
ax.axhline(0, color="black", linestyle="--", linewidth=0.7)
ax.set_xticks(np.arange(0, 2.01, 0.25))
ax.set_ylim(-1.1, 1.1)
ax.grid(True, linestyle=":", alpha=0.5)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
output = Path(__file__).resolve().with_name("visualisasi_square.png")
fig.savefig(output, dpi=180)
print(f"Grafik disimpan: {output}")
plt.show()
```

</details>

**Output Visualisasi:**  
![Hasil Eksekusi Visualisasi](visualisasi_square.jpg)

---

## Soal 3 – Subnetting Jaringan

Kasus subnetting untuk merincikan spesifikasi IP Network, Subnet Mask, rentang Host, hingga kapasitas per subnet.

### Bagian 1: `192.168.1.0/24` dipecah jadi 4 Subnet
- **Proses:** Kita ingin memecah jadi 4 bagian, artinya pinjam 2 bit (2^2 = 4 subnet). Prefix /24 berubah jadi /26.
- **Ukuran per blok:** Total IP ada 64 buah per subnet, dengan Host Valid sejumlah 62.

| Subnet Ke- | IP Network | Masker (/Prefix) | Awal | Akhir | Broadcast | Kapasitas Host |
|:----------:|:-----------|:-----------------|:-----|:------|:----------|:--------------:|
| 1 | `192.168.1.0` | `255.255.255.192` (/26) | `192.168.1.1` | `192.168.1.62` | `192.168.1.63` | 62 |
| 2 | `192.168.1.64` | `255.255.255.192` (/26) | `192.168.1.65` | `192.168.1.126` | `192.168.1.127` | 62 |
| 3 | `192.168.1.128` | `255.255.255.192` (/26) | `192.168.1.129` | `192.168.1.190` | `192.168.1.191` | 62 |
| 4 | `192.168.1.192` | `255.255.255.192` (/26) | `192.168.1.193` | `192.168.1.254` | `192.168.1.255` | 62 |

---

### Bagian 2: `132.10.0.0/16` dipecah jadi 10 Subnet
- **Proses:** Untuk dapat minimal 10 subnet, butuh 4 bit pinjaman (2^4 = 16 rentang yang terbentuk). Prefix jadi /20.
- **Ukuran per blok:** Bloknya melompat kelipatan 16 di oktet ketiga. Setiap rentang mampu menampung 4.094 host.

| Subnet Ke- | IP Network | Masker (/Prefix) | Awal | Akhir | Broadcast | Kapasitas Host |
|:----------:|:-----------|:-----------------|:-----|:------|:----------|:--------------:|
| 1 | `132.10.0.0` | `255.255.240.0` (/20) | `132.10.0.1` | `132.10.15.254` | `132.10.15.255` | 4094 |
| 2 | `132.10.16.0` | `255.255.240.0` (/20) | `132.10.16.1` | `132.10.31.254` | `132.10.31.255` | 4094 |
| 3 | `132.10.32.0` | `255.255.240.0` (/20) | `132.10.32.1` | `132.10.47.254` | `132.10.47.255` | 4094 |
| 4 | `132.10.48.0` | `255.255.240.0` (/20) | `132.10.48.1` | `132.10.63.254` | `132.10.63.255` | 4094 |
| 5 | `132.10.64.0` | `255.255.240.0` (/20) | `132.10.64.1` | `132.10.79.254` | `132.10.79.255` | 4094 |
| 6 | `132.10.80.0` | `255.255.240.0` (/20) | `132.10.80.1` | `132.10.95.254` | `132.10.95.255` | 4094 |
| 7 | `132.10.96.0` | `255.255.240.0` (/20) | `132.10.96.1` | `132.10.111.254` | `132.10.111.255` | 4094 |
| 8 | `132.10.112.0` | `255.255.240.0` (/20) | `132.10.112.1` | `132.10.127.254` | `132.10.127.255` | 4094 |
| 9 | `132.10.128.0` | `255.255.240.0` (/20) | `132.10.128.1` | `132.10.143.254` | `132.10.143.255` | 4094 |
| 10 | `132.10.144.0` | `255.255.240.0` (/20) | `132.10.144.1` | `132.10.159.254` | `132.10.159.255` | 4094 |

---

### Bagian 3: `17.8.0.0/16` dipecah jadi 4 Subnet
- **Proses:** Membutuhkan pinjaman 2 bit ke oktet ketiga agar pecah jadi 4 rute (prefix jadi /18).
- **Ukuran per blok:** Melompat setiap 64 angka di oktet ketiga, daya tampungnya mencapai 16.382 alamat per blok.

| Subnet Ke- | IP Network | Masker (/Prefix) | Awal | Akhir | Broadcast | Kapasitas Host |
|:----------:|:-----------|:-----------------|:-----|:------|:----------|:--------------:|
| 1 | `17.8.0.0` | `255.255.192.0` (/18) | `17.8.0.1` | `17.8.63.254` | `17.8.63.255` | 16382 |
| 2 | `17.8.64.0` | `255.255.192.0` (/18) | `17.8.64.1` | `17.8.127.254` | `17.8.127.255` | 16382 |
| 3 | `17.8.128.0` | `255.255.192.0` (/18) | `17.8.128.1` | `17.8.191.254` | `17.8.191.255` | 16382 |
| 4 | `17.8.192.0` | `255.255.192.0` (/18) | `17.8.192.1` | `17.8.255.254` | `17.8.255.255` | 16382 |

---

### Bagian 4: `8.32.0.0/12` dipecah jadi 6 Subnet
- **Proses:** Bawaan /12 pinjam 3 bit supaya bisa menciptakan maksimal 8 subnet (2^3 = 8). Targetnya cuma butuh 6 blok subnet, prefix ganti jadi /15.
- **Ukuran per blok:** Pertambahannya 2 blok IP besar pada oktet kedua, memberi ruang hingga 131.070 host aktif per subnet.

| Subnet Ke- | IP Network | Masker (/Prefix) | Awal | Akhir | Broadcast | Kapasitas Host |
|:----------:|:-----------|:-----------------|:-----|:------|:----------|:--------------:|
| 1 | `8.32.0.0` | `255.254.0.0` (/15) | `8.32.0.1` | `8.33.255.254` | `8.33.255.255` | 131070 |
| 2 | `8.34.0.0` | `255.254.0.0` (/15) | `8.34.0.1` | `8.35.255.254` | `8.35.255.255` | 131070 |
| 3 | `8.36.0.0` | `255.254.0.0` (/15) | `8.36.0.1` | `8.37.255.254` | `8.37.255.255` | 131070 |
| 4 | `8.38.0.0` | `255.254.0.0` (/15) | `8.38.0.1` | `8.39.255.254` | `8.39.255.255` | 131070 |
| 5 | `8.40.0.0` | `255.254.0.0` (/15) | `8.40.0.1` | `8.41.255.254` | `8.41.255.255` | 131070 |
| 6 | `8.42.0.0` | `255.254.0.0` (/15) | `8.42.0.1` | `8.43.255.254` | `8.43.255.255` | 131070 |

---

## Soal 4 – Analisis Traceroute & Mekanisme TTL

Berikut penjabaran fungsi dan mekanika *Traceroute* serta kaitannya dengan batas hidup IP (TTL).

1. **Apa itu Traceroute?**  
   Alat bantu sistem jaringan yang bertugas mencari dan menggambar jalur yang dilewati paket data (lompatan router) menuju host tujuan. Selain menampilkan alamat hop, ia juga memperlihatkan total delay (RTT) ke titik tersebut.

2. **Peran TTL (Time To Live)**  
   TTL ibarat nyawa suatu paket (maksimal angka 255). Fungsinya mencegah paket yang nyasar di jaringan berputar-putar tanpa batas (looping). Tiap ada router yang memproses paket, nilai nyawa (TTL) dipotong 1. Kalau nilai TTL menyentuh 0, router akan menghapus paket itu.

3. **Rahasia Traceroute Memanfaatkan TTL**  
   Traceroute melakukan pelacakan secara perlahan dengan sengaja mengirimkan paket ber-TTL kecil. 
   - Pertama, ia kirim IP paket dengan `TTL=1`. Paket langsung "mati" di Router ke-1. Router 1 kirim laporan, sehingga Traceroute dapat alamat Router 1.
   - Kedua, ia kirim lagi paket dengan `TTL=2`. Router 1 memotong jadi 1, diteruskan ke Router 2 dan paket mati di situ. Traceroute dapat info rute hop-2.
   - Hal ini terus diulang dengan `TTL=3, 4, ...` sampai berhasil menyentuh tujuan.

4. **Keterlibatan Protokol ICMP**  
   Proses deteksi di atas tidak akan jalan tanpa umpan balik ICMP. Setiap router yang membunuh paket gara-gara TTL=0 akan melapor ke pengirim dengan sandi *ICMP Time Exceeded (Type 11)*. Berbekal laporan pesan inilah Traceroute mengenali rute jaringannya.

---

## Soal 5 – Subnetting metode VLSM

Membedah pengalokasian IP `10.252.108.0/24` untuk empat gedung/departemen supaya hemat ruang menggunakan prinsip Variable Length Subnet Mask (VLSM).

**Syarat Mutlak VLSM:** Rentang IP wajib disebar berurutan, dimulai dari area yang membutuhkan ruang terbanyak ke area dengan kebutuhan paling ramping supaya tidak tumpang-tindih (overlap).
- Urutan: Lab A (90) -> Lab B (60) -> Admin (14) -> P2P (4).

#### Ringkasan Kalkulasi VLSM:
1. **Lab A (90 Host):** Butuh penampung ukuran 128 alamat IP. Karena itu dialokasikan ke prefix /25 (maks 126 host aktif).
2. **Lab B (60 Host):** Target penampung 64 alamat IP. Melanjutkan sisa sebelumnya, prefix yang cocok adalah /26.
3. **Administrasi (14 Host):** Sesuai blok 16 IP, digunakan prefix /28 (pas menyediakan 14 IP aktif).
4. **Jalur P2P (4 Host):** Butuh blok ukuran 8 (karena blok isi 4 cuma menyisakan 2 host). Diberikan porsi prefix /29.

#### Tabel Hasil Pembagian:

| Area Jaringan | Jumlah Host | IP Network | Masker (/Prefix) | IP Awal | IP Akhir | Broadcast | Sisa Tersedia |
|:--------------|:-----------:|:-----------|:-----------------|:--------|:---------|:----------|:-------------:|
| **Laboratorium A** | 90 | `10.252.108.0` | `255.255.255.128` (/25) | `10.252.108.1` | `10.252.108.126` | `10.252.108.127` | 126 |
| **Laboratorium B** | 60 | `10.252.108.128` | `255.255.255.192` (/26) | `10.252.108.129` | `10.252.108.190` | `10.252.108.191` | 62 |
| **Administrasi** | 14 | `10.252.108.192` | `255.255.255.240` (/28) | `10.252.108.193` | `10.252.108.206` | `10.252.108.207` | 14 |
| **Tautan P2P** | 4 | `10.252.108.208` | `255.255.255.248` (/29) | `10.252.108.209` | `10.252.108.214` | `10.252.108.215` | 6 |

*(Sisa rentang IP mulai dari `10.252.108.216/29` ke atas dibiarkan nganggur untuk kebutuhan masa depan).*
