#Permasalahan Modul 3

bahan_bakar_awal = 120        
bahan_bakar_isi_ulang = 20    
membutuhkan_per_putaran = 5      
putaran_per_pitstop = 10      
jumlah_ban_per_ganti = 4      

total_bahan_bakar = bahan_bakar_awal
total_ban_digunakan = 0
jumlah_pitstop = 0
putaran_saat_ini = 0 

maks_simulasi = 1000 

print(f"--- SIMULASI BALAPAN DIMULAI ---")
print(f"Bahan Bakar Awal: {bahan_bakar_awal}L, Konsumsi: {membutuhkan_per_putaran}L/Putaran.")
print("-" * 60)


for i in range(1, maks_simulasi + 1):
    if total_bahan_bakar < membutuhkan_per_putaran:
        print(f"Bahan Bakar ({total_bahan_bakar:.2f}L) tidak cukup untuk putaran berikutnya.")
        break 
        
    total_putaran = i 
    putaran_saat_ini += 1
    total_bahan_bakar -= membutuhkan_per_putaran
    pesan_status = f"Putaran {total_putaran:02d}: Bahan Bakar berkurang {membutuhkan_per_putaran}L. Bahan Bakar Sisa: {total_bahan_bakar:02d}L. "
    if putaran_saat_ini == putaran_per_pitstop:
        jumlah_pitstop += 1
        putaran_saat_ini = 0 
        total_bahan_bakar += bahan_bakar_isi_ulang
        total_ban_digunakan += jumlah_ban_per_ganti
        pesan_status += (f"* PIT STOP KE-{jumlah_pitstop:02d}! (+{bahan_bakar_isi_ulang}L Bahan Bakar, +{jumlah_ban_per_ganti} Ban). Bahan Bakar Baru: {total_bahan_bakar:02d}L. *")
    
    else:
        pesan_status += "Tidak ada Pit Stop."
    print(pesan_status)
        
print("-" * 60)
print("--- SIMULASI SELESAI ---")
print(f"Total Putaran yang ditempuh: {total_putaran} putaran")
print(f"Jumlah Pit Stop (Pengisian Bahan Bakar & Ganti Ban): {jumlah_pitstop} kali")
print(f"Total Ban yang digunakan: {total_ban_digunakan} ban")
print(f"Sisa Bahan Bakar (kurang dari 5L): {total_bahan_bakar:.2f} liter")
